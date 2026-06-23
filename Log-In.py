import tkinter as tk
from tkinter import messagebox

# Window
root = tk.Tk()
root.title("Modern Login")
root.geometry("500x600")
root.configure(bg="#121212")
root.resizable(False, False)

# Login function
def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# Main Card
card = tk.Frame(root, bg="#1E1E1E")
card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=450)

# Logo / Title
title = tk.Label(
    card,
    text="Welcome Back",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg="#1E1E1E"
)
title.pack(pady=(40, 10))

subtitle = tk.Label(
    card,
    text="Login to continue",
    font=("Segoe UI", 11),
    fg="#B0B0B0",
    bg="#1E1E1E"
)
subtitle.pack(pady=(0, 30))

# Username
user_label = tk.Label(
    card,
    text="Username",
    font=("Segoe UI", 10),
    fg="white",
    bg="#1E1E1E"
)
user_label.pack(anchor="w", padx=40)

user_entry = tk.Entry(
    card,
    font=("Segoe UI", 12),
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    relief="flat"
)
user_entry.pack(fill="x", padx=40, pady=(5, 20), ipady=10)

# Password
pass_label = tk.Label(
    card,
    text="Password",
    font=("Segoe UI", 10),
    fg="white",
    bg="#1E1E1E"
)
pass_label.pack(anchor="w", padx=40)

pass_entry = tk.Entry(
    card,
    show="•",
    font=("Segoe UI", 12),
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    relief="flat"
)
pass_entry.pack(fill="x", padx=40, pady=(5, 30), ipady=10)

# Login Button
login_btn = tk.Button(
    card,
    text="Login",
    font=("Segoe UI", 12, "bold"),
    bg="#4F46E5",
    fg="white",
    relief="flat",
    activebackground="#4338CA",
    activeforeground="white",
    cursor="hand2",
    command=login
)
login_btn.pack(fill="x", padx=40, ipady=10)

# Footer
footer = tk.Label(
    card,
    text="Forgot Password?",
    font=("Segoe UI", 9),
    fg="#4F46E5",
    bg="#1E1E1E",
    cursor="hand2"
)
footer.pack(pady=20)

root.mainloop()
