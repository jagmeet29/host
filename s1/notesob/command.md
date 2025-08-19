# Ollama Commands Reference

Here's a comprehensive table of essential **Ollama** commands for managing and interacting with **large language models** locally

## Core **Ollama CLI** Commands

| Command          | Description                          | Example Usage         |
|------------------|--------------------------------------|-----------------------|
| **ollama serve** | Starts the **Ollama** server/daemon  | `code_line ollama serve` |
| **ollama run**   | Runs a model and starts interactive chat | `code_line ollama run llama3.2` |
| **ollama pull**  | Downloads a model from the registry   | `code_line ollama pull mistral` |
| **ollama list**  | Lists all downloaded models          | `code_line ollama list` or `code_line ollama ls` |
| **ollama ps**    | Shows currently running models       | `code_line ollama ps` |
| **ollama stop**  | Stops a specific running model       | `code_line ollama stop llama3.2` |
| **ollama rm**    | Removes/deletes a model              | `code_line ollama rm mistral` |
| **ollama show**  | Displays detailed model information  | `code_line ollama show llama3.2` |
| **ollama create**| Creates a custom model from **Modelfile** | `code_line ollama create my-model -f ./Modelfile` |
| **ollama cp**    | Copies a model to a new name          | `code_line ollama cp llama3.2 my-llama` |
| **ollama push**  | Pushes a model to remote registry     | `code_line ollama push my-model` |
| **ollama help**  | Shows help for commands              | `code_line ollama help` or `code_line ollama help run` |

## Interactive Session Commands

When running a model with **ollama run**, these commands work within the chat session:

| Command   | Description                        | Example Usage         |
|-----------|------------------------------------|-----------------------|
| **/help** or **/?** | Shows available session commands | `/help` |
| **/show** | Displays current model information | `/show` |
| **/set**  | Sets session variables             | `/set temperature 0.8` |
| **/load** | Loads a session or model           | `/load my-session` |
| **/save** | Saves current session              | `/save my-session` |
| **/clear**| Clears session context             | `/clear` |
| **/bye**  | Exits the interactive session      | `/bye` |

## Common Usage Examples

**Single prompt without interactive mode:**
```bash
ollama run llama3.2 "What are the benefits of renewable energy?"
```

**Running with specific parameters:**
```bash
ollama run llama3.2 --verbose
```

**Downloading multiple models:**
```bash
ollama pull llama3.2
ollama pull mistral
ollama pull codellama
```

**Checking system status:**
```bash
ollama ps              # See what's running
ollama list            # See what's downloaded
ollama --version       # Check **Ollama** version
```

## Model Management Tips

**Creating custom models:** Use a **Modelfile** to define parameters, prompts, and base models. Example **Modelfile:**
```yaml
FROM llama3.2
PARAMETER temperature 0.8
SYSTEM You are a helpful coding assistant.
```

**Environment variables** for **ollama serve**:
- `OLLAMA_DEBUG` - Enable debugging
- `OLLAMA_HOST` - Specify server host
- `OLLAMA_MAX_QUEUE` - Set max queued requests

**Automation:** You can create bash scripts to automate **Ollama** tasks and set up cron jobs for scheduled operations.

These commands provide complete control over your local **AI models**, from downloading and running to customization and management. The **Ollama** server runs on port 11434 by default and provides both **CLI** and **API** access to your models.

# PowerShell File Handling Commands Reference

Here's a comprehensive table of essential **PowerShell** file handling commands and their most useful parameters:

## Basic File Handling Commands

