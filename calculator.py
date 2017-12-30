from tkinter import *
w=Tk()
w.title("Calculator")
w.resizable(0,0)

#define the functions
input_value=StringVar()
expression=""
def click(n):
    global expression
    expression+=str(n)
    input_value.set(expression)
def calculate():
    global expression
    input_value.set(eval(expression))
def clear():
    global expression
    expression=""
    input_value.set(expression)

#design the components
entry=Entry(w,bg="yellow",font=("arial",20,"bold"),textvariable=input_value,justify="right")
btn1=Button(w,text="1",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click(1))
btn2=Button(w,text="2",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click(2))
btn3=Button(w,text="3",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click(3))
btn4=Button(w,text="4",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click(4))
btn5=Button(w,text="5",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click(5))
btn6=Button(w,text="6",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click(6))
btn7=Button(w,text="7",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click(7))
btn8=Button(w,text="8",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click(8))
btn9=Button(w,text="9",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click(9))
btn0=Button(w,text="0",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click(0))
btnequals=Button(w,text="=",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=calculate)
btnclear=Button(w,text="C",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=clear)
btnplus=Button(w,text="+",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click("+"))
btnminus=Button(w,text="-",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click("-"))
btnmul=Button(w,text="*",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click("*"))
btndiv=Button(w,text="/",font=("arial",20,"bold"),padx=16,pady=16,relief="groove",bd=10,command=lambda:click("/"))

#palcing the components
entry.grid(row=1,column=1,columnspan=4)

btn1.grid(row=2,column=1)
btn2.grid(row=2,column=2)
btn3.grid(row=2,column=3)
btn4.grid(row=2,column=4)

btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btn7.grid(row=3,column=3)
btn8.grid(row=3,column=4)

btn9.grid(row=4,column=1)
btn0.grid(row=4,column=2)
btnequals.grid(row=4,column=3)
btnclear.grid(row=4,column=4)

btnplus.grid(row=5,column=1)
btnminus.grid(row=5,column=2)
btnmul.grid(row=5,column=3)
btndiv.grid(row=5,column=4)



w.mainloop()
