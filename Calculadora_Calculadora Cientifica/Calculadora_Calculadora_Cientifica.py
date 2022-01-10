from tkinter import *
import tkinter as tk
from math import pi, tan, log, sin, cos, log10, acos, atan, asin
from tkinter import EXCEPTION, font
from tkinter import ttk
from tkinter.constants import ANCHOR, DISABLED
import tkinter.messagebox




#defino una funcion limpieza para borrar el contenido del calculo
def limpieza():
    global operacion
    calculo.set('0') #pone un cero en la pantalla
    operacion = ''   #borra la cuenta de la consola

def limpieza2():
    global operacion2
    calculo2.set('0') #pone un cero en la pantalla
    operacion2 = ''   #borra la cuenta de la consola

#defino la funcion que almacena los clics de cada tecla
def click(tecla):
    global operacion
    operacion = operacion + tecla
    calculo.set(operacion)
    

def click2(tecla):
    global operacion2
    operacion2 = operacion2 + tecla
    calculo2.set(operacion2)

#Defino la funcion que actua al tocar el =

def hacer_cuenta():
    global operacion
    try:
        total = str(eval(operacion))
    except Exception:
        limpieza()
        total = 'ERROR' 
    calculo.set(total)
    operacion = total

def hacer_cuenta2():
    global operacion2
    try:
        total = str(eval(operacion2))
    except Exception:
        limpieza()
        total = 'ERROR' 
    calculo2.set(total)
    operacion2 = total

def borrar():
    global operacion
    lista = []
    #creo una lista con los valores de operacion
    for i in range(len(operacion)):
        lista.append(operacion[i])
    #borro el ultimo caracter
    lista =  lista [:-1]
    operacion =  ''.join(lista)
    #muestro la cadena en la pantalla
    calculo.set(operacion)


def borrar2():
    global operacion2
    lista = []
    #creo una lista con los valores de operacion
    for i in range(len(operacion2)):
        lista.append(operacion2[i])
    #borro el ultimo caracter
    lista =  lista [:-1]
    operacion2 =  ''.join(lista)
    #muestro la cadena en la pantalla
    calculo2.set(operacion2)
    

#ventana para contener la calculadora

ventana = Tk()
ventana.title('CALCULADORA')
ventana.geometry('390x675')
ventana.resizable(0,0)

#Creacion de solapas
tabcontrol = ttk.Notebook(ventana)
tabcontrol.pack(fill='both', expand='yes')
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text='Caculadora')
tabcontrol.add(tab2, text='Calculadora Cientifica')


#Funcion de about_us

def about_us():
    tkinter.messagebox.showinfo('About Calculator', 'This is a calculator build using Python Tkinter by @Nicolas Patti')

#creamos la barra de menu y submenu

menubar = Menu(ventana)
ventana.config(menu=menubar)
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

#creamos una variable para mostrar el calculo en la pantalla

calculo = tk.StringVar()
calculo2 = tk.StringVar()

#llamo a la funcion limpieza para inicializar la calculadora
limpieza()
limpieza2()

#creamos la pantalla tab1

pantalla = Entry(tab1, font = ('arial',15,'bold'), 
                    width= 30,
                    bd= 15, 
                    bg = 'light grey', 
                    justify = 'right', 
                    state = tk.DISABLED,
                    textvariable= calculo
                )

pantalla.place(x = 10, y= 30)

#creamos la pantalla tab2

pantalla2 = Entry(tab2, font = ('arial',15,'bold'), 
                    width= 30,
                    bd= 15, 
                    bg = 'light grey', 
                    justify = 'right', 
                    state = tk.DISABLED,
                    textvariable= calculo2
                )

pantalla2.place(x = 10, y= 30)

#defino las dimensiones de la tecla
ancho = 10
alto = 2

#creo una variable para almacenar el calculo del lado de consola
operacion = ''
operacion2 = ''


##########BOTONES tab1##########

####Primera fila: 1 2 3 +
boton1 = Button(tab1, text='1', width=ancho, height=alto, bg='cyan2', command=lambda:click('1')).place(x=17, y=180)

boton2 = Button(tab1,text='2', width=ancho, height=alto, bg='cyan2', command=lambda:click('2')).place(x=107, y=180),

boton3 = Button(tab1,text='3', width=ancho, height=alto, bg='cyan2', command=lambda:click('3')).place(x=197, y=180)

