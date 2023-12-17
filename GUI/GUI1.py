import tkinter as tk
from tkinter import ttk

def button_func():
    print('the button is working')

def exerisebutton_func1():
    print('hello')


#Create a Windows
windows= tk.Tk()
windows.title('windows and widgets')
windows.geometry("800x500")

#ttk label
label=ttk.Label(master=windows, text="this is a test run")
label.pack()

#create widgets
text=tk.Text(master=windows)
text.pack()

#creating the entry
entry=ttk.Entry(master=windows)
entry.pack()

#creating exerise label    
exeriselabel_1=ttk.Label(master=windows,text='exeriselabel')
exeriselabel_1.pack()

#creating exerise button  
exerisebutton_1=ttk.Button(master=windows,text='exerise_1',command=exerisebutton_func1)
exerisebutton_1.pack()

#creating the button
button=ttk.Button(master=windows, text='BUTTON',command=button_func)
button.pack()


#run
windows.mainloop()
#40:44