from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import sleep
import pymysql
import subprocess
from random import randint
import tkinter as tk
import tkinter.ttk as ttk

raiz= Tk()
str_resultado=StringVar()
raiz.resizable(0,0)
##titulo de la ventana
raiz.title("Ignorancia")
raiz.iconbitmap("Overwatchlogo.ico")
##tamaño de la ventana
raiz.geometry("1300x690")
##color del fondo
raiz.config(bg="red")

moira=PhotoImage(file="Jugador2.PNG")
mercy=PhotoImage(file="Jugador1.PNG")
duo=PhotoImage(file="Ignorancia.PNG")
fondo1=PhotoImage(file="fondo.PNG")
fondo2=PhotoImage(file="fondo2.PNG")

x_burro=20
y_burro=540
x_juga1=20
y_juga1=340
x_juga2=20
y_juga2=440
idmateria=""


str_ale=StringVar()
str_ale.set("")
str_nom=StringVar()
str_id=StringVar()
str_aux=StringVar()
str_op1=StringVar()
str_op2=StringVar()
str_op3=StringVar()
str_opc=StringVar()
str_nom.set("")
str_id.set("")
str_op1.set("")
str_op2.set("")
str_op3.set("")
str_opc.set("")
maximo=0
seleccion=IntVar()
turno=1
def lista_materias():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='maraton')
	cursor = conn.cursor()
	cursor.execute('select descripcion from materia')
	mts = []
	for row in cursor:
		mts.append(row[0])
	cursor.close()
	conn.close()
	return mts


def as_lista(event):
	global idmateria
	global maximo
	men=mat.get()
	##messagebox.showinfo(message=men)
	sql = "select id_materia from materia where descripcion='"+men+"'"
	db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
	cursor = db.cursor()
	cursor.execute(sql)
	idmateria = cursor.fetchone()[0]
	sql = "select max(id_pregunta) from pregunta"
	cursor.execute(sql)
	maximo = cursor.fetchone()[0]
	##messagebox.showinfo(message=idmateria)
def selec_pregunta():
	global idmateria
	global maximo
	db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
	cursor = db.cursor()
	registros=0
	while registros==0:
		str_ale.set(str(randint(0,maximo)))
		sql = "select count(*) from pregunta where id_materia="+str(idmateria)
		+ " and id_pregunta=" + str_ale.get()
		cursor.execute(sql)
		registros=cursor.fetchone()[0]
	sql="select id_pregunta, descripcion, opcion1, opcion2, opcion3, correcto, nivel from pregunta where id_materia="
	sql=sql+str(idmateria)+" and id_pregunta="+str_ale.get()
	cursor.execute(sql)
	for row in cursor:
		str_nom.set(row[1])
		str_op1.set(row[2])
		str_op2.set(row[3])
		str_op3.set(row[4])
		str_opc.set(row[5])
	e_pregunta.config(width=50)
	e_pregunta.place(x=690, y=60)
	pregunta_u.config(width=50)
	pregunta_u.place(x=690, y=90)
	r_opc1.config(width=50)
	r_opc1.place(x=665, y=120)
	opc1_u.config(width=50)
	opc1_u.place(x=690, y=120)
	r_opc2.config(width=50)
	r_opc2.place(x=665, y=150)
	opc2_u.config(width=50)
	opc2_u.place(x=690, y=150)
	r_opc3.config(width=50)
	r_opc3.place(x=665, y=180)
	opc3_u.config(width=50)
	opc3_u.place(x=690, y=180)
	cursor.close()
	db.close()




def pantalla2():
	subprocess.Popen(["python","pantalla2.py"])
def pantalla3():
	subprocess.Popen(["python","pantalla3.py"])
def pantalla4():
	subprocess.Popen(["python","pantalla4.py"])
def sel_prgunta():
	b_pregunta.config(height=1)
	b_pregunta.config(width=1)
	pregunta.config(height=400)
	pregunta.config(width=400)
	pregunta.config(image=fondo2)
	selec_pregunta()

def avanza1():
	global turno
	global x_juga1
	global y_juga1
	x_juga1 = x_juga1 + 50
	juga1.place(x=x_juga1, y=y_juga1)
	if x_juga1>=1000:
		messagebox.showinfo(message="Gano jugador 1")
	turno = 2
def avanza2():
	global turno
	global x_juga2
	global y_juga2
	x_juga2 = x_juga2 + 100
	juga2.place(x=x_juga2, y=y_juga2)
	if x_juga2>=1000:
		messagebox.showinfo(message="Gano jugador 2")
	turno = 1
def avanza_burro():
	global turno
	global x_burro
	global y_burro
	x_burro = x_burro + 50
	burro.place(x=x_burro, y=y_burro)
	if turno==1:
		turno = 2
	else:
		turno = 1
	if x_burro>=1000:
		messagebox.showinfo(message="Gano la ignorancia")
