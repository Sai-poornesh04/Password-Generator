from tkinter import *
import string
import random
import pyperclip


def generator():
    lower_cases = string.ascii_lowercase
    upper_cases = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    combine = lower_cases+upper_cases+numbers+symbols
    password_length = int(length_Box.get())
    passwordField.insert(0, random.sample(combine, password_length))


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root = Tk()
root.config(bg='black')
Font = ('arial', 13, 'bold')

passwordLabel = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'), bg='#A9F1DF', fg='#DD2476')
passwordLabel.grid(pady=10)

lengthLabel = Label(root, text='Password Length', font=Font, bg='#A9F1DF', fg='#DD2476')
lengthLabel.grid(pady=5)

length_Box = Spinbox(root, from_=8, to=128, width=5, font=Font)
length_Box.grid(pady=5)

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.grid(pady=5)

root.mainloop()
