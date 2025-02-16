import tkinter as tk
import subprocess
import os
import signal
from tkinter import Tk, Label, Canvas
from PIL import ImageTk, Image

# Create a Tkinter window
root = tk.Tk()
root.title("Drowsiness Detection System")

# Set the window size and position to cover the whole screen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Create a function to run the Python file
process = None

def start_detection():
    global process
    if process is None:
        process = subprocess.Popen(["python", "drowsiness detection.py"])

def stop_detection():
    global process
    if process is not None:
        os.kill(process.pid, signal.SIGTERM)
        process = None

root.configure(background='#FFF9D0')
# Add a message label for the college name
message_label = tk.Label(root, text="AISSMS College of Engineering",
                         font=("Arial", 20), fg="purple", bg='#CAF4FF')
message_label.pack(pady=20)

# Add a message label for the department name 
message_label = tk.Label(root, text="Department of Computer Engineering",
                         font=("Arial", 20), bg='#CAF4FF')
message_label.pack(pady=25)

# Add a message label for the system name
message_label = tk.Label(root, text="Drowsiness Detection and Alert System",
                         font=("Arial", 20), fg="black", bg='#CAF4FF')
message_label.pack(pady=50)

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create the start button
start_button = tk.Button(button_frame, text="Start", font=("Arial", 16),
                         fg="green", bg="white", width=10, height=3, command=start_detection)
start_button.pack(side=tk.LEFT, padx=20, pady=20)

# Create the stop button
stop_button = tk.Button(button_frame, text="Stop", font=("Arial", 16),
                        fg="red", bg="white", width=10, height=3, command=stop_detection)
stop_button.pack(side=tk.RIGHT, padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()