def seleccionado():
	global turno
	global x_burro
	global y_burro
	global x_juga2
	global y_juga2
	if str(seleccion.get())==str_opc.get():
		messagebox.showinfo(message="Muy bien!!!!!!!!")
		if turno==1:
			avanza1()
		else:
			avanza2()
	else:
		messagebox.showinfo(message="Respuesta incorrecta")
		avanza_burro()
	b_pregunta.config(height=1)
	b_pregunta.config(width=1)
	pregunta.config(height=17)
	pregunta.config(width=60)
	e_pregunta.config(width=0)
	e_pregunta.place(x=620, y=60)
	pregunta_u.config(width=0)
	pregunta_u.place(x=650, y=90)
	r_opc1.config(width=0)
	r_opc1.place(x=655, y=120)
	opc1_u.config(width=0)
	opc1_u.place(x=650, y=120)
	r_opc2.config(width=0)
	r_opc2.place(x=655, y=150)
	opc2_u.config(width=0)
	opc2_u.place(x=650, y=150)
	r_opc3.config(width=0)
	r_opc3.place(x=655, y=180)
	opc3_u.config(width=0)
	opc3_u.place(x=650, y=180)
	str_nom.set("")
	str_id.set("")
	str_op1.set("")
	str_op2.set("")
	str_op3.set("")
	str_opc.set("")


conn=pymysql.connect(host="localhost",user="root",passwd="",db="maraton")
cursor=conn.cursor()

cursor.execute("select Nombre from usuario")

fondos=Label(raiz,image=fondo1)
fondos.place(x=0, y=0)



##boton para desplegar la ventana de usuarios
boton1=Button(raiz,cursor="mouse",text="Usuario",relief="ridge",font="Helvetica 10 bold",pady=5,width=13,bg="gray1",fg="white",command=pantalla2)
boton1.place(x=20, y=30)

##boton para desplegar la ventana de materias
boton2=Button(raiz,cursor="mouse",text="Materia",relief="ridge",font="Helvetica 10 bold",pady=5,width=13,bg="gray1",fg="white",command=pantalla3)
boton2.place(x=155, y=30)


##boton para desplegar la ventana de preguntas
boton3=Button(raiz,cursor="mouse",text="Pregunta",relief="ridge",font="Helvetica 10 bold",pady=5,width=13,bg="gray1",fg="white",command=pantalla4)
boton3.place(x=290, y=30)
##Etiqueta para el combobox de materia
mate=Label(raiz, bg="LightSteelBlue2", fg="black", font='Helvetica 12 bold',text="Materia")
mate.place(x=300, y=1)
##Combobox para elegir materia
mat=ttk.Combobox(raiz, font='Helvetica 10', width=20)
mat.place(x=370, y = 1)
mat.bind('<<ComboboxSelected>>', as_lista)

lista=lista_materias()
mat['values']=lista





##Etiqueta 
pregunta= Label(raiz, bg='SkyBlue1', height=1,width=1)
pregunta.place(x=900, y=0)

##Marcador para ¿? (esta en la parte superior izquierda)
aleatorio = Entry(raiz, textvariable=str_ale, font='Helvetica 8', width=2)
aleatorio.place(x=20, y=30)

##Etiqueta para el marcador de pregunta
e_pregunta= Label(raiz, bg='brown', fg="white", text="Pregunta", font='Helvetica 8 bold', width=0)
e_pregunta.place(x=910, y=30)

##Marcador de pregunta
pregunta_u = Entry(raiz, textvariable=str_nom, font='Helvetica 8', width=0)
pregunta_u.place(x=910, y=60)

##boton1 para asignar una respuesta
r_opc1=Radiobutton(raiz, value=1, variable=seleccion, command=seleccionado,width=0)
r_opc1.place(x=1200, y=120)

#Marcador
opc1_u = Entry(raiz, textvariable=str_op1, font='Helvetica 8', width=0)
opc1_u.place(x=910, y=120)

##boton2 para asignar una respuesta
r_opc2=Radiobutton(raiz, value=2, variable=seleccion, command=seleccionado,width=0)
r_opc2.place(x=1200, y=150)

##Marcador
opc2_u = Entry(raiz, textvariable=str_op2, font='Helvetica 8', width=0)
opc2_u.place(x=910, y=150)

##boton3 para asignar una respuesta
r_opc3=Radiobutton(raiz, value=3, variable=seleccion, command=seleccionado, width=0)
r_opc3.place(x=1200, y=180)

##Marcador
opc3_u = Entry(raiz, textvariable=str_op3, font='Helvetica 8', width=0)
opc3_u.place(x=910, y=180)

##Marcador
opcc_u = Entry(raiz, textvariable=str_opc, font='Helvetica 8', width=1)
opcc_u.place(x=910, y=210)

##Etiqueta
juga1= Label(raiz, bg='red1',image=mercy,  height=95,width=100)
juga1.place(x=x_juga1, y=y_juga1)

##Etiqueta
juga2= Label(raiz, bg='red1',image=moira,  height=95,width=100)
juga2.place(x=x_juga2, y=y_juga2)

##Etiqueta
burro= Label(raiz, bg='red1',image=duo,  height=95,width=100)
burro.place(x=x_burro, y=y_burro)

##Boton
b_pregunta = Button(raiz, cursor="mouse", bg="white", relief="ridge",command=sel_prgunta, width=10, height=10)
b_pregunta.place(x=800, y=0)


raiz.mainloop()