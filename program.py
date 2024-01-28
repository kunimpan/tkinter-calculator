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

#dipsplay Frame
display=Entry(displayFrame, width=30, font=displayFont, bg="white", border=5, justify=RIGHT) # justify is curser position. 
display.pack(padx=5, pady=5)

#clear & quit
btnClear=Button(buttonFrame, text="Clear", font=btnFont)
btnQuit=Button(buttonFrame, text="Quit", font=btnFont, command=root.destroy)
btnClear.grid(row=0, column=0, columnspan=2, ipadx=35, sticky="WE") # columnspan is taking up space.
btnQuit.grid(row=0, column=2, columnspan=2, ipadx=35, sticky="WE")

#opeator button
btnInverse=Button(buttonFrame, text="1/x", font=btnFont, bg=color)
btnSquare=Button(buttonFrame, text="x^2", font=btnFont, bg=color)
btnExponent=Button(buttonFrame, text="x^n", font=btnFont, bg=color)
btnDivide=Button(buttonFrame, text="/", font=btnFont, bg=color)
btnMultiply=Button(buttonFrame, text="x", font=btnFont, bg=color)
btnSubtract=Button(buttonFrame, text="1/x", font=btnFont, bg=color)
btnAdd=Button(buttonFrame, text="+", font=btnFont, bg=color)
btnEqual=Button(buttonFrame, text="=", font=btnFont, bg=color)
btnDecimal=Button(buttonFrame, text=".", font=btnFont, bg=color)
btnNegate=Button(buttonFrame, text="+/-", font=btnFont, bg=color)

#number button
btn9=Button(buttonFrame, text="9", font=btnFont, bg="black", fg="white")
btn8=Button(buttonFrame, text="8", font=btnFont, bg="black", fg="white")
btn7=Button(buttonFrame, text="7", font=btnFont, bg="black", fg="white")
btn6=Button(buttonFrame, text="6", font=btnFont, bg="black", fg="white")
btn5=Button(buttonFrame, text="5", font=btnFont, bg="black", fg="white")
btn4=Button(buttonFrame, text="4", font=btnFont, bg="black", fg="white")
btn3=Button(buttonFrame, text="3", font=btnFont, bg="black", fg="white")
btn2=Button(buttonFrame, text="2", font=btnFont, bg="black", fg="white")
btn1=Button(buttonFrame, text="1", font=btnFont, bg="black", fg="white")
btn0=Button(buttonFrame, text="0", font=btnFont, bg="black", fg="white")



root.mainloop()