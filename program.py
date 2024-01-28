from tkinter import *

# design root windows
root=Tk()
root.title("Calculator")
root.iconbitmap("icon/cal-logo.ico")
root.geometry("300x400")
root.resizable(0, 0)

#settings
color="orange"
displayFont=("Arail", 35)
btnFont=("Arail", 19)


#design frame
displayFrame=LabelFrame(root)
buttonFrame=LabelFrame(root)

displayFrame.pack(padx=2, pady=5)
buttonFrame.pack(pady=2)

root.mainloop()