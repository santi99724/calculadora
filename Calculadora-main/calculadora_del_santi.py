#Projecto calculdora
#Importamos la biblioteca tkinter que sirve para crear ventanas 
from math import*
from tkinter import*
from math import sqrt as r 
from math import sin as sin
from math import cos as cos
from math import tan as tan

#Aca asignamos la variable ventana con tk que hace la ventana luego el geometry que es para el tamaño
#y title para el nombre que aparecera cuando abramos la ventana
ventana= Tk()
ventana.title("Calculadora")
ventana.config(bg='grey63')
#caja de texto
caja=Entry(ventana, font=('System 20'),bg='dark olive green')
caja.grid(row=0, column=0, columnspan=6, padx=5, pady=5)
#variables globales
A=0
condicion=0
num1=0
num2=0
num3=0
#Funciones para  colores de la calculadora 
def azul():
    alto=3
    ancho=11
    caja.config(bg='#15ab92')
    botonE=Button(ventana, text="e^x",width=ancho, height=alto,bg='#0E60E6', command=lambda:FuncionE(e))
    Theme= Button(ventana, text="Theme",width=ancho, height=alto, bg='#0E60E6', command=cambioColor("verde"))
    botonCero=Button(ventana, text= "0", width=ancho, height=alto, bg='#1C36FC', command=lambda:botones(0))
    botonPunto=Button(ventana, text=".", width=ancho, height=alto, bg='#0E60E6', command=lambda:botones(','))
    botonPi=Button(ventana, text= "1/x", width=ancho, height=alto, bg='#0E60E6', command=lambda:botonesInverso('**-1'))
    botonPorcen=Button(ventana, text="%", width=ancho, height=alto, bg='#0E60E6', command=lambda:botones('%'))
    botonIgual=Button(ventana, text="=", width=ancho, height=alto, bg='#0E60E6', command=igual)
    boton1=Button(ventana, text="1", width=ancho, height=alto,bg='#1C36FC', command=lambda:botones(1))
    boton2=Button(ventana, text="2", width=ancho, height=alto, bg='#1C36FC', command=lambda:botones(2))
    boton3=Button(ventana, text="3", width=ancho, height=alto, bg='#1C36FC', command=lambda:botones(3))
    botonMas=Button(ventana, text="═╬═  ", width=ancho, height=alto, bg='#0E60E6', command=lambda:botones('+'))
    botonMenos=Button(ventana, text="▄▄ ", width=ancho, height=alto, bg='#0E60E6', command=lambda:botones('-'))
    boton4=Button(ventana, text="4", width=ancho, height=alto, bg='#1C36FC', command=lambda:botones(4))
    boton5=Button(ventana, text="5", width=ancho, height=alto, bg='#1C36FC',command=lambda:botones(5))
    boton6=Button(ventana, text='6', width=ancho, height=alto, bg='#1C36FC', command=lambda:botones(6) )
    botonMulti=Button(ventana, text="×", width=ancho, height=alto, bg='#0E60E6', command=lambda:botones('*'))
    botonDivision=Button(ventana, text='÷',width=ancho, height=alto, bg='#0E60E6', command=lambda:botones('/'))
    boton7=Button(ventana, text='7', width=ancho, height=alto, bg='#1C36FC', command=lambda:botones(7))
    boton8=Button(ventana, text='8', width=ancho, height=alto, bg='#1C36FC', command=lambda:botones(8))
    boton9=Button(ventana, text='9', width=ancho, height=alto, bg='#1C36FC', command=lambda:botones(9))


    botonDel=Button(ventana, text='Del', width=ancho, height=alto, bg='#750FFE', command=borrar)
    botonAC=Button(ventana, text='AC', width=ancho, height=alto, bg='#2F0EE6', command=AC)
    botonIzquier=Button(ventana,text='🢀', width=ancho, height=alto, bg='#0E60E6',command=lambda: flechaIz())
    botonDerecha=Button(ventana, text='🢂', width=ancho, height=alto, bg='#0E60E6', command=lambda: flechaDer())

    botonRaiz=Button(ventana, text='√ ', width=ancho, height=alto, bg='#0E60E6', command=lambda:botones('r'))
    botonExponente=Button(ventana,text='Exp', width=ancho, height=alto, bg='#0E60E6', command=lambda:botonesExp('**'))
    botonLog=Button(ventana, text='Log', width=ancho, height=alto, bg='#0E60E6', command=lambda:botonesLog('log'))
    botonParentesis=Button(ventana, text='( ', width=ancho, height=alto, bg='#0E60E6', command=lambda:botones('('))
    botonParentesisII=Button(ventana, text=') ', width=ancho, height=alto, bg='#0E60E6', command=lambda:botones(')'))
    botonseno=Button(ventana, text='sin ', width=ancho, height=alto,bg='dark slate gray',command=Seno)
    botoncoseno=Button(ventana, text='cos ', width=ancho, height=alto, bg='dark slate gray', command=Cos)
    botontangente=Button(ventana, text='tan ', width=ancho, height=alto, bg='dark slate gray', command=Tan)


    ventana.config(bg='#0FA9FE')
    #colocar botones
    botonE.grid(row=1, column=4, padx=5, pady=5)
    Theme.grid(row= 1,column=0, padx=5, pady=5)
    botonParentesis.grid(row=1, column=1, padx=5, pady=5)
    botonParentesisII.grid(row=1, column=3, padx=5, pady=5)
    botonRaiz.grid(row=2, column=0, padx=5, pady=5)
    botonIzquier.grid(row=2, column=1, padx=5, pady=5)
    botonExponente.grid(row=2, column=2, padx=5, pady=5)
    botonDerecha.grid(row=2, column=3, padx=5, pady=5)
    botonLog.grid(row=2, column=4, padx=5, pady=5)
    boton7.grid(row=3, column=0, padx=5, pady=5)
    boton8.grid(row=3, column=1, padx=5, pady=5)
    boton9.grid(row=3, column=2, padx=5, pady=5)
    botonDel.grid(row=3, column=3, padx=5, pady=5)
    botonAC.grid(row=3, column=4, padx=5, pady=5)
    boton4.grid(row=4, column=0, padx=5, pady=5)
    boton5.grid(row=4, column=1, padx=5, pady=5)
    boton6.grid(row=4, column=2, padx=5, pady=5)
    botonMulti.grid(row=4, column=3, padx=5, pady=5)
    botonDivision.grid(row=4, column=4, padx=5, pady=5)
    boton1.grid(row=5, column=0, padx=5, pady=5)
    boton2.grid(row=5, column=1, padx=5, pady=5)
    boton3.grid(row=5, column=2, padx=5, pady=5)
    botonMas.grid(row=5, column=3, padx=5, pady=5)
    botonMenos.grid(row=5, column=4, padx=5, pady=5)
    botonCero.grid(row=6, column=0, padx=5, pady=5)
    botonPunto.grid(row=6, column=1, padx=5, pady=5)
    botonPi.grid(row=6, column=2, padx=5, pady=5)
    botonPorcen.grid(row=6, column=3, padx=5, pady=5)
    botonIgual.grid(row=7, column=0, padx=5, pady=5)
    botonseno.grid(row=7, column=4, padx=5, pady=5)
    botoncoseno.grid(row=6, column=4, padx=5, pady=5)
    botontangente.grid(row=7, column=4, padx=5, pady=5)

