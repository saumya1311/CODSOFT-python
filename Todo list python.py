import tkinter as tk
from tkinter import ttk
import mysql.connector
import sys

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="saumya123")
cursor=mydb.cursor()
cursor.execute("create database if not exists todolist")
cursor.execute("use todolist")

#DATABASE WORK
def add():
	mydb=mysql.connector.connect(host="localhost",user="root",password="saumya123")
	cursor=mydb.cursor()
	cursor.execute("create database if not exists todolist")
	cursor.execute("use todolist")
	cursor.execute("insert into list values(%s,%s)",(S_No.get(),Work_to_do.get()))
	mydb.commit()
	show()
	clear()
	mydb.close()
def show():
	mydb=mysql.connector.connect(host="localhost",user="root",password="saumya123")
	cursor=mydb.cursor()
	cursor.execute("create database if not exists todolist")
	cursor.execute("use todolist")
	cursor.execute("select * from list")
	rec=cursor.fetchall()
	if len(rec)!=0:
		list1.delete(*list1.get_children())
		for rows in rec:
			list1.insert('',tk.END,values=rows)
		mydb.commit()
	mydb.close()	
def clear():
	S_No.set("")
	Work_to_do.set("")	
def cur(self):
	cur_row=list1.focus()
	cntnt=list1.item(cur_row)
	rows=cntnt['values']
	S_No.set(rows[0])
	Work_to_do.set(rows[1])
def update():
	mydb=mysql.connector.connect(host="localhost",user="root",password="saumya123")
	cursor=mydb.cursor()
	cursor.execute("create database if not exists todolist")
	cursor.execute("use todolist")
	cursor.execute("update list set S_No_='%s',Work_to_do='%s' where S_No_='%s'"%(S_No.get(),Work_to_do.get(),S_No.get()))
	mydb.commit()
	mydb.close()
	show()
	clear()
def delete():
	mydb=mysql.connector.connect(host="localhost",user="root",password="saumya123")
	cursor=mydb.cursor()
	cursor.execute("create database if not exists todolist")
	cursor.execute("use todolist")
	cursor.execute("delete from list where S_No_='%s'"%(S_No.get()))
	mydb.commit()
	show()
	clear()
	mydb.close()

#framework
cb=tk.Tk()
cb.geometry("700x600+0+0")
cb.title("To Do List")

cb.config(bg="#427D9D")
title_lbl=tk.Label(cb,text="To Do List",font=("Agency FB",30),border=12,relief=tk.GROOVE,bg="#427D9D",foreground="white")
title_lbl.pack(side=tk.TOP,fill=tk.X)

data_frm=tk.Frame(cb,border=9,bg="#9BBEC8",relief=tk.GROOVE)
data_frm.place(x=4,y=79,width=690,height=380)
mnfrm=tk.Frame(data_frm,bd=11,relief=tk.GROOVE)
mnfrm.pack(fill=tk.BOTH,expand=True)
scrly=tk.Scrollbar(mnfrm,orient=tk.VERTICAL)
scrlx=tk.Scrollbar(mnfrm,orient=tk.HORIZONTAL)
list1=ttk.Treeview(mnfrm,columns=("S_No","Work_to_do"),yscrollcommand=scrly.set,xscrollcommand=scrlx.set)
scrly.config(command=list1.yview)
scrlx.config(command=list1.xview)
scrly.pack(side=tk.RIGHT,fill=tk.Y)
scrlx.pack(side=tk.BOTTOM,fill=tk.X)
list1.heading("S_No",text="S.No.")
list1.heading("Work_to_do",text="Work To Do")
list1["show"]="headings"
list1.column("S_No",width=100)
list1.column("Work_to_do",width=500)
list1.pack(fill=tk.BOTH,expand=True)
list1.bind("<ButtonRelease-1>",cur)

bfrm=tk.LabelFrame(cb,bg="#9BBEC8",fg="white",border=9,relief=tk.GROOVE)
bfrm.place(x=5,y=460,width=690,height=130)
S_No=tk.StringVar()
Work_to_do=tk.StringVar()
sno_lbl=tk.Label(bfrm,text="Serial No. :",font=("Agency FB",25),bg="#9BBEC8")
sno_lbl.grid(row=1,column=0,padx=2,pady=2)
sno_ent=tk.Entry(bfrm,bd=4,font=("Arial",15),width=10,textvariable=S_No)
sno_ent.grid(row=1,column=1,pady=2)
note_lbl=tk.Label(bfrm,text="Work To Do :",font=("Agency FB",25),bg="#9BBEC8")
note_lbl.grid(row=1,column=2,padx=2,pady=2)
note_ent=tk.Entry(bfrm,bd=4,font=("Arial",15),width=23,textvariable=Work_to_do)
note_ent.grid(row=1,column=3,padx=2,pady=2)
adbut=tk.Button(bfrm,bg="#427D9D",foreground="white",text="Add",bd=6,width=15,height=1,font=("Agency FB",14),command=add)
adbut.grid(row=2,column=0,padx=8,pady=4)
dlbut=tk.Button(bfrm,bg="#427D9D",foreground="white",text="Delete",command=delete,bd=6,width=15,height=1,font=("Agency FB",14))
dlbut.grid(row=2,column=1,padx=0,pady=0)
clbut=tk.Button(bfrm,command=clear,bg="#427D9D",foreground="white",text="Clear",bd=6,width=35,height=1,font=("Agency FB",14))
clbut.grid(row=2,column=3,padx=0,pady=0)
upbut=tk.Button(bfrm,bg="#427D9D",foreground="white",command=update,text="Update",bd=6,width=15,height=1,font=("Agency FB",14))
upbut.grid(row=2,column=2,padx=2,pady=0)
list1.bind("<ButtonRelease-1>",cur)

show()
cb.mainloop()





