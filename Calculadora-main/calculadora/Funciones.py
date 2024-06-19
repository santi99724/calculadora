# Importamos Las librerias y definimos las variables globales:
import Librerias as Lib
from tkinter import*
import math as MT

A=0

def Config_Init():
    datos_encontrados = {}
    try: 
        with open("Config.txt",'r') as Archivo:
            # Leer todas las líneas del archivo
            lineas = Archivo.readlines()
            
            # Iterar sobre cada línea
            for linea in lineas:
                # Dividir la línea en dos partes usando el signo "=" como separador
                partes = linea.split("=")
                # La primera parte será la clave y la segunda parte será el valor
                clave = partes[0].strip()
                valor = partes[1].strip()
                # Almacenar la clave y el valor en el diccionario datos_encontrados
                datos_encontrados[clave] = valor
    except FileNotFoundError:
        with open("Config.txt","w+") as Archivo:
            Archivo.writelines(Lib.Base_Config)
    return datos_encontrados

def Escribir(Numero):
    nueva_configuracion = f"Theme={Numero}\n"
    print(Numero)
    try:
        # Leer el archivo y modificar la configuración del tema
        with open("Config.txt", "r") as archivo:
            lineas = archivo.readlines()

        for i, linea in enumerate(lineas):
            if linea.startswith("Theme="):
                lineas[i] = nueva_configuracion
                break

        # Escribir las nuevas líneas en el archivo
        with open("Config.txt", "w") as archivo:
            archivo.writelines(lineas)
            
    except FileNotFoundError:
        pass

    
    

             

#Funcion de los botones al hacer click 
def CambiarColor(Color):
    if Color != 2:
        Color=Color+1
    else:
        Color=0
        
    Escribir(Color)
    Cerrar_Ventana()
    Open_Calc(Color, Ans, Alto, Ancho)

def botones(n):
   global A
   caja.insert(A, n)
   A+=1
def botonesExp(n):
    global A
    caja.insert(A, n)
    A+=2
def FuncionE(n):
    global A
    caja.insert(A, n)
    A+=17
def Funcionpy(n):
    global A
    caja.insert(A, n)
    A=MT.pi
    A+=17
    return A
def  botonesLog(n):
    global A
    caja.insert(A, n)
    A+=4
def botonesInverso(n):
    global A
    caja.insert(A, n)
    A=0    
def AC():
    caja.delete(0, END) # Limpiar cualquier contenido en la caja de entrada
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
def acosh():
 global A
 operacion=caja.get()

 texto='('
 texto+=operacion
 texto+=')'
 caja.delete(0,END) #borra lo de la caja de entrada

 caja.insert(0,MT.acosh(float(operacion)))  # Insertar el valor de cosh en la caja de entrada

 A+=17

def asinh():
 global A
 operacion=caja.get()

 texto='('
 texto+=operacion
 texto+=')'
 caja.delete(0,END) #borra lo de la caja de entrada

 caja.insert(0,MT.asinh(float(operacion)))  # Insertar el valor de cosh en la caja de entrada

 A+=17

def Acos():
 global A
 operacion=caja.get()

 texto='('
 texto+=operacion
 texto+=')'
 caja.delete(0,END) #borra lo de la caja de entrada

 caja.insert(0,MT.acos(float(operacion))) 

 A-=1

def Asin():
 global A
 operacion=caja.get()

 texto='('
 texto+=operacion
 texto+=')'
 caja.delete(0,END) #borra lo de la caja de entrada

 caja.insert(0,MT.asin(float(operacion)))

 A+=17

def Sinh():
 global A
 operacion=caja.get()

 texto='('
 texto+=operacion
 texto+=')'
 caja.delete(0,END) #borra lo de la caja de entrada

 caja.insert(0,MT.sinh(float(operacion)))

 A+=17
def Cosh():
 global A
 operacion=caja.get()

 texto='('
 texto+=operacion
 texto+=')'
 caja.delete(0,END) #borra lo de la caja de entrada

 caja.insert(0,MT.cosh(float(operacion)))

 A+=17