def verde():

    alto=3
    ancho=11
    caja.config(bg='DarkGoldenrod4')
    botonE=Button(ventana, text="e^x",width=ancho, height=alto,bg='#50DE5C', command=lambda:FuncionE(e))
    Theme= Button(ventana, text="Theme",width=ancho, height=alto, bg='#50DE5C', command=cambioColor("Casio"))
    botonCero=Button(ventana, text= "0", width=ancho, height=alto, bg='#82FA5A', command=lambda:botones(0))
    botonPunto=Button(ventana, text=".", width=ancho, height=alto, bg='#50DE5C', command=lambda:botones(','))
    botonPi=Button(ventana, text= "1/x", width=ancho, height=alto, bg='#50DE5C', command=lambda:botonesInverso('**-1'))
    botonPorcen=Button(ventana, text="%", width=ancho, height=alto, bg='#50DE5C', command=lambda:botones('%'))
    botonIgual=Button(ventana, text="=", width=ancho, height=alto, bg='#50DE5C', command=igual)
    boton1=Button(ventana, text="1", width=ancho, height=alto, bg='#82FA5A', command=lambda:botones(1))
    boton2=Button(ventana, text="2", width=ancho, height=alto, bg='#82FA5A', command=lambda:botones(2))
    boton3=Button(ventana, text="3", width=ancho, height=alto, bg='#82FA5A', command=lambda:botones(3))
    botonMas=Button(ventana, text="═╬═  ", width=ancho, height=alto, bg='#50DE5C', command=lambda:botones('+'))
    botonMenos=Button(ventana, text="▄▄ ", width=ancho, height=alto, bg='#50DE5C', command=lambda:botones('-'))
    boton4=Button(ventana, text="4", width=ancho, height=alto, bg='#82FA5A', command=lambda:botones(4))
    boton5=Button(ventana, text="5", width=ancho, height=alto, bg='#82FA5A', command=lambda:botones(5))
    boton6=Button(ventana, text='6', width=ancho, height=alto, bg='#82FA5A', command=lambda:botones(6))
    botonMulti=Button(ventana, text="×", width=ancho, height=alto, bg='#50DE5C', command=lambda:botones('*'))
    botonDivision=Button(ventana, text='÷',width=ancho, height=alto, bg='#50DE5C', command=lambda:botones('/'))
    boton7=Button(ventana, text='7', width=ancho, height=alto, bg='#82FA5A', command=lambda:botones(7))
    boton8=Button(ventana, text='8', width=ancho, height=alto, bg='#82FA5A', command=lambda:botones(8))
    boton9=Button(ventana, text='9', width=ancho, height=alto, bg='#82FA5A', command=lambda:botones(9))
    botonDel=Button(ventana, text='Del', width=ancho, height=alto, bg='#5AFAF0', command=borrar) 
    botonAC=Button(ventana, text='AC', width=ancho, height=alto, bg='#50DEAC', command=AC)
    botonRaiz=Button(ventana, text='√ ', width=ancho, height=alto, bg='#50DE5C', command=lambda:botones('r'))
    botonIzquier=Button(ventana,text='🢀', width=ancho, height=alto, bg='#50DE5C', command=lambda:flechaIz())
    botonExponente=Button(ventana,text='Exp', width=ancho, height=alto, bg='#50DE5C', command=lambda:botones('**'))
    botonDerecha=Button(ventana, text='🢂', width=ancho, height=alto, bg='#50DE5C', command=lambda:flechaDer())
    botonLog=Button(ventana, text='Log', width=ancho, height=alto, bg='#50DE5C', command=lambda:botonesLog('log'))
    botonParentesis=Button(ventana, text='( ', width=ancho, height=alto, bg='#50DE5C', command=lambda:botones('('))
    botonParentesisII=Button(ventana, text=') ', width=ancho, height=alto, bg='#50DE5C', command=lambda:botones(')'))
    botonseno=Button(ventana, text='sin ', width=ancho, height=alto,bg='dark slate gray',command=Seno)
    botoncoseno=Button(ventana, text='cos ', width=ancho, height=alto, bg='dark slate gray', command=Cos)
    botontangente=Button(ventana, text='tan ', width=ancho, height=alto, bg='dark slate gray', command=Tan)

    ventana.config(bg='#65F599')
    #colocar botones
    botonE.grid(row=1, column=4, padx=5, pady=5)
    Theme.grid(row= 1,column=0, padx=5, pady=5)
    botonParentesis.grid(row=1, column=1, padx=5, pady=5)
    botonParentesisII.grid(row=1, column=3, padx=5, pady=5)
    botonRaiz.grid(row=2, column=0, padx=5, pady=5)
    botonIzquier.grid(row=2, column=1, padx=5, pady=5)
    botonExponente.grid(row=2, column=2, padx=5, pady=5)
    botonDerecha.grid(row=2, column=3, padx=5, pady=5)
    botonLog.grid(row=2, column=4, padx=5, pady=5)
    boton7.grid(row=3, column=0, padx=5, pady=5)
    boton8.grid(row=3, column=1, padx=5, pady=5)
    boton9.grid(row=3, column=2, padx=5, pady=5)
    botonDel.grid(row=3, column=3, padx=5, pady=5)
    botonAC.grid(row=3, column=4, padx=5, pady=5)
    boton4.grid(row=4, column=0, padx=5, pady=5)
    boton5.grid(row=4, column=1, padx=5, pady=5)
    boton6.grid(row=4, column=2, padx=5, pady=5)
    botonMulti.grid(row=4, column=3, padx=5, pady=5)
    botonDivision.grid(row=4, column=4, padx=5, pady=5)
    boton1.grid(row=5, column=0, padx=5, pady=5)
    boton2.grid(row=5, column=1, padx=5, pady=5)
    boton3.grid(row=5, column=2, padx=5, pady=5)
    botonMas.grid(row=5, column=3, padx=5, pady=5)
    botonMenos.grid(row=5, column=4, padx=5, pady=5)
    botonCero.grid(row=6, column=0, padx=5, pady=5)
    botonPunto.grid(row=6, column=1, padx=5, pady=5)
    botonPi.grid(row=6, column=2, padx=5, pady=5)
    botonPorcen.grid(row=6, column=3, padx=5, pady=5)
    botonIgual.grid(row=7, column=0, padx=5, pady=5)
    botonseno.grid(row=7, column=4, padx=5, pady=5)
    botoncoseno.grid(row=6, column=4, padx=5, pady=5)
    botontangente.grid(row=7, column=4, padx=5, pady=5)
