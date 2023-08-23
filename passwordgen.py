import string
import random
import tkinter as tk

def passgenerator():
    current_state = generatedpass.cget("state")
    new_state = tk.NORMAL if current_state == tk.DISABLED else tk.DISABLED
    generatedpass.config(state=new_state)

    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation

    passlen = int(textbox.get("1.0", "end-1c"))

    s = []

    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))

    random.shuffle(s)

    pas = ("".join(s[0:passlen]))
    generatedpass.insert("1.0", str(pas))
    generatedpass.config(state=tk.DISABLED)

def clear_password():
    current_state = generatedpass.cget("state")
    new_state = tk.NORMAL if current_state == tk.DISABLED else tk.DISABLED
    generatedpass.config(state=new_state)

    textbox.delete("1.0", "end")
    generatedpass.delete("1.0", "end")
    generatedpass.config(state=tk.DISABLED)

root = tk.Tk()
root.geometry("300x180")
root.title("Password Generator")
frame = tk.Frame(root)
frame.pack()

label = tk.Label(
    frame, 
    text="Enter the password length: "
)
label.pack()

textbox = tk.Text(frame, height=1, width=10)
textbox.pack()

button = tk.Button(
    frame,
    text="Generate",
    command=passgenerator
)
button.pack()

generatedpass = tk.Text(frame, height=5, width=30, state=tk.DISABLED)
generatedpass.pack()

clear = tk.Button(
    frame,
    text="Clear",
    command=clear_password
)
clear.pack()

root.mainloop()