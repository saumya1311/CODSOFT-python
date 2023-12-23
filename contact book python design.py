import tkinter as tk
from tkinter import ttk
import mysql.connector
import sys

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="saumya123")

cursor=mydb.cursor()
cursor.execute("create database if not exists ContactBook")
cursor.execute("use ContactBook")

#Databasework
def add():
	mydb=mysql.connector.connect(host="localhost",user="root",password="saumya123")
	cursor=mydb.cursor()
	cursor.execute("create database if not exists ContactBook")
	cursor.execute("use ContactBook")
	cursor.execute("insert into contctlist values(%s,%s,%s,%s,%s)",(Name.get(),Phone_Number.get(),Email.get(),Address.get(),Note.get()))
	mydb.commit()
	show()
	clear()
	mydb.close()
    
def show():
	mydb=mysql.connector.connect(host="localhost",user="root",password="saumya123")
	cursor=mydb.cursor()
	cursor.execute("create database if not exists ContactBook")
	cursor.execute("use ContactBook")
	cursor.execute("select * from contctlist")
	rec=cursor.fetchall()
	if len(rec)!=0:
		book.delete(*book.get_children())
		for rows in rec:
			book.insert('',tk.END,values=rows)
		mydb.commit()
	mydb.close()

def clear():
	Name.set("")
	Phone_Number.set("")
	Email.set("")
	Address.set("")
	Note.set("")

def cur(self):
	cur_row=book.focus()
	cntnt=book.item(cur_row)
	rows=cntnt['values']
	Name.set(rows[0])
	Phone_Number.set(rows[1])
	Email.set(rows[2])
	Address.set(rows[3])
	Note.set(rows[4])

def update():
	mydb=mysql.connector.connect(host="localhost",user="root",password="saumya123")
	cursor=mydb.cursor()
	cursor.execute("create database if not exists ContactBook")
	cursor.execute("use ContactBook")
	cursor.execute("update contctlist set Name='%s',Phone_Number='%s',Email='%s',Address='%s',Note='%s' where Name='%s'"%(Name.get(),Phone_Number.get(),Email.get(),Address.get(),Note.get(),Name.get()))
	mydb.commit()
	mydb.close()
	show()
	clear()

def delete():
	mydb=mysql.connector.connect(host="localhost",user="root",password="saumya123")
	cursor=mydb.cursor()
	cursor.execute("create database if not exists ContactBook")
	cursor.execute("use ContactBook")
	cursor.execute("delete from contctlist where Name='%s'"%(Name.get()))
	mydb.commit()
	show()
	clear()
	mydb.close()

def sech():
	mydb=mysql.connector.connect(host="localhost",user="root",password="saumya123")
	cursor=mydb.cursor()
	cursor.execute("create database if not exists ContactBook")
	cursor.execute("use ContactBook")
	cursor.execute("select * from contctlist where "+str(sechboxv.get())+" LIKE '%"+str(sev.get())+"%'")
	rec=cursor.fetchall()
	if len(rec)!=0:
		book.delete(*book.get_children())
		for rows in rec:
			book.insert('',tk.END,values=rows)
	mydb.commit()
	clear()
	mydb.close()



#tkinter_Designing
cb=tk.Tk()
cb.geometry("1400x700+0+0")
cb.title("Contact Book")

cb.config(bg="#BBDEFB")

title_lbl=tk.Label(cb,text="Contact Book",font=("Impact",30,"bold"),border=15,relief=tk.GROOVE,bg="#7986CB",foreground="black")
title_lbl.pack(side=tk.TOP,fill=tk.X)

entry_frame=tk.LabelFrame(cb,text="Enter Details",font=("Times new",33),bg="#90CAF9",fg="black",border=12,relief=tk.GROOVE)
entry_frame.place(x=20,y=90,width=450,height=350)

data_frm=tk.Frame(cb,border=12,bg="#90CAF9",relief=tk.GROOVE)
data_frm.place(x=500,y=90,width=880,height=600)

bfrm=tk.LabelFrame(cb,bg="#90CAF9",fg="black",border=12,relief=tk.GROOVE)
bfrm.place(x=20,y=450,width=450,height=235)

Name=tk.StringVar()
Phone_Number=tk.StringVar()
Email=tk.StringVar()
Address=tk.StringVar()
Note=tk.StringVar()
sev=tk.StringVar()
sechboxv=tk.StringVar()

name_lbl=tk.Label(entry_frame,text="Name",font=("Agency FB",25),bg="#90CAF9")
name_lbl.grid(row=1,column=0,padx=2,pady=2)

name_ent=tk.Entry(entry_frame,bd=8,font=("Arial",15),width=24,textvariable=Name)
name_ent.grid(row=1,column=1,padx=2,pady=2)