def Casio():
    #variables para alto y ancho de los botones
    alto=3
    ancho=11
    #Todos los  botones
    caja.config(bg='dark olive green')
    ventana.config(bg='grey63')
    Theme= Button(ventana, text="Theme",width=ancho, height=alto,bg='LightSteelBlue4', command=cambioColor("azul"))
    botonE=Button(ventana, text="e^x",width=ancho, height=alto,bg='gray25', command=lambda:FuncionE(e))
    botonCero=Button(ventana, text= "0", width=ancho, height=alto,bg='gray25',command=lambda:botones(0))
    botonPunto=Button(ventana, text=".", width=ancho, height=alto,bg='gray25',command=lambda:botones(','))
    botonPi=Button(ventana, text= "1/x", width=ancho, height=alto,bg='gray25',command=lambda:botonesInverso('**-1'))
    botonPorcen=Button(ventana, text="%", width=ancho, height=alto,bg='gray25',command=lambda:botones('%'))
    botonIgual=Button(ventana, text="=", width=ancho, height=alto,bg='gray25',command=igual)
    boton1=Button(ventana, text="1", width=ancho, height=alto,bg='gray25',command=lambda:botones(1))
    boton2=Button(ventana, text="2", width=ancho, height=alto,bg='gray25',command=lambda:botones(2))
    boton3=Button(ventana, text="3", width=ancho, height=alto,bg='gray25',command=lambda:botones(3))
    botonMas=Button(ventana, text="═╬═", width=ancho, height=alto,bg='gray25',command=lambda:botones('+'))
    botonMenos=Button(ventana, text="▄▄ ", width=ancho, height=alto,bg='gray25',command=lambda:botones('-'))
    boton4=Button(ventana, text="4", width=ancho, height=alto,bg='gray25',command=lambda:botones(4))
    boton5=Button(ventana, text="5", width=ancho, height=alto,bg='gray25',command=lambda:botones(5))
    boton6=Button(ventana, text='6', width=ancho, height=alto,bg='gray25',command=lambda:botones(6))
    botonMulti=Button(ventana, text="×", width=ancho, height=alto,bg='gray25',command=lambda:botones('**'))
    botonDivision=Button(ventana, text='÷',width=ancho, height=alto,bg='gray25',command=lambda:botones('/'))
    boton7=Button(ventana, text='7', width=ancho, height=alto,bg='gray25',command=lambda:botones(7))
    boton8=Button(ventana, text='8', width=ancho, height=alto,bg='gray25',command=lambda:botones(8))
    boton9=Button(ventana, text='9', width=ancho, height=alto,bg='gray25',command=lambda:botones(9))

    botonDel=Button(ventana, text='Del', width=ancho, height=alto,bg='DeepPink4', command=borrar)
    botonAC=Button(ventana, text='AC', width=ancho, height=alto,bg='DeepPink4', command=AC)
    botonIzquier=Button(ventana,text='🢀', width=ancho, height=alto,bg='dark slate gray',command=lambda: flechaIz())
    botonDerecha=Button(ventana, text='🢂', width=ancho, height=alto,bg='dark slate gray',command=lambda:flechaDer())

    botonRaiz=Button(ventana, text='√ ', width=ancho, height=alto,bg='dark slate gray',command=lambda:botones('r'))
    botonExponente=Button(ventana,text='Exp', width=ancho, height=alto,bg='dark slate gray',command=lambda:botones('**'))
    botonLog=Button(ventana, text='Log', width=ancho, height=alto,bg='dark slate gray',command=lambda:botonesLog('log'))
    botonParentesis=Button(ventana, text='( ', width=ancho, height=alto,bg='LightSteelBlue4',command=lambda:botones('('))
    botonParentesisII=Button(ventana, text=') ', width=ancho, height=alto,bg='LightSteelBlue4',command=lambda:botones(')'))
    botonseno=Button(ventana, text='sin ', width=ancho, height=alto,bg='dark slate gray',command=Seno)
    botoncoseno=Button(ventana, text='cos ', width=ancho, height=alto, bg='dark slate gray', command=Cos)
    botontangente=Button(ventana, text='tan ', width=ancho, height=alto, bg='dark slate gray', command=Tan)


    #colocar botones
    Theme.grid(row= 1,column=0, padx=5, pady=5)
    botonE.grid(row=1, column=4, padx=5, pady=5)
    botonParentesis.grid(row=1, column=1, padx=5, pady=5)
    botonParentesisII.grid(row=1, column=3, padx=5, pady=5)
    botonRaiz.grid(row=2, column=0, padx=5, pady=5)
    botonIzquier.grid(row=2, column=1, padx=5, pady=5)
    botonExponente.grid(row=2, column=2, padx=5, pady=5)
    botonDerecha.grid(row=2, column=3, padx=5, pady=5)
    botonLog.grid(row=2, column=4, padx=5, pady=5)
    boton7.grid(row=3, column=0, padx=5, pady=5)
    boton8.grid(row=3, column=1, padx=5, pady=5)
    boton9.grid(row=3, column=2, padx=5, pady=5)
    botonDel.grid(row=3, column=3, padx=5, pady=5)
    botonAC.grid(row=3, column=4, padx=5, pady=5)
    boton4.grid(row=4, column=0, padx=5, pady=5)
    boton5.grid(row=4, column=1, padx=5, pady=5)
    boton6.grid(row=4, column=2, padx=5, pady=5)
    botonMulti.grid(row=4, column=3, padx=5, pady=5)
    botonDivision.grid(row=4, column=4, padx=5, pady=5)
    boton1.grid(row=5, column=0, padx=5, pady=5)
    boton2.grid(row=5, column=1, padx=5, pady=5)
    boton3.grid(row=5, column=2, padx=5, pady=5)
    botonMas.grid(row=5, column=3, padx=5, pady=5)
    botonMenos.grid(row=5, column=4, padx=5, pady=5)
    botonCero.grid(row=6, column=0, padx=5, pady=5)
    botonPunto.grid(row=6, column=1, padx=5, pady=5)
    botonPi.grid(row=6, column=2, padx=5, pady=5)
    botonPorcen.grid(row=6, column=3, padx=5, pady=5)
    botonIgual.grid(row=7, column=0, padx=5, pady=5)
    botonseno.grid(row=7, column=4, padx=5, pady=5)
    botoncoseno.grid(row=6, column=4, padx=5, pady=5)
    botontangente.grid(row=7, column=4, padx=5, pady=5)

