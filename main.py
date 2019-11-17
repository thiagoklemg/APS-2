from tkinter import * 
import time

#!!!!!!!!!!!!!!!!!! INICIO FUNÇÃO HOMEPAGE!!!!!!!!!!!!!!!!


def HomePage():
    #inicia a tela inicial dentro de uma função
    JanelaInicial = Tk()
    JanelaInicial.title("Reciclar")
    LabelInicial = Label(JanelaInicial, text='Escolha, a baixo, qual tipo de lixo você quer descartar \n ou se deseja sair do programa')
    LabelInicial.pack()
    LabelInicial.place(relx=0.5, rely=0.1, anchor=CENTER)
    LabelInicial.configure(font='Calibri, 18')
    #funcao para a janela papel e suas utilidades

    #%%%%%%%%%%%%%%%%%%% JANELA PAPEL %%%%%%%%%%%%%%%%%% (INICIO)
    def Papel():
        JanelaPapel = Tk()
        JanelaPapel.title("Papel")
        JanelaPapel.configure(background='#008bff')        
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaPapel.destroy()

        BotaoVoltar = Button(JanelaPapel, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
        BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
        #label para o usuario identificar se é reciclavel ou não
        LabelPapel = Label(JanelaPapel,  text='CONFIRME SE É RECICLAVEL: \n \n  Exemplos de reciclaveis : \n Caixa de papelão, jonais, revistas, \n folhas de caderno, caixas, envelopes, cartazes entre outros. \n Exemplos de não reciclaveis: \n Papel higienico, guardanapo, papel laminado, papel plastificado, \n papel carbono, fita crepe, fotografia e bituca de cigarro.')
        LabelPapel.pack()
        LabelPapel.place(relx=0.5, rely=0.2, anchor=CENTER)
        LabelPapel.configure(background='#008bff', font='Calibri, 16')
        #Janela para a localização (ultima janela)

        #@@@@@@@@@@@@@@@ JANELA CONFIRMAR (LOCALIZAÇÃO) @@@@@@@@@@@@ (INICIO)
        def Confirmar():
            JanelaConfirmar = Tk()
            JanelaConfirmar.title('Confirmar')
            JanelaConfirmar.configure(background='#008bff')
            #botao para destruir a janela da confirmar (localização)

            def Voltar():
                return JanelaConfirmar.destroy()
            BotaoVoltar = Button(JanelaConfirmar, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
            BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
            JanelaConfirmar.geometry('700x770+0+0')
            
            def LocalProximo():
                JanelaLocalProximo = Tk()
                JanelaLocalProximo.title('Endereço')
                JanelaLocalProximo.configure(background='#008bff')
                JanelaLocalProximo.geometry('700x770+0+0')

                def Voltar():
                    return JanelaLocalProximo.destroy()
                BotaoVoltar = Button(JanelaLocalProximo, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
                BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
                JanelaLocalProximo.geometry('700x770+0+0')
                JanelaLocalProximo.mainloop()

            BotaoLocalizacao = Button(JanelaConfirmar, text="Pesquisar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=LocalProximo)
            BotaoLocalizacao.place(relx=0.5, rely=0.5, anchor=CENTER)
            JanelaConfirmar.geometry("700x770+0+0")
            JanelaConfirmar.mainloop()
        #@@@@@@@@@@@@@@@@@ JANELA CONFIRMAR (LOCALIZAÇÃO) @@@@@@@@@@@@ (FINAL)

        BotaoConfirmar = Button(JanelaPapel, text="É recliclavel!", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Confirmar)
        BotaoConfirmar.place(relx=0.5, rely=0.5, anchor=CENTER)
        JanelaPapel.geometry("700x770+0+0")
        JanelaPapel.mainloop()
    #%%%%%%%%%%%%%%%%%%% JANELA PAPEL %%%%%%%%%%%% (FINAL)


#TELA INICIAL
#*****************
    BotaoPapel = Button(JanelaInicial, text='Papel', bg='#008bff', width=15, height=1, font='Calibri, 14', command=Papel)
    BotaoPapel.place(relx=0.5, rely=0.3, anchor=CENTER)
#*******************
#Funcao para a janela do vidro
    # %%%%%%%%%%%%%% JANELA VIDRO %%%%%%%%%%%%%%%%% (INICIO)

    def Vidro():
        JanelaVidro = Tk()
        JanelaVidro.title("Vidro")
        JanelaVidro.configure(background='#00ff5e')
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaVidro.destroy()
        # botão voltar e suas funcionalidades
        BotaoVoltar = Button(JanelaVidro, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
        BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)  # locar do botao voltar
        #inicialização dos label informativo da janela vidro
        #lABEL que fica na janela de cada categoria identificando se é reciclavel ou nao
        LabelVidro = Label(JanelaVidro,  text='CONFIRME SE É RECICLAVEL: \n \n Exemplos de reciclaveis : \n spelhos, cristal, ampolas de medicamentos, \n cerâmicas e louças, lâmpadas, vidros temperados planos. \n Exemplos de não reciclaveis: \n vidros de automóveis, temperado e espelhos.')
        LabelVidro.pack()  # comando reservado para funcioonar o label
        LabelVidro.place(relx=0.5, rely=0.2, anchor=CENTER)  # localização do label
        LabelVidro.configure(background='#00ff5e', font='Calibri, 16')
        #Janela para a localização (ultima janela)

        #@@@@@@@@@@@@@@@@@@@ JANELA CONFIRMAR @@@@@@@@@@@@@@ (INICIO)
        def Confirmar():  # função para a janela caso o lixo seja reciclavel
            JanelaConfirmar = Tk()  # abertura da janela
            JanelaConfirmar.title('Confirmar')
            JanelaConfirmar.configure(background='#00ff5e')
            #botao para destruir a janela da confirmar (localização)

            def Voltar():
                return JanelaConfirmar.destroy()
            # botão voltar da janela confirmar(localizção)
            BotaoVoltar = Button(JanelaConfirmar, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
            BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
            # janela da localização e ses adereços
            JanelaConfirmar.geometry('700x770+0+0')
            
            def LocalProximo():
                JanelaLocalProximo = Tk()
                JanelaLocalProximo.title('Endereço')
                JanelaLocalProximo.configure(background='#00ff5e')
                JanelaLocalProximo.geometry('700x770+0+0')

                def Voltar():
                    return JanelaLocalProximo.destroy()
                BotaoVoltar = Button(JanelaLocalProximo, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
                BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
                JanelaLocalProximo.geometry('700x770+0+0')
                JanelaLocalProximo.mainloop()

            BotaoLocalizacao = Button(JanelaConfirmar, text="Pesquisar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=LocalProximo)
            BotaoLocalizacao.place(relx=0.5, rely=0.5, anchor=CENTER)
            JanelaConfirmar.geometry("700x770+0+0")
            JanelaConfirmar.mainloop()
            #@@@@@@@@@@@@@@@@@ JANELA CONFIRMAR @@@@@@@@@@@@@@@@@ (FINAL)

        # botao caso o lixo seja reciclavel e diecionamento para a janela confirmar (Localizção)
        BotaoConfirmar = Button(JanelaVidro, text="É recliclavel!", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Confirmar)
        BotaoConfirmar.place(relx=0.5, rely=0.5, anchor=CENTER)
        JanelaVidro.geometry("700x770+0+0")
        JanelaVidro.mainloop()  # finalização da janela vidro
    # %%%%%%%%%%%%%%%%%%% JANELA VIDRO %%%%%%%%%%%%%%%% (FINAL)
#TELA INICIAL
#*******************
    BotaoVidro = Button(JanelaInicial, text='Vidro', bg='#00ff5e',  width=15, height=1, font='Calibri, 14', command=Vidro)
    BotaoVidro.place(relx=0.5, rely=0.4, anchor=CENTER)
#********************

#Funcao para a janela do PLASTICO
    #%%%%%%%%%%%%%%%%%%% JANELA PLASTICO %%%%%%%%% (INICIO)
    def Plastico():
        JanelaPlastico = Tk()
        JanelaPlastico.title("Vidro")
        JanelaPlastico.configure(background='red')
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaPlastico.destroy()
        BotaoVoltar = Button(JanelaPlastico, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
        BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
        #lABEL que fica na janela de cada categoria identificando se é reciclavel ou nao
        LabelPlastico = Label(JanelaPlastico,  text='CONFIRME SE É RECICLAVEL: \n \n  Exemplos de reciclaveis : \n tampas, potes de alimentos (margarina), frascos, \n utilidades domésticas, embalagens de refrigerante. \n Exemplos de não reciclaveis: \n cabos de panela, tomadas, isopor, adesivos, \n espuma, teclados de computador, acrílicos.')
        LabelPlastico.pack()  # comando reservado para funcioonar o label
        LabelPlastico.configure(background='red', font='Calibri, 16')
        LabelPlastico.place(relx=0.5, rely=0.2, anchor=CENTER)  # localização do label

        #@@@@@@@@@@ JANELA CONFIRMAR (LOCALIZAÇÃO)@@@@@@@@@@@@@@@@@ (INICIO)

        def Confirmar():  # função para a janela caso o lixo seja reciclavel
            JanelaConfirmar = Tk()  # abertura da janela
            JanelaConfirmar.title('Confirmar')
            JanelaConfirmar.configure(background='red')
            #botao para destruir a janela da confirmar (localização)

            def Voltar():
                return JanelaConfirmar.destroy()
            # botão voltar da janela confirmar(localizção)
            BotaoVoltar = Button(JanelaConfirmar, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
            BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
            # janela da localização e ses adereços
            JanelaConfirmar.geometry('700x770+0+0')
            
            def LocalProximo():
                JanelaLocalProximo = Tk()
                JanelaLocalProximo.title('Endereço')
                JanelaLocalProximo.configure(background='red')
                JanelaLocalProximo.geometry('700x770+0+0')

                def Voltar():
                    return JanelaLocalProximo.destroy()
                BotaoVoltar = Button(JanelaLocalProximo, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
                BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
                JanelaLocalProximo.geometry('700x770+0+0')
                JanelaLocalProximo.mainloop()

            BotaoLocalizacao = Button(JanelaConfirmar, text="Pesquisar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=LocalProximo)
            BotaoLocalizacao.place(relx=0.5, rely=0.5, anchor=CENTER)
            JanelaConfirmar.geometry("700x770+0+0")
            JanelaConfirmar.mainloop()
        #@@@@@@@@@@@@@@@@ JANELA CONFIRMAR (LOCALIZAÇÃO) @@@@@@@@@@@ (FINAL)

        #botao caso o lixo seja reciclavel e diecionamento para a janela confirmar (Localizção)
        BotaoConfirmar = Button(JanelaPlastico, text="É recliclavel!", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Confirmar)
        BotaoConfirmar.place(relx=0.5, rely=0.5, anchor=CENTER)
        JanelaPlastico.geometry("700x770+0+0")
        JanelaPlastico.mainloop()
    #%%%%%%%%%%%%%%%%%%%% JANELA PLASTICO %%%%%%%%%%%% (FINAL)


#*******************TELA INICIAL*******************(BOTAO PLASTICO INICO)
    # Chamando a função plastico que esta acima e tem todas as funcionalidades necessárias
    BotaoPlastico = Button(JanelaInicial, text='Plástico', bg='red', width=15, height=1, font='Calibri, 14',command=Plastico)
    BotaoPlastico.place(relx=0.5, rely=0.5, anchor=CENTER)
#******************* TELA INICIAL **************** (BOTAO PLASTICO FINAL)

    #%%%%%%%%%%%%%%%% JANELA METAL %%%%%%%%%%% (INICIO)
    def Metal():
        JanelaMetal = Tk()
        JanelaMetal.title("Vidro")
        JanelaMetal.configure(background='yellow')
        #função para o botão voltar funcionar

        def Voltar():
            return JanelaMetal.destroy()
        BotaoVoltar = Button(JanelaMetal, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
        BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
        #lABEL que fica na janela de cada categoria identificando se é reciclavel ou nao
        LabelMetal = Label(JanelaMetal,  text='CONFIRME SE É RECICLAVEL: \n \n  Exemplos de reciclaveis : \n Latas de alumínio (refrigerante, cerveja, etc) e aço \n (latas de sardinha, molhos, óleo, etc. \n Exemplos de não reciclaveis: \n clipes, grampos, esponjas de aço, latas de tintas, \n latas de combustível e pilhas.')
        LabelMetal.pack()  # comando reservado para funcioonar o label
        LabelMetal.configure(background='yellow', font='Calibri, 16')
        LabelMetal.place(relx=0.5, rely=0.2, anchor=CENTER)  # localização do label
        #Janela para a localização (ultima janela)

        #@@@@@@@@@@@@@@@@@@@ JANELA CONFIRMAR @@@@@@@@@@@@@@ (INICIO)
        def Confirmar():  # função para a janela caso o lixo seja reciclavel
            JanelaConfirmar = Tk()  # abertura da janela
            JanelaConfirmar.title('Confirmar')
            JanelaConfirmar.configure(background='yellow')
            #botao para destruir a janela da confirmar (localização)

            def Voltar():
                return JanelaConfirmar.destroy()
            # botão voltar da janela confirmar(localizção)
            BotaoVoltar = Button(JanelaConfirmar, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
            BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
            # janela da localização e ses adereços
            JanelaConfirmar.geometry('700x770+0+0')
            
            def LocalProximo():
                JanelaLocalProximo = Tk()
                JanelaLocalProximo.title('Endereço')
                JanelaLocalProximo.configure(background='yellow')
                JanelaLocalProximo.geometry('700x770+0+0')

                def Voltar():
                    return JanelaLocalProximo.destroy()
                BotaoVoltar = Button(JanelaLocalProximo, text="Voltar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Voltar)
                BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
                JanelaLocalProximo.geometry('700x770+0+0')
                JanelaLocalProximo.mainloop()

            BotaoLocalizacao = Button(JanelaConfirmar, text="Pesquisar", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=LocalProximo)
            BotaoLocalizacao.place(relx=0.5, rely=0.5, anchor=CENTER)
            JanelaConfirmar.geometry("700x770+0+0")
            JanelaConfirmar.mainloop()
            #@@@@@@@@@@@@@@@@@ JANELA CONFIRMAR @@@@@@@@@@@@@@@@@ (FINAL)

        # botao caso o lixo seja reciclavel e diecionamento para a janela confirmar (Localizção)
        BotaoConfirmar = Button(JanelaMetal, text="É recliclavel!", bg='Light grey',  width=15, height=1, font='Calibri, 14', command=Confirmar)
        BotaoConfirmar.place(relx=0.5, rely=0.5, anchor=CENTER)
        JanelaMetal.geometry("700x770+0+0")
        JanelaMetal.mainloop()
    #%%%%%%%%%%%% JANELA METAL %%%%%%%%%%%%%%%%% (FINAL)

#TELA INICIAL
#*******************
    # chama todas as funçoes declaras dentro da função metal
    BotaoMetal = Button(JanelaInicial, text='Metal', bg='yellow',  width=15, height=1, font='Calibri, 14', command=Metal)
    BotaoMetal.place(relx=0.5, rely=0.6, anchor=CENTER)
#*******************

#Função para Destruir a TELA INICIAL
    def Sair():
        return JanelaInicial.destroy()

    #******************* TELA INICIAL *************** (BOTAO SAIR (INICIO))
    BotaoSair = Button(JanelaInicial, text='Sair', bg='Light grey',  width=15, height=1, font='Calibri, 14',command=Sair)
    BotaoSair.place(relx=0.5, rely=0.8, anchor=CENTER)
    #******************* TELA INICIAL *************** (BOTAO SAIR (FINAL))
    #Encerra os botões na tela principal

    #====================DECLARAÇÃO DO TAMANHO DA JANELA INICIAL===============
    JanelaInicial.geometry("700x770+0+0")
    JanelaInicial.mainloop()

#!!!!!!!!!!!!!!!!!! FIM FUNÇÃO HOMEPAGE !!!!!!!!!!!!!!!!


#!!!!!!!!!!!!!!!!! INICIO PROGRAMA PRINCIPAL !!!!!!!!!!!!!!
#---chama a funcão em que ta todo o programa---
HomePage()
