import matplotlib.pyplot as plt
from pandas import*
import numpy as np
from tkinter  import *
from tkinter import messagebox
from tkinter import scrolledtext 
import itertools
from cx_Oracle import *
import socket
import requests
import bs4
from urllib.request import urlopen
root=Tk()
root.title("python")
root.geometry("1500x1500+20+50")
def f1():
	root.withdraw()
	adst.deiconify()
def f2():
	adst.withdraw()
	root.deiconify()
def f4():
	vt.withdraw()
	root.deiconify()
def f7():
	root.withdraw()
	up.deiconify()
def f9():
	up.withdraw()
	root.deiconify()
def f10():
	root.withdraw()
	dell.deiconify()
def f11():
	dell.withdraw()
	root.deiconify()
def fd():
	con=None
	try:
		con=connect('c##system123/tiger')
		rno=int(dentrno.get())
		cursor=con.cursor()
		if rno<0:
			messagebox.showerror("issue","rollno ")
						
		else:
			cursor=con.cursor()
			sql1="select rno from pro"
			cursor.execute(sql1)
			data=cursor.fetchall()
			dat=list(itertools.chain(*data))
			f=0
			for n in dat:
				if n==str(rno):
					sql="delete from pro where rno='%d'  "
					args=(rno)
					cursor.execute(sql%args)
					con.commit()
					messagebox.showinfo("success","deleted")
					f=1
			if f==0:
				messagebox.showerror("issue","record not found ")
			dentrno.delete(0,END)	
	except (ValueError,RuntimeError,TypeError):
			messagebox.showerror("issue","Enter valid rollno")
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue", ""+e)
	finally:
		if con is not None:
			con.close()
		
def f3():
	vdata.delete(1.0,END)
	root.withdraw()
	vt.deiconify()
	con=None
	try:
		con=connect('c##system123/tiger')
		cursor=con.cursor()
		sql="select rno,name,marks from pro order by marks desc"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg+"rno= "+str(d[0])+ "name= "+str(d[1]) + "marks= "+str(d[2])+"\n"
		vdata.insert(INSERT,msg)
	except DatabaseError as e:
		print("issue",e)
	finally:
		if con is not None:
			con.close()
	
def f8():
	con=None
	try:
		con=connect('c##system123/tiger')
		try:
			rno=int(uentrno.get())
			if rno>0:
				
				try:
					name=uentname.get()
					if name.isalpha() :
						if len(name)>2:
							try:
								mks=int(uentmks.get())
					
	
								cursor=con.cursor()
								if rno<0:
									messagebox.showerror("issue","rollno is invalid")
							
								if mks<=0 or mks>101:
									messagebox.showerror("issue","enter No from 0-100")	
									uentmks.delete(0,END)
									uentmks.focus()				
								else:
									cursor=con.cursor()
									sql1="select rno from pro"
									cursor.execute(sql1)
									data=cursor.fetchall()
									dat=list(itertools.chain(*data))
									f=0
									
									
									for n in dat:
										
										if n==str(rno):
											
											sql="update pro set marks='%d',name='%s' where rno='%d' "
											args=(mks,name,rno)
											cursor.execute(sql%args)
											con.commit()	
											messagebox.showinfo("success","updated")
									
											f=1
									if f==0:
										messagebox.showerror("issue","record not found")		
									uentrno.delete(0,END)	   
									uentname.delete(0,END)								
									uentmks.delete(0,END)

									uentrno.focus()
							except (ValueError,RuntimeError,TypeError):
								messagebox.showerror("issue","Enter valid marks")
								uentmks.delete(0,END)
								uentmks.focus()
						else:
							messagebox.showerror("issue","minimum 3 letters")
							uentname.delete(0,END)
							uentname.focus()
					else:
						messagebox.showerror("issue","Only alphabets allowed")
						uentname.delete(0,END)
						uentname.focus()
				except (ValueError,RuntimeError,TypeError):
					messagebox.showerror("issue","Enter valid name")
					uentname.delete(0,END)
					uentmks.delete(0,END)
					uentname.focus()
			else:
				messagebox.showerror("issue","enter +ve values")	
				uentrno.delete(0,END)
				uentrno.focus()
		except (ValueError,RuntimeError,TypeError):
			messagebox.showerror("issue","Enter valid rno")
			entrno.delete(0,END)
			entrno.focus()
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue", ""+e)
	finally:
		if con is not None:
			con.close()