#Funcion del boton theme, cuando la entrada es  azul retorna la funcion azul y si la entrada en verde retorna la funcion verde 
def cambioColor(t):
    if t=="azul":
        return azul
    elif t=="verde":
        return verde
    elif t=='Casio':
        return Casio
#Funcion de los botones al hacer click 
def botones(n):
    global A
    caja.insert(A, n)
    A=17
def botonesExp(n):
    global A
    caja.insert(A, n)
    A+=2
def FuncionE(n):
    global A
    caja.insert(A, n)
    A+=17
def  botonesLog(n):
    global A
    caja.insert(A, n)
    A+=4
def botonesInverso(n):
    global A
    caja.insert(A, n)
    A=0    
def AC():
    caja.delete(0, END)
def borrar():
    global A
    caja.delete(A-1,A)
    A-=1
def flechaIz():
    global A
    A-=1
def flechaDer():
    global A
    A+=1

def Seno():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    
    
    caja.delete(0, END)
    caja.insert (0,sin(float(operacion)))
    A=0
    
def Cos():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    
    
    caja.delete(0, END)
    caja.insert (0,cos(float(operacion)))
    A=0    

def Tan():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    
    
    caja.delete(0, END)
    caja.insert (0,tan(float(operacion)))
    A=0

def verificar_signos(operacion):
        for caracter in operacion:
            if caracter == "^":
                return True
        return False    

