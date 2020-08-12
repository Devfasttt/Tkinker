#import tkinter
from tkinter import *
#main window
root=Tk()
#create a label widget
myLabel=Label(root, text="hello")
#shoving it on the screen
myLabel.pack()#pack the window according to the content on the screen.
#Call the main loop
root.mainloop()
