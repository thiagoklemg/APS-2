from tkinter import *
import time

#!!!!!!!!!!!!!!!!!! INICIO FUNÇÃO HOMEPAGE!!!!!!!!!!!!!!!!


def HomePage():
    #inicia a tela inicial dentro de uma função
    JanelaInicial = Tk()
    JanelaInicial.title("Reciclar")
    #funcao para a janela papel e suas utilidades

    #%%%%%%%%%%%%%%%%%%% JANELA PAPEL %%%%%%%%%%%%%%%%%% (INICIO)
    def Papel():
        JanelaPapel = Tk()
        JanelaPapel.title("Papel")
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaPapel.destroy()

        BotaoVoltar = Button(JanelaPapel, text="Voltar", width=10, command=Voltar)
        BotaoVoltar.place(x=300, y=650)
        #label para o usuario identificar se é reciclavel ou não
        LabelPapel = Label(JanelaPapel,  text='CONFIRME SE É RECICLAVEL: \n  Exemplos de reciclaveis : \n Caixa de papelão, jonais, revistas, \n folhas de caderno, caixas, envelopes, cartazes entre outros. \n Exemplos de não reciclaveis: \n Papel higienico, guardanapo, papel laminado, papel plastificado, \n papel carbono, fita crepe, fotografia e bituca de cigarro.')
        LabelPapel.pack()
        LabelPapel.place(x=300, y=200)
        #Janela para a localização (ultima janela)

        #@@@@@@@@@@@@@@@ JANELA CONFIRMAR (LOCALIZAÇÃO) @@@@@@@@@@@@ (INICIO)
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
        #@@@@@@@@@@@@@@@@@ JANELA CONFIRMAR (LOCALIZAÇÃO) @@@@@@@@@@@@ (FINAL)

        BotaoConfirmar = Button(JanelaPapel, text="É recliclavel!", width=10, command=Confirmar)
        BotaoConfirmar.place(x=300, y=550)
        JanelaPapel.geometry("700x770+0+0")
        JanelaPapel.mainloop()
    #%%%%%%%%%%%%%%%%%%% JANELA PAPEL %%%%%%%%%%%% (FINAL)


#TELA INICIAL
#*****************
    BotaoPapel = Button(JanelaInicial, text='Papel', width=10, command=Papel)
    BotaoPapel.place(x=300, y=10)
#*******************
#Funcao para a janela do vidro
    # %%%%%%%%%%%%%% JANELA VIDRO %%%%%%%%%%%%%%%%% (INICIO)

    def Vidro():
        JanelaVidro = Tk()
        JanelaVidro.title("Vidro")
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaVidro.destroy()
        # botão voltar e suas funcionalidades
        BotaoVoltar = Button(JanelaVidro, text="Voltar",width=10, command=Voltar)
        BotaoVoltar.place(x=300, y=650)  # locar do botao voltar
        #inicialização dos label informativo da janela vidro
        #lABEL que fica na janela de cada categoria identificando se é reciclavel ou nao
        LabelVidro = Label(JanelaVidro,  text='CONFIRME SE É RECICLAVEL: \n  Exemplos de reciclaveis : \n Exemplos de não reciclaveis: \n.')
        LabelVidro.pack()  # comando reservado para funcioonar o label
        LabelVidro.place(x=300, y=200)  # localização do label
        #Janela para a localização (ultima janela)

        #@@@@@@@@@@@@@@@@@@@ JANELA CONFIRMAR @@@@@@@@@@@@@@ (INICIO)
        def Confirmar():  # função para a janela caso o lixo seja reciclavel
            JanelaConfirmar = Tk()  # abertura da janela
            JanelaConfirmar.title('Localização')
            #botao para destruir a janela da confirmar (localização)

            def Voltar():
                return JanelaConfirmar.destroy()
            # botão voltar da janela confirmar(localizção)
            BotaoVoltar = Button(JanelaConfirmar, text="Voltar", width=10, command=Voltar)
            BotaoVoltar.place(x=300, y=650)
            # janela da localização e ses adereços
            JanelaConfirmar.geometry('700x770+0+0')
            JanelaConfirmar.mainloop()
            #@@@@@@@@@@@@@@@@@ JANELA CONFIRMAR @@@@@@@@@@@@@@@@@ (FINAL)

        # botao caso o lixo seja reciclavel e diecionamento para a janela confirmar (Localizção)
        BotaoConfirmar = Button(JanelaVidro, text="É recliclavel!", width=10, command=Confirmar)
        BotaoConfirmar.place(x=300, y=550)
        JanelaVidro.geometry("700x770+0+0")
        JanelaVidro.mainloop()  # finalização da janela vidro
    # %%%%%%%%%%%%%%%%%%% JANELA VIDRO %%%%%%%%%%%%%%%% (FINAL)
#TELA INICIAL
#*******************
    BotaoVidro = Button(JanelaInicial, text='Vidro', width=10, command=Vidro)
    BotaoVidro.place(x=300, y=110)
#********************

