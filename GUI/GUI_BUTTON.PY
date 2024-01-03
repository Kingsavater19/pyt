import tkinter as tk
from tkinter import ttk

#creating the windows
windows= tk.Tk()
windows.title('buttons')


def button_func():
    print('this is a button')
    print(radio_var.get())



#creating a stringvar
String_Var=tk.StringVar(value='stringvar button')


#creating the button
button=ttk.Button(master=windows,text='button', textvariable=String_Var, command=button_func)
button.pack()

#check button
check_var=tk.IntVar()
check=ttk.Checkbutton(windows ,text='checkbutton1',command=lambda:print(check_var.get()) ,variable=check_var,onvalue=100,offvalue=0)
check.pack()

#radiobutton
radio_var=tk.StringVar()
radio=ttk.Radiobutton(windows,text='Radiobutton',value=0,variable=radio_var, command=lambda:print(radio_var))
radio.pack()
radio1=ttk.Radiobutton(windows,text='Radiobutton1',value=1,variable=radio_var,command=lambda:print(radio_var))
radio1.pack()





#run
windows.mainloop()