def igual():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    operacion= 'caja.insert'+'(0,'+texto+')'
    
    caja.delete(0, END)
    caja.insert (0,exec(operacion))
    A=0
    #caja.insert(0, resultado)

#variables para alto y ancho de los botones
alto=3
ancho=11

#Todos los  botones
botonE=Button(ventana, text="e^x",width=ancho, height=alto,bg='LightSteelBlue4', command=lambda:FuncionE(e))
Theme= Button(ventana, text="Theme",width=ancho, height=alto,bg='LightSteelBlue4', command=cambioColor("azul"))
botonCero=Button(ventana, text= "0", width=ancho, height=alto,bg='gray25',command=lambda:botones(0))
botonPunto=Button(ventana, text=".", width=ancho, height=alto,bg='gray25',command=lambda:botones(','))
botonPi=Button(ventana, text= "1/x", width=ancho, height=alto,bg='gray25',command=lambda:botonesInverso('**-1'))
botonPorcen=Button(ventana, text="%", width=ancho, height=alto,bg='gray25',command=lambda:botones('%'))
botonIgual=Button(ventana, text="=", width=ancho, height=alto,bg='gray25',command=igual)
boton1=Button(ventana, text="1", width=ancho, height=alto,bg='gray25',command=lambda:botones(1))
boton2=Button(ventana, text="2", width=ancho, height=alto,bg='gray25',command=lambda:botones(2))
boton3=Button(ventana, text="3", width=ancho, height=alto,bg='gray25',command=lambda:botones(3))
botonMas=Button(ventana, text="+", width=ancho, height=alto,bg='gray25',command=lambda:botones('+'))
botonMenos=Button(ventana, text="- ", width=ancho, height=alto,bg='gray25',command=lambda:botones('-'))
boton4=Button(ventana, text="4", width=ancho, height=alto,bg='gray25',command=lambda:botones(4))
boton5=Button(ventana, text="5", width=ancho, height=alto,bg='gray25',command=lambda:botones(5))
boton6=Button(ventana, text='6', width=ancho, height=alto,bg='gray25',command=lambda:botones(6))
botonMulti=Button(ventana, text="×", width=ancho, height=alto,bg='gray25',command=lambda:botones('*'))
botonDivision=Button(ventana, text='÷',width=ancho, height=alto,bg='gray25',command=lambda:botones('/'))
boton7=Button(ventana, text='7', width=ancho, height=alto,bg='gray25',command=lambda:botones(7))
boton8=Button(ventana, text='8', width=ancho, height=alto,bg='gray25',command=lambda:botones(8))
boton9=Button(ventana, text='9', width=ancho, height=alto,bg='gray25',command=lambda:botones(9))

