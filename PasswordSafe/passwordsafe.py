from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FILE_DELIMITER = "|"


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_symbols

    shuffle(password_list)
    password = "".join(password_list)
    input_pwd.insert(0, password)
    pyperclip.copy(password)


def add_password():
    # Capture all the entered details:
    user_details = [input_website.get(), input_uname.get(), input_pwd.get()]
    field_result = validate_field()
    if field_result == 0:
        messagebox.showerror(message=f"Please don't leave any fields empty!\n")
    else:
        is_ok = messagebox.askokcancel(
            message=f"These are the details entered: \nEmail: {input_uname.get()}\nPassword: {input_pwd.get()}\n\nAre the details okay to save?\n")
        if is_ok:
            write_to_pwdfile(user_details)
            clear_field(input_website)
            clear_field(input_pwd)


def write_to_pwdfile(details):
    with open("passfile.txt", 'a') as logfile:
        for item in details[:-1]:
            logfile.write(item)
            logfile.write(FILE_DELIMITER)
        logfile.write(details[-1])
        logfile.write('\n')


def clear_field(field):
    field.delete(0, END)


def validate_field():
    if len(input_website.get()) == 0 or len(input_pwd.get()) == 0 or len(input_uname.get()) == 0:
        return 0
    else:
        return 1


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:", font=("Ariel", 14))
label_website.grid(column=0, row=1)
label_uname = Label(text="Email/Username:", font=("Ariel", 14))
label_uname.grid(column=0, row=2)
label_pwd = Label(text="Password:", font=("Ariel", 14))
label_pwd.grid(column=0, row=3)

# Entry
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()
input_uname = Entry(width=35)
input_uname.grid(column=1, row=2, columnspan=2)
input_uname.insert(0, "test@example.com")
input_pwd = Entry(width=20)
input_pwd.grid(column=1, row=3)

# Button
btn_gen_pass = Button(text="Generate Password", width=11, command=generate_password)
btn_gen_pass.grid(column=2, row=3)
btn_add = Button(text="Add", width=34, command=add_password)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
