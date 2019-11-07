from tkinter import *
import time 

#Inicia programa tela principal
#==================================================================
jinicial = Tk()
jinicial.title("Reciclar")

#Chama o processo da tela do papel
def bt_papel():
    jinicial.destroy()
#Encerra o processo datela do papel

#Chama o processo de encerrar o programa
#==================================================================
def bt_sair():
    jinicial.destroy()
#==================================================================

#Cria os botoes na tela principal
#==================================================================
btpapel = Button(jinicial, text='Papel', width=10, command=bt_papel)
btpapel.place(x=300, y=10)
btvidro = Button(jinicial, text='Vidro', width=10)
btvidro.place(x=300, y=110)
btplastico = Button(jinicial, text='Plástico', width=10)
btplastico.place(x=300, y=210)
btmetal = Button(jinicial, text='Metal', width=10)
btmetal.place(x=300, y=310)
btSair = Button(jinicial, text='Sair', width=10, command=bt_sair)
btSair.place(x=500, y=310)
#Encerra os botões na tela principal
#==================================================================
jinicial.geometry("700x770+0+0")
jinicial.mainloop()
#Encerra a jinicial principal
#==================================================================
#Inicia programa tela papel
#==================================================================
jaapel = Tk()
jpapel.title("Papel")
jpapel.geometry("700x770+0+0")
jpapel.mainloop()