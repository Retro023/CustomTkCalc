
#|-----------Imports-----------|
import customtkinter as ctk
from tkinter import *

#|------Default settings----|
ctk.set_default_color_theme('Themes/breeze.json')
ctk.set_appearance_mode('light')


#|-----Change mode-------|
def toggle_switch(textbox):
    if mode_var.get() == "on":
        ctk.set_appearance_mode('dark')
        textbox.delete(0.0,END)
        textbox.insert(END, "Dark mode")
    else:
        ctk.set_appearance_mode('light')
        textbox.delete(0.0,END)
        textbox.insert(END, "Light mode")



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
        expression = expression.replace("x", "*",).replace("÷", "/")
        result = str(eval(expression))
        entry.delete(0,END)
        entry.insert(END,result)
        expression = result
    except ZeroDivisionError:
        entry.delete(0,END)
        entry.insert(END, "ERROR: cant divide by zero")
        expression = ""
    except ValueError:
        entry.delete(0,END)
        entry.insert(END,"ERROR: invalid number")
        expression = ""
    except TypeError:
        entry.delete(0,END)
        entry.insert(END,"ERROR: mismatched data types")
        expression = ""
    except OverflowError:
        entry.delete(0,END)
        entry.insert(0,"ERROR: number to large to compute")
        expression = ""
    except NameError:
        entry.delete(0,END)
        entry.insert(0, "ERROR: undefined variable ")
        expression = ""
    except ArithmeticError:
        entry.delete(0,END)
        entry.insert(0, "Error: Incorrect Arithmetic")
        expression = ""
    except AttributeError:
        entry.delete(0,END)
        entry.insert(0,"ERROR: attribute")
        expression = ""
    except SyntaxError:
        entry.delete(0,END)
        entry.insert(0,"ERROR: syntax error")
        expression = ""


#|-----Clear entry field-----|
def clear_field(entry):
    global expression
    expression = ""
    entry.delete(0,END)

#|-------Main------|

def main():
    global mode_var
    root = ctk.CTk()
    root.title("Calculator")
    root.geometry("500x700")
    
    entry = ctk.CTkEntry(root, width=500, height=95, font=('Arial', 30))
    entry.grid(row=0, column=0, columnspan=4, pady=20)
    textbox =ctk.CTkTextbox(root, width=160, height=10)
    textbox.grid(row=10, column=2, columnspan=4, pady=10)
    mode_var = ctk.StringVar(value="off")
    mode = ctk.CTkSwitch(master=root, text="Dark Mode",variable=mode_var, onvalue="on", offvalue="off"  ,command=lambda:toggle_switch(textbox))
    mode.grid(row=10, column=1, columnspan=4, pady=10, sticky="wn")

    Button_frame = ctk.CTkFrame(root)
    button_labels =  [
        ("7", "8", "9", "÷"),
        ("4", "5", "6", "x"),
        ("1", "2", "3", "-"),
        ("C", "0", "=", "+")
    ]
    basic_funcs = {
        '=': lambda e=entry: calculate(e),
        'c': lambda e=entry: clear_field(e)
    }
    
    for i, row in enumerate(button_labels):
        for x, button in enumerate(row):
            bttn = ctk.CTkButton(
                root, text=button, width=20, height=20, command=lambda value=button, 
                    e=entry: add_expression(value,e) if value != '=' and value != 'C' else (calculate(e) if value == '=' else clear_field(e)))
            bttn.grid(row=i+3, column=x, pady=5, padx=5, sticky='nsew')
    
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(3, 7):
        root.grid_rowconfigure(i, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
