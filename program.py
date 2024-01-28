from tkinter import *

# design root windows
root=Tk()
root.title("Calculator")
root.iconbitmap("icon/cal-logo.ico")
root.geometry("300x400")
root.resizable(0, 0)

def showNumber(number):
    display.insert(END, number) #Let the numbers follow each other.

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
btnSubtract=Button(buttonFrame, text="-", font=btnFont, bg=color)
btnAdd=Button(buttonFrame, text="+", font=btnFont, bg=color)
btnEqual=Button(buttonFrame, text="=", font=btnFont, bg=color)
btnDecimal=Button(buttonFrame, text=".", font=btnFont, bg=color)
btnNegate=Button(buttonFrame, text="+/-", font=btnFont, bg=color)

#number button
btn9=Button(buttonFrame, text="9", font=btnFont, bg="black", fg="white", command=lambda:showNumber(9))
btn8=Button(buttonFrame, text="8", font=btnFont, bg="black", fg="white", command=lambda:showNumber(8))
btn7=Button(buttonFrame, text="7", font=btnFont, bg="black", fg="white", command=lambda:showNumber(7))
btn6=Button(buttonFrame, text="6", font=btnFont, bg="black", fg="white", command=lambda:showNumber(6))
btn5=Button(buttonFrame, text="5", font=btnFont, bg="black", fg="white", command=lambda:showNumber(5))
btn4=Button(buttonFrame, text="4", font=btnFont, bg="black", fg="white", command=lambda:showNumber(4))
btn3=Button(buttonFrame, text="3", font=btnFont, bg="black", fg="white", command=lambda:showNumber(3))
btn2=Button(buttonFrame, text="2", font=btnFont, bg="black", fg="white", command=lambda:showNumber(2))
btn1=Button(buttonFrame, text="1", font=btnFont, bg="black", fg="white", command=lambda:showNumber(1))
btn0=Button(buttonFrame, text="0", font=btnFont, bg="black", fg="white", command=lambda:showNumber(0))

#row1
btnInverse.grid(row=1, column=0, pady=1, ipadx=10, sticky="WE")
btnSquare.grid(row=1, column=1, pady=1, ipadx=10, sticky="WE")
btnExponent.grid(row=1, column=2, pady=1, ipadx=10, sticky="WE")
btnDivide.grid(row=1, column=3, pady=1, ipadx=10, sticky="WE")

#row2
btn7.grid(row=2, column=0, pady=1, ipadx=10, sticky="WE")
btn8.grid(row=2, column=1, pady=1, ipadx=10, sticky="WE")
btn9.grid(row=2, column=2, pady=1, ipadx=10, sticky="WE")
btnMultiply.grid(row=2, column=3, pady=1, ipadx=10, sticky="WE")

#row3
btn4.grid(row=3, column=0, pady=1, ipadx=10, sticky="WE")
btn5.grid(row=3, column=1, pady=1, ipadx=10, sticky="WE")
btn6.grid(row=3, column=2, pady=1, ipadx=10, sticky="WE")
btnSubtract.grid(row=3, column=3, pady=1, ipadx=10, sticky="WE")

#row4
btn1.grid(row=4, column=0, pady=1, ipadx=10, sticky="WE")
btn2.grid(row=4, column=1, pady=1, ipadx=10, sticky="WE")
btn3.grid(row=4, column=2, pady=1, ipadx=10, sticky="WE")
btnAdd.grid(row=4, column=3, pady=1, ipadx=10, sticky="WE")

#row5
btnNegate.grid(row=5, column=0, pady=1, ipadx=10, sticky="WE")
btn0.grid(row=5, column=1, pady=1, ipadx=10, sticky="WE")
btnDecimal.grid(row=5, column=2, pady=1, ipadx=10, sticky="WE")
btnEqual.grid(row=5, column=3, pady=1, ipadx=10, sticky="WE")

root.mainloop()