import tkinter as tk
from tkinter import scrolledtext

# main window
root = tk.Tk()
root.title("Python Calculator with History")
root.geometry("350x450")
root.resizable(False, False)

expression = ""

# display
display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
display.pack(fill="both", padx=10, pady=10)

# history box
history = scrolledtext.ScrolledText(root, height=8, font=("Arial", 10))
history.pack(fill="both", padx=10, pady=5)

def press(num):
    global expression
    expression = expression + str(num)
    display.delete(0, tk.END)
    display.insert(0, expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        history.insert(tk.END, expression + " = " + result + "\n")
        display.delete(0, tk.END)
        display.insert(0, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        expression = ""

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def clear_history():
    history.delete(1.0, tk.END)

# button frame
frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('=',4,2),('+',4,3)
]

for (text,row,col) in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, width=8, height=3, command=equalpress)
    else:
        btn = tk.Button(frame, text=text, width=8, height=3, command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

# control buttons
clear_btn = tk.Button(root, text="Clear", height=2, command=clear)
clear_btn.pack(fill="both", padx=10, pady=3)

clear_hist_btn = tk.Button(root, text="Clear History", height=2, command=clear_history)
clear_hist_btn.pack(fill="both", padx=10)

root.mainloop()