#Funcao para a janela do PLASTICO
    #%%%%%%%%%%%%%%%%%%% JANELA PLASTICO %%%%%%%%% (INICIO)
    def Plastico():
        JanelaPlastico = Tk()
        JanelaPlastico.title("Vidro")
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaPlastico.destroy()
        BotaoVoltar = Button(JanelaPlastico, text="Voltar",width=10, command=Voltar)
        BotaoVoltar.place(x=300, y=650)
        #lABEL que fica na janela de cada categoria identificando se é reciclavel ou nao
        LabelVidro = Label(JanelaPlastico,  text='CONFIRME SE É RECICLAVEL: \n  Exemplos de reciclaveis : \n Exemplos de não reciclaveis: \n.')
        LabelVidro.pack()  # comando reservado para funcioonar o label
        LabelVidro.place(x=300, y=200)  # localização do label

        #@@@@@@@@@@ JANELA CONFIRMAR (LOCALIZAÇÃO)@@@@@@@@@@@@@@@@@ (INICIO)

        def Confirmar():  # função para a janela caso o lixo seja reciclavel
            JanelaConfirmar = Tk()  # abertura da janela
            JanelaConfirmar.title('Localização')
            #botao para destruir a janela da confirmar (localização)

            def Voltar():
                return JanelaConfirmar.destroy()
            # botão voltar da janela confirmar(localizção)
            BotaoVoltar = Button(JanelaConfirmar, text="Voltar", width=10, command=Voltar)
            BotaoVoltar.place(x=300, y=650)
            # janela da localização e ses adereços
            JanelaConfirmar.geometry('700x770+0+0')
            JanelaConfirmar.mainloop()
        #@@@@@@@@@@@@@@@@ JANELA CONFIRMAR (LOCALIZAÇÃO) @@@@@@@@@@@ (FINAL)

        #botao caso o lixo seja reciclavel e diecionamento para a janela confirmar (Localizção)
        BotaoConfirmar = Button(JanelaPlastico, text="É recliclavel!", width=10, command=Confirmar)
        BotaoConfirmar.place(x=300, y=550)
        JanelaPlastico.geometry("700x770+0+0")
        JanelaPlastico.mainloop()
    #%%%%%%%%%%%%%%%%%%%% JANELA PLASTICO %%%%%%%%%%%% (FINAL)


#*******************TELA INICIAL*******************(BOTAO PLASTICO INICO)
    # Chamando a função plastico que esta acima e tem todas as funcionalidades necessárias
    BotaoPlastico = Button(JanelaInicial, text='Plástico', width=10, command=Plastico)
    BotaoPlastico.place(x=300, y=210)
#******************* TELA INICIAL **************** (BOTAO PLASTICO FINAL)

    #%%%%%%%%%%%%%%%% JANELA METAL %%%%%%%%%%% (INICIO)
    def Metal():
        JanelaMetal = Tk()
        JanelaMetal.title("Vidro")
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaMetal.destroy()
        BotaoVoltar = Button(JanelaMetal, text="Voltar",width=10, command=Voltar)
        BotaoVoltar.place(x=300, y=650)
        #lABEL que fica na janela de cada categoria identificando se é reciclavel ou nao
        LabelVidro = Label(JanelaMetal,  text='CONFIRME SE É RECICLAVEL: \n  Exemplos de reciclaveis : \n Exemplos de não reciclaveis: \n.')
        LabelVidro.pack()  # comando reservado para funcioonar o label
        LabelVidro.place(x=300, y=200)  # localização do label
        #Janela para a localização (ultima janela)

        #@@@@@@@@@@@@@@@@@@@ JANELA CONFIRMAR @@@@@@@@@@@@@@ (INICIO)
        def Confirmar():  # função para a janela caso o lixo seja reciclavel
            JanelaConfirmar = Tk()  # abertura da janela
            JanelaConfirmar.title('Localização')
            #botao para destruir a janela da confirmar (localização)

            def Voltar():
                return JanelaConfirmar.destroy()
            # botão voltar da janela confirmar(localizção)
            BotaoVoltar = Button(JanelaConfirmar, text="Voltar", width=10, command=Voltar)
            BotaoVoltar.place(x=300, y=650)
            # janela da localização e ses adereços
            JanelaConfirmar.geometry('700x770+0+0')
            JanelaConfirmar.mainloop()
            #@@@@@@@@@@@@@@@@@ JANELA CONFIRMAR @@@@@@@@@@@@@@@@@ (FINAL)

        # botao caso o lixo seja reciclavel e diecionamento para a janela confirmar (Localizção)
        BotaoConfirmar = Button(JanelaMetal, text="É recliclavel!", width=10, command=Confirmar)
        BotaoConfirmar.place(x=300, y=550)
        JanelaMetal.geometry("700x770+0+0")
        JanelaMetal.mainloop()
    #%%%%%%%%%%%% JANELA METAL %%%%%%%%%%%%%%%%% (FINAL)

#TELA INICIAL
#*******************
    # chama todas as funçoes declaras dentro da função metal
    BotaoMetal = Button(JanelaInicial, text='Metal', width=10, command=Metal)
    BotaoMetal.place(x=300, y=310)
#*******************

#Função para Destruir a TELA INICIAL
    def Sair():
        return JanelaInicial.destroy()

    #******************* TELA INICIAL *************** (BOTAO SAIR (INICIO))
    BotaoSair = Button(JanelaInicial, text='Sair', width=10, command=Sair)
    BotaoSair.place(x=500, y=310)
    #******************* TELA INICIAL *************** (BOTAO SAIR (FINAL))
    #Encerra os botões na tela principal

    #====================DECLARAÇÃO DO TAMANHO DA JANELA INICIAL===============
    JanelaInicial.geometry("700x770+0+0")
    JanelaInicial.mainloop()

#!!!!!!!!!!!!!!!!!! FIM FUNÇÃO HOMEPAGE !!!!!!!!!!!!!!!!


#!!!!!!!!!!!!!!!!! INICIO PROGRAMA PRINCIPAL !!!!!!!!!!!!!!
#---chama a funcão em que ta todo o programa---
HomePage()
