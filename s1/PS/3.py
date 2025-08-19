from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from InquirerLib import prompt_async
import re
import asyncio
from ollama import AsyncClient
import os
import pyperclip
from contextlib import suppress
from playsound import playsound
from collections import deque

# --- Audio helpers ---------------------------------------------------------
async def safe_play(path: str, console: Console):
    """Play a sound file safely (non-blocking to event loop)."""
    if not path:
        return
    try:
        if os.path.exists(path):
            await asyncio.to_thread(playsound, path)
        else:
            console.print(f"[yellow]Sound file not found: {path}[/yellow]")
    except Exception as e:
        console.print(f"[yellow]Sound play failed for {os.path.basename(path)}: {e}[/yellow]")


class real_time:
    def __init__(self, model="mistral-small3.2:latest"):
        self.model = model
        self.generationStart = False

    async def pregeneration(self, edited_file_text, file_text, layout, console):
        text_display = edited_file_text.split("\n\n#")
        text_display_raw = file_text.split("\n\n#")
        try:
            for i in range(min(len(text_display_raw), len(text_display))):
                layout["Head"].update(Panel("🔎 Links Detected", border_style="#0DA643", height=3))
                layout["Body"].update(Panel(Markdown(text_display_raw[i]), style="#F2F0D8", title="View", border_style="#F2884B"))
                await asyncio.sleep(0.3)
                layout["Head"].update(Panel("✅ Links Removed", border_style="#0DA643", height=3))
                layout["Body"].update(Panel(Markdown(text_display[i]), title="View", style="#F2F0D8", border_style="#F2884B"))
                await asyncio.sleep(0.3)
            layout["Head"].update(Panel("🔮 Sent To Ollama", border_style="#0DA643", height=3))
            layout["Body"].update(Panel(" ", title="View", style="#F2F0D8", border_style="#F2884B"))
        except asyncio.CancelledError:
            pass
        except Exception as e:
            console.print(f"[red]Pregeneration error: {e}[/red]")
        return

    async def response_full(self, message_content, edited_file_text, file_text, layout, console):
        content = ""
        print(message_content)
        # Resolve sound file paths relative to this script
        base_dir = os.path.dirname(__file__)
        processing_sound = os.path.join(base_dir, 'processing.mp3')
        completion_sound = os.path.join(base_dir, 'out.mp3')

        pregentask = asyncio.create_task(self.pregeneration(edited_file_text, file_text, layout, console))
        try:
            client = AsyncClient()
            response_stream = await client.chat(
                model=self.model,
                messages=[{'role': 'user', 'content': message_content}],
                stream=True
            )
            async for chunk in response_stream:
                if not self.generationStart:
                    self.generationStart = True
                    pregentask.cancel()
                    with suppress(asyncio.CancelledError):
                        await pregentask
                    layout["Head"].update(Panel("🔮 Sent To Ollama", border_style="#0DA643", height=3))
                    layout["Body"].update(Panel(" ", title="View", style="#F2F0D8", border_style="#F2884B"))
                    # Play a single processing sound (optional)
                    await safe_play(processing_sound, console)
                token = chunk.get('message', {}).get('content', '')
                if token:
                    content += token  # accumulate full content for clipboard
                    # Streaming display config
                    MAX_TOTAL_CHARS = 700
                    MAX_VISIBLE_LINES = 20
                    if 'lines_deque' not in locals():
                        lines_deque = deque()
                        current_line = ''
                        total_chars = 0

                    for ch in token:
                        if ch == '\n':
                            # finalize line (no per-line sound to avoid spam & Error 259)
                            lines_deque.append(current_line)
                            total_chars += len(current_line) + 1
                            current_line = ''
                            while total_chars > MAX_TOTAL_CHARS and lines_deque:
                                removed = lines_deque.popleft()
                                total_chars -= len(removed) + 1
                        else:
                            current_line += ch
                        visible_lines = list(lines_deque)
                        if current_line:
                            visible_lines.append(current_line)
                        if len(visible_lines) > MAX_VISIBLE_LINES:
                            visible_lines = visible_lines[-MAX_VISIBLE_LINES:]
                        visible_text = "\n".join(visible_lines)
                        layout["Head"].update(Panel("✨ Response ready!", border_style="#0DA643", height=3))
                        layout["Body"].update(Panel(Markdown(visible_text), title="View", style="#F2F0D8", border_style="#F2884B"))
            if 'current_line' in locals() and current_line:
                pass
            if content.strip():
                try:
                    pyperclip.copy(content)
                except pyperclip.PyperclipException as e:
                    console.print(f"[red]Clipboard copy failed: {e}[/red]")
                # Play completion sound once
                await safe_play(completion_sound, console)
        except Exception as e:
            pregentask.cancel()
            console.print(f"[red]Stream error: {e}[/red]")
        return


async def main():
    layout = Layout()
    layout.split_column(
        Layout(Panel("Head"), name="Head", size=3),
        Layout(Panel("Body"), name="Body")
    )
    console = Console()

    with open("Hosted/s1/notesob/out.md", "r", encoding="utf-8") as f:
        file_text = f.read()

    edited_file_text = re.sub(r"(\d+)?\. \[(.*?)\]\((.*?)\)", r"", file_text)
    edited_file_text = re.sub(r"\[(.*?)\]\((.*?)\)", r"", edited_file_text)

    questions = [{
        "type": "list",
        "message": "Formatting Type ?",
        "choices": ["Text","Custom"],
        "name": "type_name"
    }]
    prompt_type = await prompt_async(questions)

    parts = []
    if prompt_type["type_name"] in ("Text"):
        with open("Hosted/s1/notesob/Chats/text.md", "r", encoding="utf-8") as f:
            parts.append(f.read())
    if prompt_type["type_name"] in ("Custom"):
        with open("Hosted/s1/notesob/Chats/custom.md", "r", encoding="utf-8") as f:
            parts.append(f.read())


    Combined_Message = "\n".join(parts) + f"\n\ncontent:[\n{edited_file_text}\n]\n"

    rt = real_time()
    with Live(layout, console=console, refresh_per_second=24):
        await rt.response_full(Combined_Message, edited_file_text, file_text, layout, console)


asyncio.run(main())
