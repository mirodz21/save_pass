from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    pw_letter = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    pw_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pw_letter + pw_symbol + pw_number

    shuffle(password_list)

    pw = "".join(password_list)
    password_entry.insert(0,pw)
    pyperclip.copy(pw)

    print(f"Your password is: {pw}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_details():
    website = website_entry.get()
    user = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        is_okay = messagebox.askokcancel("Save details?", f"save the following details? \nWebsite: {website}\nUsername: {user}\nPassword: {password}")
        if is_okay:
            with open("data.txt","a") as f:
                f.write(str(f"\n{website} : {user} : {password}"))
                messagebox.showinfo("Success", "Details saved")

                website_entry.delete(0, "end")
                username_entry.delete(0, "end")
                password_entry.delete(0, "end")


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
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

# EMAIL/USERNAME

username_text= Label(text="Email/Username: ")
username_text.grid( row=2, column=0, sticky="w")

username_entry = Entry(width=35, )
username_entry.insert(0,"youremail@mail.com")
username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

# PASSWORD
password_text = Label(text="Password: ")
password_text.grid(row=3, column=0, sticky="w")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1 , sticky="ew")

password_btn = Button(text="Generate Password", command=gen_pass)
password_btn.grid(row=3, column=2)

# SAVE PASS
save_btn = Button(text="Save Password", width=36, command=save_details)
save_btn.grid(row=4, column=1, columnspan=2, sticky="ew" )


window.mainloop()