boton_suma = Button(tab1,text='+', width=ancho, height=alto, bg='deep pink', command=lambda:click('+')).place(x=287, y=180)

####Segunda fila: 4 5 6 -

boton4 = Button(tab1,text='4', width=ancho, height=alto, bg='cyan2', command=lambda:click('4')).place(x=17, y=240)

boton5 = Button(tab1,text='5', width=ancho, height=alto, bg='cyan2', command=lambda:click('5')).place(x=107, y=240)

boton6 = Button(tab1,text='6', width=ancho, height=alto, bg='cyan2', command=lambda:click('6')).place(x=197, y=240)

boton_resta = Button(tab1,text='-', width=ancho, height=alto, bg='deep pink', command=lambda:click('-')).place(x=287, y=240)

#####tercera fila: 7 8 9 x

boton7 = Button(tab1,text='7', width=ancho, height=alto, bg='cyan2', command=lambda:click('7')).place(x=17, y=300)

boton8 = Button(tab1,text='8', width=ancho, height=alto, bg='cyan2', command=lambda:click('8')).place(x=107, y=300)

boton9 = Button(tab1,text='9', width=ancho, height=alto, bg='cyan2', command=lambda:click('9')).place(x=197, y=300)

boton_por = Button(tab1,text='x', width=ancho, height=alto, bg='deep pink', command=lambda:click('*')).place(x=287, y=300)

#####Cuarta fila: ( 0 ) /

boton_par_izq = Button(tab1,text='(', width=ancho, height=alto, bg='spring green', command=lambda:click('(')).place(x=17, y=360)

boton0 = Button(tab1,text='0', width=ancho, height=alto, bg='cyan2', command=lambda:click('0')).place(x=107, y=360)

boton_par_der = Button(tab1,text=')', width=ancho, height=alto, bg='spring green', command=lambda:click(')')).place(x=197, y=360)

boton_division = Button(tab1,text='/', width=ancho, height=alto, bg='deep pink', command=lambda:click('/')).place(x=287, y=360)

###Quinta fila: Raiz, coma decimal, potencia, resto

boton_raiz = Button(tab1,text='√', width=ancho, height=alto, bg='spring green', command=lambda:click('sqrt(')).place(x=17, y=420)

boton_coma = Button(tab1,text='.', width=ancho, height=alto, bg='cyan2', command=lambda:click('.')).place(x=107, y=420)

boton_potencia = Button(tab1,text='EXP', width=ancho, height=alto, bg='spring green', command=lambda:click('**')).place(x=197, y=420)

boton_resto = tk.Button(tab1,text='%', width=ancho, height=alto, bg='deep pink', command=lambda:click('%')).place(x=287, y=420)

####Sexta Fila: Clear, Factorial, Pi, =, Clear2 

boton_clear = Button(tab1,text='C', width=ancho, height=alto, bg='red2', command=limpieza).place(x=17, y=480)

boton_factorial = Button(tab1,text='!', width=ancho, height=alto, bg='cyan2', command=lambda:click('factorial(')).place(x=107, y=480)

boton_pi = Button(tab1,text='π', width=ancho, height=alto, bg='spring green', command=lambda:click(str(pi))).place(x=197, y=480)

boton_igual = Button(tab1,text='=', width=ancho, height=alto, bg='yellow', command=hacer_cuenta).place(x=287, y=480)

boton_borrar = Button(tab1,text='<--', width=ancho, height=alto, bg='red2', command=borrar).place(x=17, y=540)

##########BOTONES tab2##########

####Primera fila: 1 2 3 +
boton1 = Button(tab2, text='1', width=ancho, height=alto, bg='cyan2', command=lambda:click2('1')).place(x=17, y=240)

boton2 = Button(tab2,text='2', width=ancho, height=alto, bg='cyan2', command=lambda:click2('2')).place(x=107, y=240),

boton3 = Button(tab2,text='3', width=ancho, height=alto, bg='cyan2', command=lambda:click2('3')).place(x=197, y=240)

boton_suma = Button(tab2,text='+', width=ancho, height=alto, bg='deep pink', command=lambda:click2('+')).place(x=287, y=240)

####Segunda fila: 4 5 6 -

boton4 = Button(tab2,text='4', width=ancho, height=alto, bg='cyan2', command=lambda:click2('4')).place(x=17, y=300)

boton5 = Button(tab2,text='5', width=ancho, height=alto, bg='cyan2', command=lambda:click2('5')).place(x=107, y=300)