phneno_lbl=tk.Label(entry_frame,text="Phone No",font=("Agency FB",25),bg="#90CAF9")
phneno_lbl.grid(row=2,column=0,padx=2,pady=2)

phneno_ent=tk.Entry(entry_frame,bd=8,font=("Arial",15),width=24,textvariable=Phone_Number)
phneno_ent.grid(row=2,column=1,padx=2,pady=2)

email_lbl=tk.Label(entry_frame,text="Email",font=("Agency FB",25),bg="#90CAF9")
email_lbl.grid(row=3,column=0,padx=2,pady=2)

email_ent=tk.Entry(entry_frame,bd=8,font=("Arial",15),width=24,textvariable=Email)
email_ent.grid(row=3,column=1,padx=6,pady=6)

ad_lbl=tk.Label(entry_frame,text="Address",font=("Agency FB",25),bg="#90CAF9")
ad_lbl.grid(row=4,column=0,padx=2,pady=2)

ad_ent=tk.Entry(entry_frame,width=24,bd=8,font=("Arial",15),textvariable=Address)
ad_ent.grid(row=4,column=1,padx=2,pady=2)

rl_lbl=tk.Label(entry_frame,text="Note",font=("Agency FB",25),bg="#90CAF9")
rl_lbl.grid(row=5,column=0,padx=2,pady=2)

rl_ent=tk.Entry(entry_frame,width=24,bd=8,font=("Arial",15),textvariable=Note)
rl_ent.grid(row=5,column=1,padx=2,pady=2)


adbut=tk.Button(bfrm,bg="#C5CAE9",text="Add",bd=6,width=25,height=2,font=("Agency FB",14,"bold"),command=add)
adbut.grid(row=0,column=0,padx=10,pady=16)

upbut=tk.Button(bfrm,bg="#C5CAE9",command=update,text="Update",bd=6,width=25,height=2,font=("Agency FB",14,"bold"))
upbut.grid(row=0,column=1,padx=10,pady=16)

dlbut=tk.Button(bfrm,bg="#C5CAE9",text="Delete",command=delete,bd=6,width=25,height=2,font=("Agency FB",14,"bold"))
dlbut.grid(row=2,column=0,padx=10,pady=16)

clbut=tk.Button(bfrm,command=clear,bg="#C5CAE9",text="Clear",bd=6,width=25,height=2,font=("Agency FB",14,"bold"))
clbut.grid(row=2,column=1,padx=10,pady=16)

sech_frm=tk.Frame(data_frm,bg="#BBDEFB",bd=10,relief=tk.GROOVE)
sech_frm.pack(side=tk.TOP,fill=tk.X)

sechlbl=tk.Label(sech_frm,text="Search",bg="#BBDEFB",font=("Agency FB",24))
sechlbl.grid(row=0,column=0,padx=2,pady=2)
sechbox=ttk.Combobox(sech_frm,font=("Arial",15),state="readonly",textvariable=sechboxv,width=10)
sechbox['values']=("Name","Email","Address")
sechbox.grid(row=0,column=1,padx=10,pady=2)
sechbut=tk.Button(sech_frm,bg="#C5CAE9",command=sech,text="Search",bd=6,font=("Agency FB",14),width=20)
sechbut.grid(row=0,column=3,padx=15,pady=2)
s_ent=tk.Entry(sech_frm,bd=4,font=("Arial",15),width=18,textvariable=sev,)
s_ent.grid(row=0,column=2,padx=6,pady=6)
shbut=tk.Button(sech_frm,bg="#C5CAE9",command=show,text="Show All",bd=6,font=("Agency FB",14),width=20)
shbut.grid(row=0,column=4,padx=15,pady=2)



mnfrm=tk.Frame(data_frm,bd=11,relief=tk.GROOVE)
mnfrm.pack(fill=tk.BOTH,expand=True)

scrly=tk.Scrollbar(mnfrm,orient=tk.VERTICAL)
scrlx=tk.Scrollbar(mnfrm,orient=tk.HORIZONTAL)

book=ttk.Treeview(mnfrm,columns=("Name","Phone Number","Email","Address","Note"),yscrollcommand=scrly.set,xscrollcommand=scrlx.set)

scrly.config(command=book.yview)
scrlx.config(command=book.xview)
scrly.pack(side=tk.RIGHT,fill=tk.Y)
scrlx.pack(side=tk.BOTTOM,fill=tk.X)

book.heading("Name",text="Name")
book.heading("Phone Number",text="Phone Number")
book.heading("Email",text="Email")
book.heading("Address",text="Address")
book.heading("Note",text="Note")
book["show"]="headings"

book.column("Name",width=100)
book.column("Phone Number",width=120)
book.column("Email",width=200)
book.column("Address",width=250)
book.column("Note",width=100)

book.pack(fill=tk.BOTH,expand=True)
book.bind("<ButtonRelease-1>",cur)

show()
cb.mainloop()