botonDel=Button(ventana, text='Del', width=ancho, height=alto,bg='DeepPink4', command=borrar)
botonAC=Button(ventana, text='AC', width=ancho, height=alto,bg='DeepPink4', command=AC)
botonIzquier=Button(ventana,text='🢀', width=ancho, height=alto,bg='dark slate gray', command=lambda: flechaIz())
botonDerecha=Button(ventana, text='🢂', width=ancho, height=alto,bg='dark slate gray', command=lambda: flechaDer())

botonRaiz=Button(ventana, text='√ ', width=ancho, height=alto,bg='dark slate gray',command=lambda:botones('r'))
botonExponente=Button(ventana,text='Exp', width=ancho, height=alto,bg='dark slate gray',command=lambda:botonesExp('**'))
botonLog=Button(ventana, text='Log', width=ancho, height=alto,bg='dark slate gray',command=lambda:botonesLog('log'))
botonParentesis=Button(ventana, text='( ', width=ancho, height=alto,bg='LightSteelBlue4',command=lambda:botones('('))
botonParentesisII=Button(ventana, text=') ', width=ancho, height=alto,bg='LightSteelBlue4',command=lambda:botones(')'))
botonseno=Button(ventana, text='sin ', width=ancho, height=alto,bg='dark slate gray',command=Seno)
botoncoseno=Button(ventana, text='cos ', width=ancho, height=alto, bg='dark slate gray', command=Cos)
botontangente=Button(ventana, text='tan ', width=ancho, height=alto, bg='dark slate gray', command=Tan)

