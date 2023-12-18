import tkinter as tk
from tkinter import ttk

def button_func():
    #Get the content of the entry
    Entry_text=Entry.get()
    Label['text']=Entry_text
    Entry['state']='disabled'
#    print(Label.configure())

#creating the window
window=tk.Tk()
window.title('Text area')


#creating a label
Label=ttk.Label(master=window,text='Enter your info here')
Label.pack()

#creating your entry
Entry=ttk.Entry(master=window)
Entry.pack()

#creating your button
Button=ttk.Button(master=window, text='Enter',command=button_func)
Button.pack()

def rest_func():
    Label['text']='Enter your info here'
    Entry['state']='enabled'



#exrerise button
exerise_button=ttk.Button(master=window,text='exerise_button' , command=rest_func)
exerise_button.pack()
 
#runing
window.mainloop()