import keyboard
import random
import time
import tkinter as tk
from tkinter import scrolledtext
import string
from tkinter import messagebox


def type_with_random_delay(text, min_delay, max_delay):
    for char in text:
        # Get slider value as a percentage (0–99), convert to threshold between 0 and 1
        threshold = current_value.get() / 100.0

        if random.random() < threshold:
            wrong_char = random.choice(string.ascii_letters + string.punctuation + string.digits)
            keyboard.write(wrong_char)
            time.sleep(random.uniform(0.05, 0.3))
            keyboard.press_and_release("backspace")
            time.sleep(random.uniform(0.05, 0.3))

        # Type the correct character
        keyboard.write(char)
        time.sleep(random.uniform(min_delay, max_delay))

def get_input():
    user_text = text_box.get("1.0", tk.END).strip()  # Get all text from the box
    print("User entered:\n", user_text)

    # Get delay values from textboxes
    try:
        min_delay = float(min_delay_box.get())
        max_delay = float(max_delay_box.get())
    except ValueError:
        print("Invalid delay values. Please enter numbers.")
        return

    # Wait for space key before typing
    print("Press SPACE to start typing...")
    keyboard.wait("space")
    time.sleep(1)
    keyboard.press_and_release("backspace")

    if len(user_text.split()) > 1:
        type_with_random_delay(user_text, min_delay, max_delay)
        keyboard.press_and_release('enter')
        messagebox.showinfo("INFO!!!!!!", "done :D")
    else:
        print("Text must contain multiple words to trigger the action.")

# Create main window
root = tk.Tk()
root.title("Text Inputer by Aleks R.") #by me:)
root.geometry("500x650")

# Label
tk.Label(root, text="Enter your text below, then click Submit and press SPACE", font=("Comic Sans MS", 12)).pack(pady=5)

# Scrollable large text box
text_box = scrolledtext.ScrolledText(root, height=10, width=50, font=("Comic Sans MS", 12), wrap="word")
text_box.pack(pady=5)

# Delay input boxes
delay_frame = tk.Frame(root)
delay_frame.pack(pady=5)

tk.Label(delay_frame, text="Min Delay (s):", font=("Comic Sans MS", 10)).grid(row=0, column=0, padx=5)
min_delay_box = tk.Entry(delay_frame, width=5)
min_delay_box.insert(0, "0.1")  # Default value
min_delay_box.grid(row=0, column=1, padx=5)

tk.Label(delay_frame, text="Max Delay (s):", font=("Comic Sans MS", 10)).grid(row=0, column=2, padx=5)
max_delay_box = tk.Entry(delay_frame, width=5)
max_delay_box.insert(0, "0.8")  # Default value
max_delay_box.grid(row=0, column=3, padx=5)

# Recommended text
tk.Label(root, text="Recommended 0.05 to 0.3 delay to make it more human", font=("Comic Sans MS", 10), fg="gray").pack(pady=2)

# Slider bar
current_value = tk.DoubleVar()

def slider_changed(event):
    value_label.config(text=f"Mistakes as a percentage: {current_value.get():.2f}")

slider = tk.Scale(
    root,
    from_=0,
    to=99,
    orient="horizontal",
    variable=current_value,
    command=slider_changed
)
slider.pack(pady=20)
slider.set(15)

value_label = tk.Label(root, text="Mistake percentage: 0.00")
value_label.pack()
tk.Label(root, text="Recommended: 15%", font=("Comic Sans MS", 10), fg="gray").pack(pady=2)

# Button to get input
tk.Button(root, text="Submit", command=get_input, font=("Comic Sans MS", 30)).pack(pady=10)

# Copyright text
tk.Label(root, text="(R) Aleks R. 2025", font=("Comic Sans MS", 10), fg="gray").pack(pady=2)

root.mainloop()
