#|-----------Imports-----------|
import customtkinter as ctk
from tkinter import *

#|------Default settings----|
ctk.set_default_color_theme('Themes/breeze.json')
ctk.set_appearance_mode('dark')
mode = 'dark'


#|-----Change mode-------|
def change_mode(textbox, choice):
    global mode
    mode = choice.lower()
    
    if mode == 'light':
        ctk.set_appearance_mode('light')
        textbox.delete(0.0, END)
        textbox.insert(END, "Light mode *ON*")
    elif mode == 'dark':
        ctk.set_appearance_mode('dark')
        textbox.delete(0.0, END)
        textbox.insert(END, "Dark mode *ON*")
    elif mode == 'system':
        ctk.set_appearance_mode('system')
        textbox.delete(0.0, END)
        textbox.insert(END, "Now using system mode")




expression = ''
#|---------Update entry field------|
def add_expression(value, entry):
    global expression
    expression += str(value)
    entry.delete(0, END)
    entry.insert(END, expression)




#|------Eval expression-----|
def calculate(entry):
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0,END)
        entry.instert(END,result)
        expression = result
    except:
        entry.delete(0,END)
        entry(END, "Error!")
        expression = ""

#|-----Clear entry field-----|
def clear_field(entry):
    global expression
    expression = ""
    entry.delete(0,END)




#|-------Main------|

def main():
    root = ctk.CTk()
    root.title("Calculator")
    root.geometry("500x700")
    
    entry = ctk.CTkEntry(root, width=300, height=50, font=('Arial', 30))
    entry.pack(pady=20)    
    textbox =ctk.CTkTextbox(root, width=500, height=500)
    textbox.pack(pady=20)
    modeMenu = ctk.CTkOptionMenu(root, values=["light","dark","system"],command=lambda choice: change_mode(textbox, choice))
    modeMenu.pack(pady=20)

    root.mainloop()

main()