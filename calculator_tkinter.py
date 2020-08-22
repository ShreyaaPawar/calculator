"""
Calculator using tkinter
"""


import tkinter
from tkinter import *      #GUI import
from tkinter import messagebox       #for showing msgs import messag

#initialisation of variables
"""
val is the data shown in label
A is the first operand present in left side of calculation and initialised as 0 to rease garbage value
operator is for +,*,-,/ signs 
"""
val = ""
A = 0
operator = ""

#functions for each buttons to perform its specific functions when pressed
def btn1_is_clicked():
    global val
    val = val + "1"   #concanate the left side operand with using 1 for eg.12=1
    data.set(val)     #display data on label

def btn2_is_clicked():
    global val
    val = val + "2"
    data.set(val)

def btn3_is_clicked():
    global val
    val = val + "3"
    data.set(val)

def btn4_is_clicked():
    global val
    val = val + "4"
    data.set(val)

def btn5_is_clicked():
    global val
    val = val + "5"
    data.set(val)

def btn6_is_clicked():
    global val
    val = val + "6"
    data.set(val)

def btn7_is_clicked():
    global val
    val = val + "7"
    data.set(val)

def btn8_is_clicked():
    global val
    val = val + "8"
    data.set(val)

def btn9_is_clicked():
    global val
    val = val + "9"
    data.set(val)

def btn10_is_clicked():
    global val
    val = val + "0"
    data.set(val)

def btnplus_is_clicked():
    global val
    global A
    global operator
    A = int(val)       #val type is converted since by default python takes it as string
    operator = "+"     #initialised operator as +
    val = val + "+"    #concanate
    data.set(val)

def btnminus_is_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btnmul_is_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btndiv_is_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btnC_is_clicked():
    global val
    global A
    global operator
    val = ""          #clear the data shown on label
    A = 0
    operator = ""
    data.set(val)

def result():
    global val
    global A
    global operator
    val2 = val

    if operator == "+":
        C = int((val2.split("+")[1]))   #val consist of the data displayed on label so its is been splited and second operand is stored in C
        res = A + C                     #add operation
        data.set(res)                   #result displayed
        val = str(res)                  #res is changed in string attribute if in case we want to use it again

    elif operator == "-":
        C = int((val2.split("-")[1]))
        res = A - C
        data.set(res)
        val = str(res)

    elif operator == "*":
        C = int((val2.split("*")[1]))
        res = A * C
        data.set(res)
        val = str(res)

    elif operator == "/":
        C = int((val2.split("/")[1]))
        if C == 0:
            messagebox.showerror("Error" , "Divide by zero is not allowed")   #error is shown and text are erased from variables
            A = ""
            val = ""

        else:
            res = int(A / C)  #provides result in int format
            data.set(res)
            val = str(res)


root = Tk()
root.geometry("250x400+300+300")
root.resizable(0 , 0)
root.title("Calculator")

data = StringVar()

"""
label attribute is initialised for providing the result
"""
lbl = Label(
    root,
    text = "label",
    anchor = SE,
    textvariable = data,
    bg = "#FFFFFF",
    fg = "#000000",
)
lbl.pack(expand = True, fill = BOTH)

"""
Frame is initialised for buttons of numbers and signs
"""
btnrow1 = Frame(root, bg='#000000')
btnrow1.pack(expand = True,fill = BOTH)

btnrow2 = Frame(root)
btnrow2.pack(expand = True , fill = BOTH)

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = BOTH)

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = BOTH)

"""
numbers and operators buttons are been initialised
"""
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Arial" , 22),
    relief = GROOVE,   #no borders around the buttons
    border = 0,
    command = btn1_is_clicked,  #when clicked mentioned functions to be executed
)
btn1.pack(side = LEFT , expand = True , fill = BOTH)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btn2_is_clicked,
)
btn2.pack(side = LEFT, expand = True, fill = BOTH)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btn3_is_clicked,
)
btn3.pack(side = LEFT, expand = True, fill = BOTH )

btn4 = Button(
    btnrow1,
    text = "+",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btnplus_is_clicked,

)
btn4.pack(side = LEFT , expand = True , fill = BOTH)

btn5 = Button(
    btnrow2,
    text = "4",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btn4_is_clicked,
)
btn5.pack(side = LEFT, expand = True, fill = BOTH)

btn6 = Button(
    btnrow2,
    text = "5",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btn5_is_clicked,
)
btn6.pack(side = LEFT, expand = True, fill = BOTH)

btn7 = Button(
    btnrow2,
    text = "6",
    font = ("Arial",22),
    relief = GROOVE,
    border = 0,
    command = btn6_is_clicked,
)
btn7.pack(side = LEFT, expand = True , fill = BOTH)

btn8 = Button(
    btnrow2,
    text = "-",
    font = ("Arial",22),
    relief = GROOVE,
    border = 0,
    command = btnminus_is_clicked,
)
btn8.pack(side = LEFT, expand = True, fill = BOTH)

btn9 = Button(
    btnrow3,
    text = "7",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btn7_is_clicked,
)
btn9.pack(side = LEFT, expand = True, fill = BOTH)

btn10 = Button(
    btnrow3,
    text = "8",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btn8_is_clicked,
)
btn10.pack(side = LEFT, expand = True, fill = BOTH)

btn11 = Button(
    btnrow3,
    text = "9",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btn9_is_clicked,
)
btn11.pack(side = LEFT , expand = True, fill = BOTH)

btn12 = Button(
    btnrow3,
    text = "*",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btnmul_is_clicked,
)
btn12.pack(side = LEFT, expand = True, fill= BOTH)

btn13 = Button(
    btnrow4,
    text = "c",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btnC_is_clicked,

)
btn13.pack(side = LEFT, expand = True, fill= BOTH)

btn14 = Button(
    btnrow4,
    text = "0",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btn10_is_clicked,
)
btn14.pack(side = LEFT, expand = True, fill= BOTH)

btn15 = Button(
    btnrow4,
    text = "=",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btn15.pack(side = LEFT, expand = True, fill= BOTH)

btn16 = Button(
    btnrow4,
    text = "/",
    font = ("Arial" , 22),
    relief = GROOVE,
    border = 0,
    command = btndiv_is_clicked,
)
btn16.pack(side = LEFT, expand = True, fill= BOTH)

root.mainloop()  #for opening window it's required