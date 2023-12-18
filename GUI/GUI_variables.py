import tkinter as tk
from tkinter import ttk

#creating a window
Windows=tk.Tk()
Windows.title('variables')
Windows.geometry('500x500')

#Creating tkinter varable
string_var=tk.StringVar(value="")

#button function
def button_func():
    print(string_var.get())


#creting label
label=ttk.Label(master=Windows,text='label',textvariable=string_var)
label.pack()

#creating Entry
entry=ttk.Entry(master=Windows,textvariable=string_var)
entry.pack()

#creating button
button=ttk.Button(master=Windows,text='Enter',command=button_func)
button.pack()



#RUNING
Windows.mainloop()