def Tanh():
 global A
 operacion=caja.get()

 texto='('
 texto+=operacion
 texto+=')'
 caja.delete(0,END) #borra lo de la caja de entrada

 caja.insert(0,MT.tanh(float(operacion)))

 A+=17

def Atan():
 global A
 operacion=caja.get()

 texto='('
 texto+=operacion
 texto+=')'
 caja.delete(0,END) #borra lo de la caja de entrada

 caja.insert(0,MT.atan(float(operacion)))

 A+=17
 



def Seno():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    
    
    caja.delete(0, END)
    caja.insert (0,MT.sin(float(operacion)))
    A+=17
    
def Cos():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    
    
    caja.delete(0, END)
    caja.insert (0,MT.cos(float(operacion)))
    A+=17   



def Tan():
    global A
    operacion= caja.get()
    
    texto='('
    texto+=operacion
    texto+=')'
    
    
    caja.delete(0, END)
    caja.insert (0,MT.tan(float(operacion)))
    A+=17

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
    A+=1



def Open_Calc(theme, Ans, Alto, Ancho):
    # Calculadora:
    global ventana
    ventana= Tk()
    ventana.title("Calculadora")
    ventana.config(bg='grey63')
    #caja de texto
    global caja
    caja=Entry(ventana, font=('System 20'),bg='dark olive green')
    caja.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

    botonE=Button(ventana, text="e^x",width=Ancho, height=Alto,bg=Lib.Theme[theme][3], command=lambda:FuncionE("e"))
    ThemeButton= Button(ventana, text="Theme",width=Ancho, height=Alto,bg=Lib.Theme[theme][3],command=lambda:CambiarColor(theme))
    botonCero=Button(ventana, text= "0", width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(0))
    botonPunto=Button(ventana, text=".", width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(','))
    botonPi=Button(ventana, text= "1/x", width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botonesInverso('**-1'))
    botonPorcen=Button(ventana, text="%", width=Ancho, height=Alto,bg=Lib.Theme[theme][3],command=lambda:botones('%'))
    botonIgual=Button(ventana, text="=", width=Ancho, height=Alto,bg=Lib.Theme[theme][2],command=igual)
    boton1=Button(ventana, text="1", width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(1))
    boton2=Button(ventana, text="2", width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(2))
    boton3=Button(ventana, text="3", width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(3))
    botonMas=Button(ventana, text="+", width=Ancho, height=Alto,bg=Lib.Theme[theme][3],command=lambda:botones('+'))
    botonMenos=Button(ventana, text="- ", width=Ancho, height=Alto,bg=Lib.Theme[theme][3],command=lambda:botones('-'))
    boton4=Button(ventana, text="4", width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(4))
    boton5=Button(ventana, text="5", width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(5))
    boton6=Button(ventana, text='6', width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(6))
    botonMulti=Button(ventana, text="×", width=Ancho, height=Alto,bg=Lib.Theme[theme][3],command=lambda:botones('*'))
    botonDivision=Button(ventana, text='÷',width=Ancho, height=Alto,bg=Lib.Theme[theme][3],command=lambda:botones('/'))
    boton7=Button(ventana, text='7', width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(7))
    boton8=Button(ventana, text='8', width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(8))
    boton9=Button(ventana, text='9', width=Ancho, height=Alto,bg=Lib.Theme[theme][1],command=lambda:botones(9))

    botonDel=Button(ventana, text='Del', width=Ancho, height=Alto,bg=Lib.Theme[theme][2], command=borrar)
    botonAC=Button(ventana, text='AC', width=Ancho, height=Alto,bg=Lib.Theme[theme][2], command=AC)
    botonIzquier=Button(ventana,text='🢀', width=Ancho, height=Alto,bg=Lib.Theme[theme][4], command=lambda: flechaIz())
    botonDerecha=Button(ventana, text='🢂', width=Ancho, height=Alto,bg=Lib.Theme[theme][4], command=lambda: flechaDer())

    botonRaiz=Button(ventana, text='√ ', width=Ancho, height=Alto,bg=Lib.Theme[theme][4],command=lambda:botones('r'))
    botonExponente=Button(ventana,text='Exp', width=Ancho, height=Alto,bg=Lib.Theme[theme][4],command=lambda:botonesExp('**'))
    botonLog=Button(ventana, text='Log', width=Ancho, height=Alto,bg=Lib.Theme[theme][4],command=lambda:botonesLog('log'))
    botonParentesis=Button(ventana, text='( ', width=Ancho, height=Alto,bg=Lib.Theme[theme][3],command=lambda:botones('('))
    botonParentesisII=Button(ventana, text=') ', width=Ancho, height=Alto,bg=Lib.Theme[theme][3],command=lambda:botones(')'))
    botonseno=Button(ventana, text='sin ', width=Ancho, height=Alto,bg=Lib.Theme[theme][4],command=Seno)
    botoncoseno=Button(ventana, text='cos ', width=Ancho, height=Alto, bg=Lib.Theme[theme][4], command=Cos)
    botontangente=Button(ventana, text='tan ', width=Ancho, height=Alto, bg=Lib.Theme[theme][4], command=Tan)
    botonacosh=Button(ventana, text= "acosh" , width=Ancho, height=Alto, bg=Lib.Theme[theme][4], command=acosh)
    botonasinh=Button(ventana, text= "asinh" , width=Ancho, height=Alto, bg=Lib.Theme[theme][4], command=asinh)
    botonasin=Button(ventana, text= "asin" , width=Ancho, height=Alto, bg=Lib.Theme[theme][4], command=Asin)
    botonacos=Button(ventana, text= "acos" , width=Ancho, height=Alto, bg=Lib.Theme[theme][4], command=Acos)
    botonatan=Button(ventana, text= "atan" , width=Ancho, height=Alto, bg=Lib.Theme[theme][4], command=Atan)
    botonpy=Button(ventana, text= "π" , width=Ancho, height=Alto, bg=Lib.Theme[theme][3], command=Funcionpy)
    botonsinh=Button(ventana, text= "sinh" , width=Ancho, height=Alto, bg=Lib.Theme[theme][4], command=Sinh)
    botontanh=Button(ventana, text= "tanh" , width=Ancho, height=Alto, bg=Lib.Theme[theme][4], command=Tanh)
    botoncosh=Button(ventana, text= "cosh" , width=Ancho, height=Alto, bg=Lib.Theme[theme][4], command=Cosh)


    botonE.grid(row=1, column=4, padx=5, pady=5)
    ThemeButton.grid(row= 1,column=0, padx=5, pady=5)
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
    botonIgual.grid(row=9, column=0,columnspan=5, padx=5,pady=5)
    botonseno.grid(row=7,  column=3, padx=5, pady=5)
    botoncoseno.grid(row=7, column=0, padx=5, pady=5)
    botontangente.grid(row=7, column=4, padx=5, pady=5)
    botonacosh.grid(row=7, column=2, padx=5, pady=5)
    botonasinh.grid(row=7, column=1, padx=5, pady=5)
    botonasin.grid(row=8, column=1, padx=5, pady=5)
    botonacos.grid(row=8, column=0, padx=5, pady=5)
    botonatan.grid(row=8, column=2, padx=5, pady=5)
    botonpy.grid(row=1, column=2, padx=5, pady=5)
    botonsinh.grid(row=8, column=4, padx=5, pady=5)
    botoncosh.grid(row=8, column=3, padx=5, pady=5)
    botontanh.grid(row=6, column=4, padx=5, pady=5)







    ventana.mainloop()

def Cerrar_Ventana():
    ventana.destroy()



# Abrimos la configuracion de software:
def TomarDatos():
    archivo=Config_Init()
    theme=int(archivo['Theme'])
    ans=int(archivo['Ans'])
    alto=int(archivo['Alto'])
    ancho=int(archivo['Ancho'])
    return theme, ans, alto, ancho

Theme, Ans, Alto, Ancho = TomarDatos()