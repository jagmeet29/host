import tkinter as tk
import time
import threading
import os
import pygame  # Better alternative to playsound

def show_red_screen():
    # Create the main window
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="#232323")
    
    # Add a message to the screen
    message = tk.Label(root, text="Time for a break ! ", font=("Sail", 100), fg="#A8D991", bg="#232323")
    message.pack(expand=True)
    
    # Play sound using pygame (more reliable than playsound)
    try:
        pygame.mixer.init()
        sound_path = os.path.join("PS", "break.mp3")  # Proper path handling
        if os.path.exists(sound_path):
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
        else:
            print(f"Audio file not found: {sound_path}")
    except Exception as e:
        print(f"Could not play sound: {e}")
    
    # Function to close the window
    def close_win(event=None):
        try:
            pygame.mixer.quit()  # Clean up pygame
        except:
            pass
        root.destroy()

    # Bind the Escape key to close the window
    root.bind('<Escape>', close_win)
    
    # Keep the window on top of all others
    root.attributes('-topmost', True)
    
    # Set a timer to close the window automatically after 1 minute (60000 milliseconds)
    root.after(30000, close_win)
    
    root.mainloop()

def start_timer(minutes):
    """Waits for a specified number of minutes then shows the red screen."""
    while True:
        print(f"Timer started for {minutes} minutes.")
        time.sleep(minutes * 60)
        print("Time's up! Displaying red screen.")
        
        # Tkinter GUI calls must be in the main thread.
        # We start a separate thread for the GUI.
        gui_thread = threading.Thread(target=show_red_screen)
        gui_thread.start()
        gui_thread.join() # Wait for the red screen to be closed

if __name__ == "__main__":
    # Set the timer for 25 minutes (using 1 for testing)
    timer_thread = threading.Thread(target=start_timer, args=(25,))
    timer_thread.daemon = True # Allows the main program to exit even if the thread is running
    timer_thread.start()

    print("The break reminder is running in the background.")
    print("Press Ctrl+C in the console to stop.")
    
    # Keep the main script alive.
    try:
        # This loop is just to keep the main thread alive.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTimer stopped by user.")