| Command           | Description                        | Key Parameters                                  | Example Usage                            |
|-------------------|------------------------------------|------------------------------------------------|------------------------------------------|
| **Get-ChildItem** | Lists files and directories        | `-Path`, `-Recurse`, `-Force`, `-Filter`, `-Include`, `-Exclude`, `-File`, `-Directory` | `Get-ChildItem -Path C: -Recurse -Force` |
| **Get-Item**      | Gets specific file or directory information | `-Path`, `-Force`, `-Filter` | `Get-Item -Path "C:\file.txt"` |
| **Test-Path**     | Tests if path exists               | `-Path`, `-PathType`                           | `Test-Path -Path "C:\file.txt"`          |
| **Split-Path**    | Returns parts of a path            | `-Path`, `-Parent`, `-Leaf`, `-Extension`      | `Split-Path -Path "C:\folder\file.txt" -Leaf` |
| **Join-Path**     | Combines path elements             | `-Path`, `-ChildPath`                          | `Join-Path -Path "C:\folder" -ChildPath "file.txt"` |
| **Resolve-Path**  | Resolves wildcards in paths        | `-Path`                                       | `Resolve-Path -Path "C:\*\file.txt"`     |

## File Content Commands

| Command            | Description                         | Key Parameters                                          | Example Usage                                                    |
| ------------------ | ----------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------- |
| **Get-Content**    | Reads content from files            | `-Path`, `-Raw`, `-Encoding`                            | `Get-Content -Path "file.txt"`                                   |
| **Set-Content**    | Writes content to files             | `-Path`, `-Value`, `-Encoding`, `-Force`                | `Set-Content -Path "file.txt" -Value "Hello World"`              |
| **Add-Content**    | Appends content to files            | `-Path`, `-Value`, `-Encoding`, `-Force`                | `Add-Content -Path "log.txt" -Value "New entry"`                 |
| **Out-File**       | Sends output to a file              | `-FilePath`, `-Encoding`, `-Append`, `-Force`, `-Width` | `"Hello"` \| `Out-File -FilePath "output.txt"`                   |
| **Select-String**  | Searches for text patterns in files | `-Path`, `-Pattern`, `-SimpleMatch`, `-CaseSensitive`   | `Select-String -Path "*.log" -Pattern "error"`                   |
| **Get-FileHash**   | Calculates file hash values         | `-Path`, `-Algorithm`                                   | `Get-FileHash -Path "file.txt" -Algorithm SHA256`                |
| **Compare-Object** | Compares file contents              | `-ReferenceObject`, `-DifferenceObject`                 | `Compare-Object (Get-Content file1.txt) (Get-Content file2.txt)` |

## File Attribute and Permission Commands

| Command        | Description                       | Key Parameters         | Example Usage                            |
|----------------|-----------------------------------|------------------------|------------------------------------------|
| **Get-Acl**    | Gets access control lists         | `-Path`                | `Get-Acl -Path "C:\file.txt"`             |
| **Set-Acl**    | Sets access control lists         | `-Path`, `-AclObject`   | `Set-Acl -Path "file.txt" -AclObject $acl` |
| **Get-ItemProperty**| Gets file properties             | `-Path`, `-Name`       | `Get-ItemProperty -Path "file.txt" -Name LastWriteTime` |
| **Set-ItemProperty**| Sets file properties             | `-Path`, `-Name`, `-Value` | `Set-ItemProperty -Path "file.txt" -Name IsReadOnly -Value $true` |

## Key Parameter Explanations

**Common Parameters:**
- **-Path**: Specifies the file or directory path
- **-Recurse**: Processes subdirectories recursively
- **-Force**: Forces the operation even for hidden/system files
- **-Filter**: Specifies a filter pattern for file names
- **-Include**: Includes only specified items
- **-Exclude**: Excludes specified items

**File Type Filters:**
- **-File**: Returns only files
- **-Directory**: Returns only directories

**Content Parameters:**
- **-Encoding**: Specifies text encoding (UTF8, ASCII, etc.)
- **-Raw**: Returns content as single string instead of array
- **-Append**: Appends to existing file instead of overwriting

These commands form the foundation of file management in **PowerShell**, allowing you to perform virtually any file operation from the command line with powerful filtering and processing capabilities.

