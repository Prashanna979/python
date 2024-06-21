import tkinter as tk

app=tk.Tk()
app.title('calculator')
app.geometry("400x350")

entry_font=('helvetica',20)
#result
result = tk.Entry(app,width=65,borderwidth=3,)
result.grid(pady=0,row=0,column=0,columnspan=10)


# result.place(x=40, y=100, width=180, height=60) 

# #get value from button
# def button_click(number):
#     current=result.get()
#     result.delete(0,tk.END)
#     result.insert(0,str)

# def add(number):

# #numbers 0-9
# zero=tk.Button(app,text="0",padx=40,pady=20,command=lambda:button_click(0))
# one=tk.Button(app,text="1",padx=40,pady=20,command=lambda:button_click(1))
# two=tk.Button(app,text="2",padx=40,pady=20,command=lambda:button_click(2))
# three=tk.Button(app,text="3",padx=40,pady=20,command=lambda:button_click(3))
# four=tk.Button(app,text="4",padx=40,pady=20,command=lambda:button_click(4))
# five=tk.Button(app,text="5",padx=40,pady=20,command=lambda:button_click(5))
# six=tk.Button(app,text="6",padx=40,pady=20,command=lambda:button_click(6))
# seven=tk.Button(app,text="7",padx=40,pady=20)
# eight=tk.Button(app,text="8",padx=40,pady=20)
# nine=tk.Button(app,text="9",padx=40,pady=20)
# dot=tk.Button(app,text="9",padx=40,pady=20)
# equal=tk.Button(app,text=".",padx=40,pady=20)
# add=tk.Button(app,text="+",padx=40,pady=20)
# subtract=tk.Button(app,text="-",padx=40,pady=20)
# multiply=tk.Button(app,text="*",padx=40,pady=20)
# divide=tk.Button(app,text="/",padx=40,pady=20)

# zero.grid(row=4,column=1)
# dot.grid(row=4,column=0)
# equal.grid(row=4,column=2)
# add.grid(row=4,column=3)
# one.grid(row=3,column=0)
# two.grid(row=3,column=1)
# three.grid(row=3,column=2)
# subtract.grid(row=3,column=3)
# four.grid(row=2,column=0)
# five.grid(row=2,column=1)
# six.grid(row=2,column=2)
# multiply.grid(row=2,column=3)
# seven.grid(row=1,column=0)
# eight.grid(row=1,column=1)
# nine.grid(row=1,column=2)
# divide.grid(row=1,column=3)


def button_click(number):
    current = result.get()
    result.delete(0, tk.END)
    result.insert(0, str(current) + str(number))

def clear():
    result.delete(0, tk.END)

def add_number_button(number):
    return tk.Button(app, text=number, padx=40, pady=20,command=lambda: button_click(number))


def equal():
    current = result.get()
    total = eval(current)
    result.delete(0, tk.END)
    result.insert(0, total)
zero = tk.Button(app, text="0", padx=40, pady=20,command=lambda: button_click(0))
one = tk.Button(app, text="1", padx=40, pady=20,command=lambda: button_click(1))
two = tk.Button(app, text="2", padx=40, pady=20,command=lambda: button_click(2))
three = tk.Button(app, text="3", padx=40, pady=20,command=lambda: button_click(3))
four = tk.Button(app, text="4", padx=40, pady=20,command=lambda: button_click(4))
five = tk.Button(app, text="5", padx=40, pady=20,command=lambda: button_click(5))
six = tk.Button(app, text="6", padx=40, pady=20,command=lambda: button_click(6))
seven = tk.Button(app, text="7", padx=40, pady=20,command=lambda: button_click(7))
eight = tk.Button(app, text="8", padx=40, pady=20,command=lambda: button_click(8))
nine = tk.Button(app, text="9", padx=40, pady=20,command=lambda: button_click(9))

dot = tk.Button(app, text=".", padx=40, pady=20,command=lambda: button_click("."))
equal = tk.Button(app, text="=", padx=40, pady=20,command=equal)
plush = tk.Button(app, text="+", padx=40, pady=20,command=lambda: button_click("+"))
minus = tk.Button(app, text="-", padx=40, pady=20,command=lambda: button_click("-"))
multiply = tk.Button(app, text="*", padx=40, pady=20,command=lambda: button_click("*"))
divide = tk.Button(app, text="/", padx=40, pady=20,command=lambda: button_click("/"))
clear = tk.Button(app, text="C", padx=40, pady=20, command=clear)

zero.grid(row=4, column=0)
one.grid(row=3, column=0)
two.grid(row=3, column=1)
three.grid(row=3, column=2)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
seven.grid(row=1, column=0)
eight.grid(row=1, column=1)
nine.grid(row=1, column=2)

dot.grid(row=4, column=1)
equal.grid(row=4, column=2)
plush.grid(row=1, column=3)
minus.grid(row=2, column=3)
multiply.grid(row=3, column=3)
divide.grid(row=4, column=3)
clear.grid(row=5, column=0, columnspan=4)

app.mainloop()