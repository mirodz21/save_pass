from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)


canvas = Canvas(width=200, height=200)
img = PhotoImage(file="./logo.png")
canvas.create_image(100,100, image=img)
canvas.grid(column=1, row=0)

# website
website_text = Label(text="Website: ")
website_text.grid(row=1, column=0, sticky="w")

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

# EMAIL/USERNAME

username_text= Label(text="Email/Username: ")
username_text.grid( row=2, column=0, sticky="w")

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

# PASSWORD
password_text = Label(text="Password: ")
password_text.grid(row=3, column=0, sticky="w")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1 , sticky="ew")

password_btn = Button(text="Generate Password")
password_btn.grid(row=3, column=2)

# SAVE PASS
save_btn = Button(text="Save Password", width=36)
save_btn.grid(row=4, column=1, columnspan=2, sticky="ew" )


window.mainloop()
