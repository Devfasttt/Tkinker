#import tkinter
from tkinter import *
#main window
root=Tk()
#create a label widget
myLabel1=Label(root, text="hello i am a  good, really good person")#.grid(row=0, column=0)
myLabel2=Label(root, text="Who are you?")#.grid(row=3, column=7)
myLabel3=Label(root, text="                     ")#.grid(row=8, column=5)
#shoving it on the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=7)
myLabel3.grid(row=3, column=5)
#Call the main loop
root.mainloop()
