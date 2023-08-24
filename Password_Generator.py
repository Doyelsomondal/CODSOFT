import tkinter as tk
import random
import string

def generate_password():
    password_length =int(length_entry.get())
    complexity = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(complexity) for _ in range(password_length))
    password_display.config(text ="Generated password: " +password)

def accept_password():
    accepted_password =password_display.cget("text").split(":")[1]
    username = username_entry.get()

def reset_password():
    password_display.config(text ="")
    generate_password()

root =tk.Tk()
root.title("password Generator")

root.configure(bg ="lightgrey")
tk.Label(root, text="Password Generator", font=("Helvetica", 16), bg="lightgray").pack(pady=10)


username_label = tk.Label(root, text="Enter Username:", font=("Helvetica", 12), bg="lightgray")
username_label.pack()

username_entry = tk.Entry(root,font=("Helvetica", 12))
username_entry.pack()

length_label = tk.Label(root, text="Enter Password Length", font=("Helvetica", 12), bg="lightgray")
length_label.pack()


length_entry = tk.Entry(root,font=("Helvetica", 12))
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12))
generate_button.pack(pady=10)

password_display = tk.Label(root, text="", font=("Helvetica", 12), bg="lightgray")
password_display.pack()

accept_button = tk.Button(root, text="Accept", command=accept_password, font=("Helvetica", 12))
accept_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_password, font=("Helvetica", 12))
reset_button.pack()



root.mainloop()