#colocar botones
botonE.grid(row=1, column=4, padx=5, pady=5)
Theme.grid(row= 1,column=0, padx=5, pady=5)
botonParentesis.grid(row=1, column=1, padx=5, pady=5)
botonParentesisII.grid(row=1, column=3, padx=5, pady=5)
botonRaiz.grid(row=2, column=0, padx=5, pady=5)
botonIzquier.grid(row=2, column=1, padx=5, pady=5)
botonExponente.grid(row=2, column=2, padx=5, pady=5)
botonDerecha.grid(row=2, column=3, padx=5, pady=5)
botonLog.grid(row=2, column=4, padx=5, pady=5)
boton7.grid(row=3, column=0, padx=5, pady=5)
boton8.grid(row=3, column=1, padx=5, pady=5)
boton9.grid(row=3, column=2, padx=5, pady=5)
botonDel.grid(row=3, column=3, padx=5, pady=5)
botonAC.grid(row=3, column=4, padx=5, pady=5)
boton4.grid(row=4, column=0, padx=5, pady=5)
boton5.grid(row=4, column=1, padx=5, pady=5)
boton6.grid(row=4, column=2, padx=5, pady=5)
botonMulti.grid(row=4, column=3, padx=5, pady=5)
botonDivision.grid(row=4, column=4, padx=5, pady=5)
boton1.grid(row=5, column=0, padx=5, pady=5)
boton2.grid(row=5, column=1, padx=5, pady=5)
boton3.grid(row=5, column=2, padx=5, pady=5)
botonMas.grid(row=5, column=3, padx=5, pady=5)
botonMenos.grid(row=5, column=4, padx=5, pady=5)
botonCero.grid(row=6, column=0, padx=5, pady=5)
botonPunto.grid(row=6, column=1, padx=5, pady=5)
botonPi.grid(row=6, column=2, padx=5, pady=5)
botonPorcen.grid(row=6, column=3, padx=5, pady=5)
botonIgual.grid(row=7, column=0, padx=5, pady=5)
botonseno.grid(row=7, column=3, padx=5, pady=5)
botoncoseno.grid(row=6, column=4, padx=5, pady=5)
botontangente.grid(row=7, column=4, padx=5, pady=5)




ventana.mainloop()