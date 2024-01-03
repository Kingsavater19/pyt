import tkinter as tk
from tkinter import ttk

def function():
    print(string_var.get())
    string_var.set("button pressed")

def func_test():
    print()
    


#creating windows
window= tk.Tk()
window.title("test run")
#tkinter variable
string_var=tk.StringVar()
string_var1=tk.StringVar(value='test')

#creating label
Label=ttk.Label(master=window,text='label', textvariable=string_var)
Label.pack()



#creating entry
entry=ttk.Entry(master=window,textvariable=string_var)
entry.pack()





#creating button 
button=ttk.Button(master=window,text='Press Me',command=function)
button.pack()

#creating label2
Label=ttk.Label(master=window,text='label', textvariable=string_var1)
Label.pack()

#creating entry2
entry=ttk.Entry(master=window,textvariable=string_var1)
entry.pack()

#creating entry3
entry=ttk.Entry(master=window,textvariable=string_var1)
entry.pack()

#creating button2 
button=ttk.Button(master=window,text='Press Me',command=func_test)
button.pack()




window.mainloop()