def f5():
	con=None
	try:
		con=connect('c##system123/tiger')
		try:
			rno=int(entrno.get())
			try:
				if rno>0:
					try:
						name=entname.get()
						if name.isalpha():
							if len(name)>2 :
								try:
									mks=int(entmks.get())
							
									cursor=con.cursor()
								
								
							
									
									if mks<=0 or mks>101:
										messagebox.showerror("issue","enter No from 0-100")
										entmks.delete(0,END)
										entmks.focus()
									else:
										sql="insert into pro values('%d','%s','%d')"
										args=(rno,name,mks)
										cursor.execute(sql%args)
										con.commit()
										messagebox.showinfo("success","inserted")
										entrno.delete(0,END)
										entname.delete(0,END)
										entmks.delete(0,END)
										entrno.focus()
						
						
								except (ValueError,RuntimeError,TypeError):
									messagebox.showerror("issue","Enter valid marks")
									entmks.delete(0,END)
									entmks.focus()
							else:
								messagebox.showerror("issue","enter minimum 3 letters")
								entname.delete(0,END)
								entname.focus()
						else:
							messagebox.showerror("issue","Enter only alphabets")
							entname.delete(0,END)
							entname.focus()
					except (ValueError,RuntimeError,TypeError):
						messagebox.showerror("issue","Enter valid name")
						entname.delete(0,END)
						entmks.delete(0,END)
						entname.focus()
				else:
					messagebox.showerror("issue","rollno+ve ")
					entrno.delete(0,END)
					entrno.focus()
		
			except (IntegrityError):
				messagebox.showerror("issue","Enter diff rno")
				entrno.delete(0,END)
				entname.delete(0,END)
				entmks.delete(0,END)
				entrno.focus()
		
		except(ValueError,TypeError,RuntimeError):
				messagebox.showerror("issue","Enter valid rno")
				entrno.delete(0,END)
				entname.delete(0,END)
				entmks.delete(0,END)
				entrno.focus()
		

						
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue", ""+e)
	finally:
			
							
		if con is not None:
			con.close()
def fg():
	
	
	con=connect("c##system123/tiger")
	cursor=con.cursor()
	cursor.execute("select count(*) from pro order by marks DESC")
	for r in cursor:
		tot=r[0]
	t=np.arange(tot)
	cursor.execute("select name,marks from pro order by marks DESC ")
	
	names=[]
	marks=[]
	
	for r in cursor:
		names.append(r[0])
		marks.append(r[1])
			
	
	bar_width=0.5
	plt.bar(t[:5],np.array(marks)[:5],bar_width,label="marks")
	plt.title("Student detail")
	plt.xlabel("Student name")
	plt.ylabel("Marks")
	plt.xticks(t[:5],np.array(names)[:5])
	plt.legend()
	xs=[x for x in range(0,5)]
	for x,y in zip(xs,marks):
		plt.annotate(marks[x],(x-bar_width/2,y))
	
	plt.show()

prjectName = Label(root,text="Student management with webscraping and socket connection",font=('arial',25,'bold'))
btnadd=Button(root,text="Add",font=('comic sans ms',16,'bold'),command=f1)
btnview=Button(root,text="View",font=('comic sans ms',16,'bold'),command=f3)
btndelete=Button(root,text="Delete",font=('comic sans ms',16,'bold'),command=f10)
btnup=Button(root,text="Update",font=('comic sans ms',16,'bold'),command=f7)
btngr=Button(root,text="Graph",font=('comic sans ms',16,'bold'),command=fg)
#city
try:
	socket.create_connection(("www.google.com",80))
	res=requests.get("https://ipinfo.io")
	data=res.json()
	city=data['city']
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address=a1+a2+a3
	res=requests.get(api_address)
	data=res.json()
	temp=data['main']['temp']
	c=Label(root,text="City:" ,font=('comic sans ms',16,'bold'))
	ci=Entry(root,bd=5,font=('comic sans ms',16,'bold'))
	ci.insert(INSERT,city)
	t=Label(root,text="Temperature:" ,font=('comic sans ms',16,'bold'))
	tc=Entry(root,bd=5,font=('comic sans ms',16,'bold'))
	tc.insert(INSERT,temp)
	
	
	
		
	c.place(x=80,y=480)
	ci.place(x=140,y=480)
	t.place(x=430,y=480)
	tc.place(x=580,y=480)