boton6 = Button(tab2,text='6', width=ancho, height=alto, bg='cyan2', command=lambda:click2('6')).place(x=197, y=300)

boton_resta = Button(tab2,text='-', width=ancho, height=alto, bg='deep pink', command=lambda:click2('-')).place(x=287, y=300)

#####tercera fila: 7 8 9 x

boton7 = Button(tab2,text='7', width=ancho, height=alto, bg='cyan2', command=lambda:click2('7')).place(x=17, y=360)

boton8 = Button(tab2,text='8', width=ancho, height=alto, bg='cyan2', command=lambda:click2('8')).place(x=107, y=360)

boton9 = Button(tab2,text='9', width=ancho, height=alto, bg='cyan2', command=lambda:click2('9')).place(x=197, y=360)

boton_por = Button(tab2,text='x', width=ancho, height=alto, bg='deep pink', command=lambda:click2('*')).place(x=287, y=360)

#####Cuarta fila: ( 0 ) /

boton_par_izq = Button(tab2,text='(', width=ancho, height=alto, bg='spring green', command=lambda:click2('(')).place(x=17, y=420)

boton0 = Button(tab2,text='0', width=ancho, height=alto, bg='cyan2', command=lambda:click2('0')).place(x=107, y=420)

boton_par_der = Button(tab2,text=')', width=ancho, height=alto, bg='spring green', command=lambda:click2(')')).place(x=197, y=420)

boton_division = Button(tab2,text='/', width=ancho, height=alto, bg='deep pink', command=lambda:click2('/')).place(x=287, y=420)

###Quinta fila: Raiz, coma decimal, potencia, resto

boton_raiz = Button(tab2,text='√', width=ancho, height=alto, bg='spring green', command=lambda:click2('sqrt(')).place(x=17, y=480)

boton_coma = Button(tab2,text='.', width=ancho, height=alto, bg='cyan2', command=lambda:click2('.')).place(x=107, y=480)

boton_potencia = Button(tab2,text='EXP', width=ancho, height=alto, bg='spring green', command=lambda:click2('**')).place(x=197, y=480)

boton_resto = tk.Button(tab2,text='%', width=ancho, height=alto, bg='deep pink', command=lambda:click2('%')).place(x=287, y=480)

####Sexta Fila: Clear, Factorial, Pi, =, Clear2 

boton_clear = Button(tab2,text='C', width=ancho, height=alto, bg='red2', command=limpieza2).place(x=17, y=540)

boton_factorial = Button(tab2,text='!', width=ancho, height=alto, bg='cyan2', command=lambda:click2('factorial(')).place(x=107, y=540)

boton_pi = Button(tab2,text='π', width=ancho, height=alto, bg='spring green', command=lambda:click2(str(pi))).place(x=197, y=540)

boton_igual = Button(tab2,text='=', width=ancho, height=alto, bg='yellow', command=hacer_cuenta2).place(x=287, y=540)

boton_borrar = Button(tab2,text='<--', width=ancho, height=alto, bg='red2', command=borrar2).place(x=17, y=600)

# tan, ln, sin, cos

botontan = Button(tab2, text='tan', width=ancho, height=alto,bg='dark orange', command=lambda:click2('tan(')).place(x=17,y=120)

botonln = Button(tab2, text='ln', width=ancho, height=alto,bg='dark orange', command=lambda:click2('log(')).place(x=107,y=120)

botonsin = Button(tab2, text='sin', width=ancho, height=alto,bg='dark orange', command=lambda:click2('sin(')).place(x=197,y=120)

botoncos =Button(tab2, text='cos', width=ancho, height=alto,bg='dark orange', command=lambda:click2('cos(')).place(x=287,y=120)

#arctan, log, arsin, arccos

botonarctan = Button(tab2, text='arctan', width=ancho, height=alto,bg='dark orange', command=lambda:click2('atan(')).place(x=17, y=180)

botonlog = Button(tab2, text='log', width=ancho, height=alto,bg='dark orange', command=lambda:click2('log10(')).place(x=107,y=180)

botonarcsin = Button(tab2, text='arcsin', width=ancho, height=alto, bg='dark orange', command=lambda:click2('asin(')).place(x=197,y=180)

botonarccos = Button(tab2, text='arccos', width=ancho, height=alto,bg='dark orange', command=lambda:click2('acos(')).place(x=287,y=180)






ventana.mainloop()