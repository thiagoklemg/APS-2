from tkinter import *
import time



def HomePage():
    #inicia a tela inicial dentro de uma função
    JanelaInicial = Tk()
    JanelaInicial.title("Reciclar")
    #funcao para a janela papel e suas utilidades

    def Papel():
        JanelaPapel = Tk()
        JanelaPapel.title("Papel")
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaPapel.destroy()
        
        BotaoVoltar = Button(JanelaPapel, text="Voltar", width=10, command=Voltar)
        BotaoVoltar.place(x=300, y=650)
        #label para o usuario identificar se é reciclavel ou não
        LabelPapel = Label(JanelaPapel,  text= 'CONFIRME SE É RECICLAVEL: \n  Exemplos de reciclaveis : \n Caixa de papelão, jonais, revistas, \n folhas de caderno, caixas, envelopes, cartazes entre outros. \n Exemplos de não reciclaveis: \n Papel higienico, guardanapo, papel laminado, papel plastificado, \n papel carbono, fita crepe, fotografia e bituca de cigarro.')
        LabelPapel.pack()
        LabelPapel.place(x=300, y=200)
       #Janela para a localização (ultima janela)
        def Confirmar():
            JanelaConfirmar = Tk()
            JanelaConfirmar.title('Localização')
            #botao para destruir a janela da confirmar (localização)         
            def Voltar():
                return JanelaConfirmar.destroy()
            BotaoVoltar = Button(JanelaConfirmar, text="Voltar", width=10, command=Voltar)
            BotaoVoltar.place(x=300, y=650)
            JanelaConfirmar.geometry('700x770+0+0')
            JanelaConfirmar.mainloop()
        
        JanelaPapel.geometry("700x770+0+0")
        BotaoConfirmar = Button (JanelaPapel, text = "É recliclavel!", width = 10, command = Confirmar)
        BotaoConfirmar.place (x=300, y= 550)
        JanelaPapel.mainloop()

#TELA INICIAL
#*****************
    BotaoPapel = Button(JanelaInicial, text='Papel', width=10, command=Papel)
    BotaoPapel.place(x=300, y=10)
#*******************
#Funcao para a janela do vidro

    def Vidro():
        JanelaVidro = Tk()
        JanelaVidro.title("Vidro")
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaVidro.destroy()
        BotaoVoltar = Button(JanelaVidro, text="Voltar", width=10, command=Voltar)
        BotaoVoltar.place(x=300, y=650)
        JanelaVidro.geometry("700x770+0+0")
        JanelaVidro.mainloop()

#TELA INICIAL
#*******************
    BotaoVidro = Button(JanelaInicial, text='Vidro', width=10, command=Vidro)
    BotaoVidro.place(x=300, y=110)
#********************

#Funcao para a janela do PLASTICO
    def Plastico():
        JanelaPlastico = Tk()
        JanelaPlastico.title("Vidro")
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaPlastico.destroy()
        BotaoVoltar = Button(JanelaPlastico, text="Voltar", width=10, command=Voltar)
        BotaoVoltar.place(x=300, y=650)
        JanelaPlastico.geometry("700x770+0+0")
        JanelaPlastico.mainloop()

#TELA INICIAL
#*******************
    BotaoPlastico = Button(JanelaInicial, text='Plástico', width=10, command=Plastico)
    BotaoPlastico.place(x=300, y=210)
#*******************

    def Metal():
        JanelaMetal = Tk()
        JanelaMetal.title("Vidro")
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaMetal.destroy()
        BotaoVoltar = Button(JanelaMetal, text="Voltar", width=10, command=Voltar)
        BotaoVoltar.place(x=300, y=650)
        JanelaMetal.geometry("700x770+0+0")
        JanelaMetal.mainloop()

#TELA INICIAL
#*******************
    BotaoMetal = Button(JanelaInicial, text='Metal', width=10, command=Metal)
    BotaoMetal.place(x=300, y=310)
#*******************

#Função para Destruir a TELA INICIAL
    def Sair():
        return JanelaInicial.destroy()

#TELA INICIAL
#*******************
    BotaoSair = Button(JanelaInicial, text='Sair', width=10, command=Sair)
    BotaoSair.place(x=500, y=310)
#*******************
#Encerra os botões na tela principal
#==================================================================
    JanelaInicial.geometry("700x770+0+0")
    JanelaInicial.mainloop()

#PROGRAMA PRINCIPAL
#---chama a funcão em que ta todo o programa---
HomePage()