except OSError as e:
	print("check network",e)

#qoute
lblqoute=Label(root,text="Quote of the day",font=('arial',16,'bold'))
entqotd=Entry(root,bd=3,font=('arial',16,'bold'),width=90)
url = "http://www.values.com/inspirational-quotes"
res = requests.get(url=url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'})
# print(res)
soup=bs4.BeautifulSoup(res.text,'lxml')
quote=soup.find('img', attrs = {'class':'margin-10px-bottom shadow'}) 
# print(quote)
msg=quote['alt']
entqotd.insert(INSERT,msg)
lblqoute.place(x=50,y=530)
entqotd.place(x=350,y=530,height=100)


prjectName.pack(pady=30)
btnadd.pack(pady=10)
btnview.pack(pady=10)
btndelete.pack(pady=10)
btnup.pack(pady=10)
btngr.pack(pady=10)

#Add screen
adst=Toplevel(root)
adst.title("ADD S")
adst.geometry("500x500+200+200")
lblrno=Label(adst,text="Enter Rno",font=('comic sans ms',16,'bold'))
entrno=Entry(adst,bd=5,font=('comic sans ms',16,'bold'))

lblname=Label(adst,text="Enter Name",font=('comic sans ms',16,'bold'))
entname=Entry(adst,bd=5,font=('comic sans ms',16,'bold'))
n=entname.get()

lblmks=Label(adst,text="Enter Marks",font=('comic sans ms',16,'bold'))
entmks=Entry(adst,bd=5,font=('comic sans ms',16,'bold'))
btnSave=Button(adst,text="Save",font=('comic sans ms',16,'bold'),command=f5)

btnBack=Button(adst,text="Back",font=('comic sans ms',16,'bold'),command=f2)
lblrno.pack(pady=10)
entrno.pack(pady=10)
lblname.pack(pady=10)
entname.pack(pady=10)
lblmks.pack(pady=10)
entmks.pack(pady=10)
btnSave.pack(pady=10)
btnBack.pack(pady=10)
adst.withdraw()


#view screen
vt=Toplevel(root)
vt.title("View data")
vt.geometry("500x500+200+200")
vdata=scrolledtext.ScrolledText(vt,width=30,height=20)
btnback=Button(vt,text="Back",font=('comic sans ms,',16,'bold'),command=f4)
vdata.pack(pady=10)
btnback.pack(pady=10)
vt.withdraw()

#update
up=Toplevel(root)
up.title("UPDATE S")
up.geometry("500x500+200+200")
urno=Label(up,text="Enter rno",font=('arial',16,'bold'))
uentrno=Entry(up,bd=5,font=('arial',16,'bold'))
uname=Label(up,text="Enter name",font=('arial',16,'bold'))
uentname=Entry(up,bd=5,font=('arial',16,'bold'))
umks=Label(up,text="Enter marks",font=('arial',16,'bold'))
uentmks=Entry(up,bd=5,font=('arial',16,'bold'))

btnupsave=Button(up,text="Save",font=('arial',16,'bold'),command=f8)
btnupback=Button(up,text="Back",font=('arial',16,'bold'),command=f9)

urno.pack(pady=10)
uentrno.pack(pady=10)
uname.pack(pady=10)
uentname.pack(pady=10)
umks.pack(pady=10)
uentmks.pack(pady=10)
btnupsave.pack(pady=10)
btnupback.pack(pady=10)
up.withdraw()


#delete
dell=Toplevel(root)
dell.title("DELETE S")
dell.geometry("500x500+200+200")
drno=Label(dell,text="Enter rno",font=('arial',16,'bold'))
dentrno=Entry(dell,bd=5,font=('arial',16,'bold'))
btndelsave=Button(dell,text="Delete",font=('arial',16,'bold'),command=fd)
btndelback=Button(dell,text="Back",font=('arial',16,'bold'),command=f11)

drno.pack(pady=10)
dentrno.pack(pady=10)
btndelsave.pack(pady=10)
btndelback.pack(pady=10)
dell.withdraw()


root.mainloop()

 
