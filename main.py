from tkinter import *
from tkinter import messagebox
from playsound import playsound
import random
import time


def tempo_real():
    hora = time.strftime("%H:%M:%S")
    hora_atual.config(text=hora)
    hora_atual.after(1000, tempo_real)

def calcular():
    #pegando tempo total em segundos
    tempotot = int(hora.get())*3600 + int(minuto.get())*60 + int(segundo.get())

    while tempotot >- 1:
        #dividindo tempo para obter os dados novamente
        min,seg = (tempotot//60, tempotot%60)
        hor = 0

        if min > 60:
            hor, min = (min//60, min%60)

        #setando no tkinter
        segundo.set(seg)
        minuto.set(min)
        hora.set(hor)

        janela.update()
        time.sleep(1)

        if tempotot == 0:
            segundo.set("00")
            minuto.set("00")
            hora.set("00")

            try:
                musica = random.randint(1, 5)
                playsound(f'musics/{musica}.mp3')
            except:
                messagebox.showinfo(title= "Aviso de termino", message="O timer acabou")
                
        tempotot = tempotot - 1

janela = Tk()
janela.title("Foco no estudo")
janela.geometry("400x250")
janela.config(bg="black")
janela.resizable(width=False, height= False)

#titulo da janela
titulo = Label(janela, text="Vamos estudar", font=("System", "12"), bg="black", fg= "white")
titulo.place(x=155, y =0)

#hora atual
text_horaat = Label(janela, text="Hora Atual :", font=("System", "12"), bg="black", fg= "white")
text_horaat.place(x=100, y =40)

hora_atual = Label(janela, font=("System", "12"), bg="black", fg= "white")
hora_atual.place(x=240, y= 40)
tempo_real()

#definir variaveis
hora = StringVar()
minuto = StringVar()
segundo = StringVar()

#setar variaveis
hora.set("00")
minuto.set("00")
segundo.set("00")

#tkinter do tempo
entrada_hora = Entry(janela, textvariable= hora, width = 7, font=("System", "12"), bg="black", fg= "white")
entrada_hora.place(x = 80, y= 95)

entrada_minuto = Entry(janela, textvariable= minuto, width = 7, font=("System", "12"), bg="black", fg= "white")
entrada_minuto.place(x = 180, y= 95)

entrada_segundo = Entry(janela, textvariable= segundo, width = 7, font=("System", "12"), bg="black", fg= "white")
entrada_segundo.place(x = 280, y= 95)

#execucao do timer
btn = Button(janela, text= "Começar", command= calcular, font=("System", "12"), bg="black", fg= "white")
btn.place(x = 173, y = 200)

janela.mainloop()
