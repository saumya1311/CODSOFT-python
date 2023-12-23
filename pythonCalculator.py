import tkinter as tk
cal=""

def addcalculation(symbol):
    global cal
    cal+=str(symbol)
    textresult.delete(1.0,'end')
    textresult.insert(1.0,cal)

def evaluatecalculation():
    global cal
    try:
        cal=str(eval(cal))
        textresult.delete(1.0,'end')
        textresult.insert(1.0,cal)
    except:
        clear()
        textresult.insert(1.0,"Error")

def clear():
    global cal
    cal=""
    textresult.delete(1.0,'end')
    
root=tk.Tk()
root.geometry("410x310")

textresult=tk.Text(root,height=2,width=21,font=("Algerian",24))
textresult.grid(columnspan=6)

btn1=tk.Button(root,text="1",command=lambda:addcalculation(1),width=11,font=("Algerian",14))
btn1.grid(row=2,column=1)

btn2=tk.Button(root,text="2",command=lambda:addcalculation(2),width=11,font=("Algerian",14))
btn2.grid(row=2,column=2)

btn3=tk.Button(root,text="3",command=lambda:addcalculation(3),width=11,font=("Algerian",14))
btn3.grid(row=2,column=3)

btn4=tk.Button(root,text="4",command=lambda:addcalculation(4),width=11,font=("Algerian",14))
btn4.grid(row=3,column=1)

btn5=tk.Button(root,text="5",command=lambda:addcalculation(5),width=11,font=("Algerian",14))
btn5.grid(row=3,column=2)

btn6=tk.Button(root,text="6",command=lambda:addcalculation(6),width=11,font=("Algerian",14))
btn6.grid(row=3,column=3)

btn7=tk.Button(root,text="7",command=lambda:addcalculation(7),width=11,font=("Algerian",14))
btn7.grid(row=4,column=1)

btn8=tk.Button(root,text="8",command=lambda:addcalculation(8),width=11,font=("Algerian",14))
btn8.grid(row=4,column=2)

btn9=tk.Button(root,text="9",command=lambda:addcalculation(9),width=11,font=("Algerian",14))
btn9.grid(row=4,column=3)

btn0=tk.Button(root,text="0",command=lambda:addcalculation(0),width=11,font=("Algerian",14))
btn0.grid(row=5,column=1)

btnplus=tk.Button(root,text="+",command=lambda:addcalculation('+'),width=11,font=("Algerian",14))
btnplus.grid(row=5,column=2)

btnmin=tk.Button(root,text="-",command=lambda:addcalculation('-'),width=11,font=("Algerian",14))
btnmin.grid(row=5,column=3)

btnmul=tk.Button(root,text="*",command=lambda:addcalculation('*'),width=11,font=("Algerian",14))
btnmul.grid(row=6,column=1)

btndiv=tk.Button(root,text="/",command=lambda:addcalculation('/'),width=11,font=("Algerian",14))
btndiv.grid(row=6,column=2)

btnpare1=tk.Button(root,text="(",command=lambda:addcalculation('('),width=11,font=("Algerian",14))
btnpare1.grid(row=6,column=3)

btnpare2=tk.Button(root,text=")",command=lambda:addcalculation(')'),width=11,font=("Algerian",14))
btnpare2.grid(row=7,column=1)

btnequ=tk.Button(root,text="=",command=evaluatecalculation,width=11,font=("Algerian",14))
btnequ.grid(row=7,column=2,)

btnclr=tk.Button(root,text="Clear",command=clear,width=11,font=("Algerian",14))
btnclr.grid(row=7,column=3,)

root.mainloop()
