from tkinter import *
import math

menu_inicial = Tk()
menu_inicial.title("Calculadora")
menu_inicial.geometry("250x300") # Tamanho da janela
menu_inicial.resizable(False, False) # Impede que a janela seja redimensionada

#change color
menu_inicial.configure(background='grey')

#change icon

img = Image("photo", file="icon.png")
menu_inicial.tk.call('wm', 'iconphoto', menu_inicial._w, img)

# operaçoes

def porcent():
    n1 = visor.get()
    n1 = int(n1)
    n2 = n1 / 100
    visor.delete(0, END)
    visor.insert(0, n2)
    opt = "porcent"

def ln():
    n1 = visor.get()
    n1 = int(n1)
    n2 = math.log(n1)
    visor.delete(0, END)
    visor.insert(0, n2)
    opt = "ln"

def potencia():
    n1 = visor.get()
    n1 = int(n1)
    n2 = n1 ** 2
    visor.delete(0, END)
    visor.insert(0, n2)
    opt = "potencia"

def raiz():
    n1=visor.get()
    n1 = int(n1)
    n2 = math.sqrt(n1)
    visor.delete(0, END)
    visor.insert(0, n2)
    opt = "raiz"

def seno():
    n1 = visor.get()
    n1 = int(n1)
    n2 = math.sin(n1)
    visor.delete(0, END)
    visor.insert(0, n2)
    opt = "seno"

def cos():
    n1 = visor.get()
    n1 = int(n1)
    n2 = math.cos(n1)
    visor.delete(0, END)
    visor.insert(0, n2)
    opt = "cos"

def tan():
    n1 = visor.get()
    n1 = int(n1)
    n2 = math.tan(n1)
    visor.delete(0, END)
    visor.insert(0, n2)
    opt = "tan"

def fatorial():
    n1 = visor.get()
    n1 = int(n1)
    n2 = 1
    for i in range(1, n1 + 1):
        n2 = n2 * i
    visor.delete(0, END)
    visor.insert(0, n2)
    opt = "fatorial"

def mult():
    global p_n1, opt
    n1 = visor.get()
    p_n1 = float(n1)
    visor.delete(0,END)
    opt = 'mult'

def div():
    global p_n1, opt
    n1 = visor.get()
    p_n1 = float(n1)
    visor.delete(0, END)
    opt = "div"

def soma():
    global p_n1, opt
    n1 = visor.get()
    p_n1 = float(n1)
    visor.delete(0, END)
    opt = "soma"


def sub():
    global p_n1, opt
    n1 = visor.get()
    p_n1 = float(n1)
    visor.delete(0, END)
    opt = "sub"



def igual():
    n2 = visor.get()
    visor.delete(0, END)
    if opt == "soma":
        visor.insert(0, int(p_n1 + float(n2)))
    elif opt == "sub":
        visor.insert(0, int(p_n1 - float(n2)))
    elif opt == "fatorial":
        fatorial()
    elif opt == "mult":
        visor.insert(0, int(p_n1 * float(n2)))
    elif opt == "div":
        visor.insert(0, p_n1 / int(n2))
    elif opt == "seno":
        seno()
    elif opt == "cos":
        cos()
    elif opt == "tan":
        tan()
    elif opt == "raiz":
        raiz()
    elif opt == "potencia":
        potencia()
    elif opt == "ln":
        ln()
    elif opt == "porcent":
        porcent()

def ce():
    visor.delete(0, END)

# visor

visor = Entry(menu_inicial, width=30, borderwidth=5)    
visor.place(x=10, y=20)

# Botões operações

botao_igual = Button(menu_inicial, text="=",padx=10, pady=30, command=igual)
botao_igual.place(x=210, y=10)

botao_soma = Button(menu_inicial, text="+", padx=10, pady=10, command=soma)
botao_soma.place(x=210, y=100)

botao_sub = Button(menu_inicial, text="-", padx=11, pady=11, command=sub)
botao_sub.place(x=210, y=150)

botao_fat = Button(menu_inicial, text="!", padx=10, pady=10, command=fatorial)
botao_fat.place(x=210, y=200)

botao_mult = Button(menu_inicial, text="x", padx=10, pady=10, command=mult)
botao_mult.place(x=210, y=250)

botao_div = Button(menu_inicial, text="/", padx=10, pady=10, command=div)
botao_div.place(x=160, y=230)

botao_ce = Button(menu_inicial, text="CE", padx=80, pady=10, command=ce)
botao_ce.place(x=10, y=130)

botao_seno = Button(menu_inicial, text="sin", padx=10, pady=10, command=seno)
botao_seno.place(x=10, y=180)

botao_cos = Button(menu_inicial, text="cos", padx=10, pady=10, command=cos)
botao_cos.place(x=60, y=180)

botao_tan = Button(menu_inicial, text="tan", padx=10, pady=10, command=tan)
botao_tan.place(x=110, y=180)

botao_raiz = Button(menu_inicial, text="√", padx=10, pady=10, command=raiz)
botao_raiz.place(x=160, y=180)

botao_potencia = Button(menu_inicial, text="x²", padx=10, pady=10, command=potencia)
botao_potencia.place(x=10, y=230)

botao_ln = Button(menu_inicial, text="ln", padx=10, pady=10, command=ln)
botao_ln.place(x=60, y=230)

botao_porcent = Button(menu_inicial, text="%", padx=10, pady=10, command=porcent)
botao_porcent.place(x=110, y=230)

# Botõeo numeros

def botao_acao(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(0, str(atual) + str(numero))


botao_1 = Button(menu_inicial, text="1", padx=7, pady=7, command=lambda: botao_acao("1"), activebackground='green')
botao_1.place(x=10, y=50)

botao_2 = Button(menu_inicial, text="2", padx=7, pady=7, command=lambda: botao_acao("2"), activebackground='green')
botao_2.place(x=50, y=50)

botao_3 = Button(menu_inicial, text="3", padx=7, pady=7, command=lambda: botao_acao("3"), activebackground='green')
botao_3.place(x=90, y=50)

botao_4 = Button(menu_inicial, text="4", padx=7, pady=7, command=lambda: botao_acao("4"), activebackground='green')
botao_4.place(x=130, y=50)

botao_5 = Button(menu_inicial, text="5", padx=7, pady=7, command=lambda: botao_acao("5"), activebackground='green')
botao_5.place(x=170, y=50)

botao_6 = Button(menu_inicial, text="6", padx=7, pady=7, command=lambda: botao_acao("6"), activebackground='green')
botao_6.place(x=10, y=90)

botao_7 = Button(menu_inicial, text="7", padx=7, pady=7, command=lambda: botao_acao("7"), activebackground='green')
botao_7.place(x=50, y=90)

botao_8 = Button(menu_inicial, text="8", padx=7, pady=7, command=lambda: botao_acao("8"), activebackground='green')
botao_8.place(x=90, y=90)

botao_9 = Button(menu_inicial, text="9", padx=7, pady=7, command=lambda: botao_acao("9"), activebackground='green')
botao_9.place(x=130, y=90)

botao_0 = Button(menu_inicial, text="0", padx=7, pady=7, command=lambda: botao_acao("0"), activebackground='green')
botao_0.place(x=170, y=90)

menu_inicial.mainloop() # Inicia o loop do menu