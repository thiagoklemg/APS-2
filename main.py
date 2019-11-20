from tkinter import *
import time
import localization
import webbrowser



def Voltar(janelaDestroy, janelaOpen, tipoDeLixo):
    if janelaOpen == "HomePage":
        HomePage(janelaDestroy)
    elif janelaOpen == "JanelaPapel":
        Papel(janelaDestroy)
    elif janelaOpen == "JanelaPlastico":
        Plastico(janelaDestroy)
    elif janelaOpen == "JanelaVidro":
        Vidro(janelaDestroy)
    elif janelaOpen == "JanelaMetal":
        Metal(janelaDestroy)
    elif janelaOpen == "JanelaOrganico":
        Organico(janelaDestroy)
    elif janelaOpen == "ConfirmarLixo":
        ConfirmarLixo(janelaDestroy, tipoDeLixo)
    elif janelaOpen == "nenhuma":
        janelaDestroy.destroy()

def VerRota(link):
    webbrowser.open_new(link)

# Janela da HomePage
def HomePage(janelaDestroy):
    # Cria a janela
    JanelaInicial = Tk()

    if janelaDestroy != 1: #Vê se é diferente de 1 porque na primeira vez quando inicia o progama não tem nenhuma janela para destruir
        # Destroi a janela anterior
        janelaDestroy.destroy()
        
    JanelaInicial.title("Reciclar")
    LabelInicial = Label(JanelaInicial,
                         text='Escolha, a baixo, qual tipo de lixo você quer descartar \n ou se deseja sair do programa!')
    LabelInicial.pack()
    LabelInicial.place(relx=0.5, rely=0.1, anchor=CENTER)
    LabelInicial.configure(font='Calibri, 18')

    #lambda é para conseguir passar parâmetro na função

    BotaoPapel = Button(JanelaInicial, text='Papel', bg='#008bff', width=15, height=1, font='Calibri, 14', command = lambda: Papel(JanelaInicial))
    BotaoPapel.place(relx=0.5, rely=0.3, anchor=CENTER)

    BotaoVidro = Button(JanelaInicial, text='Vidro', bg='#00ff5e', width=15, height=1, font='Calibri, 14',
                        command = lambda: Vidro(JanelaInicial))
    BotaoVidro.place(relx=0.5, rely=0.4, anchor=CENTER)

    BotaoPlastico = Button(JanelaInicial, text='Plástico', bg='red', width=15, height=1, font='Calibri, 14',
                            command = lambda: Plastico(JanelaInicial))
    BotaoPlastico.place(relx=0.5, rely=0.5, anchor=CENTER)

    BotaoMetal = Button(JanelaInicial, text='Metal', bg='yellow', width=15, height=1, font='Calibri, 14', 
                        command = lambda: Metal(JanelaInicial))
    BotaoMetal.place(relx=0.5, rely=0.6, anchor=CENTER)

    BotaoOrganico = Button(JanelaInicial, text='Organico', bg='brown', width=15, height=1, font='Calibri, 14',
                           command = lambda: Organico(JanelaInicial))
    BotaoOrganico.place(relx=0.5, rely=0.7, anchor=CENTER)

    BotaoSair = Button(JanelaInicial, text='Sair', bg='Light grey', width=15, height=1, font='Calibri, 14',
                       command = lambda: Voltar(JanelaInicial, "nenhuma", 0))
    BotaoSair.place(relx=0.5, rely=0.8, anchor=CENTER)

    JanelaInicial.geometry("700x770+0+0")
    JanelaInicial.mainloop()

def Papel(janelaDestroy):

    JanelaPapel = Tk()
    janelaDestroy.destroy()
    JanelaPapel.title("Papel")
    JanelaPapel.configure(background='#008bff')

    BotaoVoltar = Button(JanelaPapel, text="Voltar", bg='Light grey', width=15, height=1, font='Calibri, 14',
                            command = lambda: Voltar(JanelaPapel, "HomePage", 1))
    BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Label para o usuario identificar se é reciclavel ou não
    LabelPapel = Label(JanelaPapel, text='CONFIRME SE É RECICLÁVEL: \n \n \nExemplos de recicláveis : \n Caixa de papelão, jornais, revistas, \n folhas de caderno, caixas, envelopes, cartazes entre outros. \n \nExemplos de não recicláveis: \n Papel higiênico, guardanapo, papel laminado, papel plastificado, \n papel carbono, fita crepe, fotografia e bituca de cigarro.')
    LabelPapel.pack() # comando reservado para funcionar o label
    LabelPapel.place(relx=0.5, rely=0.2, anchor=CENTER) # localização do label
    LabelPapel.configure(background='#008bff', font='Calibri, 16') 

    BotaoConfirmar = Button(JanelaPapel, text="É recliclavel!", bg='Light grey', width=15, height=1,
                                font='Calibri, 14', command = lambda: ConfirmarLixo(JanelaPapel, 1))
    BotaoConfirmar.place(relx=0.5, rely=0.5, anchor=CENTER)

    JanelaPapel.geometry("700x770+0+0")
    JanelaPapel.mainloop()

def Plastico(janelaDestroy):

    JanelaPlastico = Tk()
    janelaDestroy.destroy()
    JanelaPlastico.title("Plástico")
    JanelaPlastico.configure(background='red')

    BotaoVoltar = Button(JanelaPlastico, text="Voltar", bg='Light grey', width=15, height=1, font='Calibri, 14',
                            command = lambda: Voltar(JanelaPlastico, "HomePage", 2))
    BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Label que fica na janela de cada categoria identificando se é reciclavel ou nao
    LabelPlastico = Label(JanelaPlastico,
                            text='CONFIRME SE É RECICLÁVEL: \n \n \nExemplos de recicláveis : \n Tampas, potes de alimentos (margarina), frascos, \n utilidades domésticas, embalagens de refrigerante. \n \nExemplos de não recicláveis: \n cabos de panela, tomadas, isopor, adesivos, \n espuma, teclados de computador, acrílicos.')
    LabelPlastico.pack()  # comando reservado para funcionar o label
    LabelPlastico.configure(background='red', font='Calibri, 16')
    LabelPlastico.place(relx=0.5, rely=0.2, anchor=CENTER)  # localização do label

    BotaoConfirmar = Button(JanelaPlastico, text="É recliclavel!", bg='Light grey', width=15, height=1,
                                font='Calibri, 14', command = lambda: ConfirmarLixo(JanelaPlastico, 2))
    BotaoConfirmar.place(relx=0.5, rely=0.5, anchor=CENTER)

    JanelaPlastico.geometry("700x770+0+0")
    JanelaPlastico.mainloop()

def Vidro(janelaDestroy):

    JanelaVidro = Tk()
    janelaDestroy.destroy()
    JanelaVidro.title("Vidro")
    JanelaVidro.configure(background='#00ff5e')

    BotaoVoltar = Button(JanelaVidro, text="Voltar", bg='Light grey', width=15, height=1, font='Calibri, 14',
                            command = lambda: Voltar(JanelaVidro, "HomePage", 3))
    BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Label que fica na janela de cada categoria identificando se é reciclavel ou nao
    LabelVidro = Label(JanelaVidro,
                           text='CONFIRME SE É RECICLÁVEL: \n \n \nExemplos de recicláveis : \n potes, vasos, perfumes, garrafas, copos, \n lâmpadas, vidros temperados planos. \n \nExemplos de não recicláveis: \n Vidro utilizados em utensílios de cozinha\n e em janelas, boxes e móveis.')
    LabelVidro.pack()  # comando reservado para funcionar o label
    LabelVidro.configure(background='#00ff5e', font='Calibri, 16')
    LabelVidro.place(relx=0.5, rely=0.2, anchor=CENTER)  # localização do label

    BotaoConfirmar = Button(JanelaVidro, text="É recliclavel!", bg='Light grey', width=15, height=1,
                                font='Calibri, 14', command = lambda: ConfirmarLixo(JanelaVidro, 3))
    BotaoConfirmar.place(relx=0.5, rely=0.5, anchor=CENTER)

    JanelaVidro.geometry("700x770+0+0")
    JanelaVidro.mainloop()

def Metal(janelaDestroy):

    JanelaMetal = Tk()
    janelaDestroy.destroy()
    JanelaMetal.title("Plástico")
    JanelaMetal.configure(background='yellow')

    BotaoVoltar = Button(JanelaMetal, text="Voltar", bg='Light grey', width=15, height=1, font='Calibri, 14',
                            command = lambda: Voltar(JanelaMetal, "HomePage", 4))
    BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Label que fica na janela de cada categoria identificando se é reciclavel ou nao
    LabelMetal = Label(JanelaMetal,
                           text='CONFIRME SE É RECICLÁVEL: \n \n \nExemplos de recicláveis : \n Latas de alumínio (refrigerante, cerveja, etc) e aço \n (latas de sardinha, molhos, óleo, etc.) \n \nExemplos de não recicláveis: \n Clipes, grampos, esponjas de aço, latas de tintas, \n latas de combustível e pilhas.')
    LabelMetal.pack()  # comando reservado para funcionar o label
    LabelMetal.configure(background='yellow', font='Calibri, 16')
    LabelMetal.place(relx=0.5, rely=0.2, anchor=CENTER)  # localização do label

    BotaoConfirmar = Button(JanelaMetal, text="É recliclavel!", bg='Light grey', width=15, height=1,
                                font='Calibri, 14', command = lambda: ConfirmarLixo(JanelaMetal, 4))
    BotaoConfirmar.place(relx=0.5, rely=0.5, anchor=CENTER)

    JanelaMetal.geometry("700x770+0+0")
    JanelaMetal.mainloop()

def Organico(janelaDestroy):

    JanelaOrganico = Tk()
    janelaDestroy.destroy()
    JanelaOrganico.title("Orgânico")
    JanelaOrganico.configure(background='brown')

    BotaoVoltar = Button(JanelaOrganico, text="Voltar", bg='Light grey', width=15, height=1, font='Calibri, 14',
                            command = lambda: Voltar(JanelaOrganico, "HomePage", 5))
    BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Label que fica na janela de cada categoria identificando se é reciclavel ou nao
    LabelOrganico = Label(JanelaOrganico,
                              text='CONFIRME SE É RECICLÁVEL: \n \n \nExemplos de recicláveis : \n tampas, potes de alimentos (margarina), frascos, \n utilidades domésticas, embalagens de refrigerante. \n \nExemplos de não recicláveis: \n cabos de panela, tomadas, isopor, adesivos, \n espuma, teclados de computador, acrílicos.')
    LabelOrganico.pack()  # comando reservado para funcionar o label
    LabelOrganico.configure(background='brown', font='Calibri, 16')
    LabelOrganico.place(relx=0.5, rely=0.2, anchor=CENTER)  # localização do label

    BotaoConfirmar = Button(JanelaOrganico, text="É recliclavel!", bg='Light grey', width=15, height=1,
                                font='Calibri, 14', command = lambda: ConfirmarLixo(JanelaOrganico, 5))
    BotaoConfirmar.place(relx=0.5, rely=0.5, anchor=CENTER)

    JanelaOrganico.geometry("700x770+0+0")
    JanelaOrganico.mainloop()

def ConfirmarLixo(janelaDestroy, tipoDeLixo):

    JanelaConfirmar = Tk()
    janelaDestroy.destroy()
    JanelaConfirmar.title('Confirmar')

    cor = "Light grey" #cor padrão
    janelaVoltar = ""
    if tipoDeLixo == 1: #caso papel
        cor="#008bff"
        janelaVoltar = "JanelaPapel"
    elif tipoDeLixo == 2: #caso plástico
        cor="red"
        janelaVoltar = "JanelaPlastico"
    elif tipoDeLixo == 3: #caso vidro
        cor="#00ff5e"
        janelaVoltar = "JanelaVidro"
    elif tipoDeLixo == 4: #caso metal
        cor="yellow"
        janelaVoltar = "JanelaMetal"
    elif tipoDeLixo == 5: #caso orgânico
        cor="brown"
        janelaVoltar = "JanelaOrganico"

    JanelaConfirmar.configure(background=cor)

    BotaoVoltar = Button(JanelaConfirmar, text="Voltar", bg='Light grey', width=15, height=1,
                            font='Calibri, 14', command = lambda: Voltar(JanelaConfirmar, janelaVoltar, tipoDeLixo))
    BotaoVoltar.place(relx=0.5, rely=0.8, anchor=CENTER)

    JanelaConfirmar.geometry('700x770+0+0')

    LabelDescription = Label(JanelaConfirmar, text="Quer descobrir um ponto de coleta \nmais perto de você?\n Preencha o formulário (Todos os campos são obrigatórios)")
    LabelDescription.pack()
    LabelDescription.place(relx=0.5, rely=0.1, anchor=CENTER)
    LabelDescription.configure(background=cor, font='Calibri 18')

    LabelStreet = Label(JanelaConfirmar, text="Rua:")
    LabelStreet.pack()
    LabelStreet.place(relx=0.5, rely=0.2, anchor=CENTER)
    LabelStreet.configure(background=cor, font='Calibri 18 bold')

    LabelStreet2 = Label(JanelaConfirmar, text="(Exemplo: Avenida Norte e Sul)")
    LabelStreet2.pack()
    LabelStreet2.place(relx=0.5, rely=0.25, anchor=CENTER)
    LabelStreet2.configure(background=cor, font='Calibri 12')

    InputStreet = Entry(JanelaConfirmar, font=('Ubuntu', 15))
    InputStreet.place(relx=0.5, rely=0.3, anchor=CENTER)


    LabelNumber = Label(JanelaConfirmar, text="Número:")
    LabelNumber.pack()
    LabelNumber.place(relx=0.5, rely=0.35, anchor=CENTER)
    LabelNumber.configure(background=cor, font='Calibri 18 bold')

    LabelNumber2 = Label(JanelaConfirmar, text="(Exemplo: 194)")
    LabelNumber2.pack()
    LabelNumber2.place(relx=0.5, rely=0.4, anchor=CENTER)
    LabelNumber2.configure(background=cor, font='Calibri 12')

    InputNumber = Entry(JanelaConfirmar, font=('Ubuntu', 15))
    InputNumber.place(relx=0.5, rely=0.45, anchor=CENTER)


    LabelCity = Label(JanelaConfirmar, text="Cidade:")
    LabelCity.pack()
    LabelCity.place(relx=0.5, rely=0.5, anchor=CENTER)
    LabelCity.configure(background=cor, font='Calibri 18 bold')

    LabelCity2 = Label(JanelaConfirmar, text="(Exemplo: Campinas)")
    LabelCity2.pack()
    LabelCity2.place(relx=0.5, rely=0.55, anchor=CENTER)
    LabelCity2.configure(background=cor, font='Calibri 12')

    InputCity = Entry(JanelaConfirmar, font=('Ubuntu', 15))
    InputCity.place(relx=0.5, rely=0.6, anchor=CENTER)

    BotaoLocalizacao = Button(JanelaConfirmar, text="Pesquisar", bg='Light grey', width=15, height=1,
                                    font='Calibri, 14', command = lambda: LocalProximo(JanelaConfirmar, InputStreet.get(), InputNumber.get(), InputCity.get(), tipoDeLixo, cor))
    BotaoLocalizacao.place(relx=0.5, rely=0.7, anchor=CENTER)

    JanelaConfirmar.geometry("700x770+0+0")
    JanelaConfirmar.mainloop()

def LocalProximo(janelaDestroy, street, number, city, tipoDeLixo, cor):
    if street != "" and number != "" and city != "":
        userAddress = localization.getUserAddress(street, number, city)
        result = localization.search(userAddress, tipoDeLixo)

        JanelaLocalProximo = Tk()
        janelaDestroy.destroy()
        JanelaLocalProximo.title('Endereço')
        JanelaLocalProximo.configure(background=cor)
        JanelaLocalProximo.geometry('700x770+0+0')

        LabelResultName = Label(JanelaLocalProximo,
                                    text=result[1])
        LabelResultName.pack()
        LabelResultName.place(relx=0.5, rely=0.1, anchor=CENTER)
        LabelResultName.configure(background=cor, font='Calibri 18 bold')

        auxAddress = "Endereço: " + result[0]
        LabelAddress = Label(JanelaLocalProximo,
                                text=auxAddress)
        LabelAddress.pack()
        LabelAddress.place(relx=0.5, rely=0.2, anchor=CENTER)
        LabelAddress.configure(background=cor, font='Calibri 18')

        BotaoIr = Button(JanelaLocalProximo, text="Ver rota!", bg='Light grey', width=15, height=1,
                            font='Calibri, 14', command = lambda: VerRota(result[2]))
        BotaoIr.place(relx=0.5, rely=0.6, anchor=CENTER)

        BotaoVoltar = Button(JanelaLocalProximo, text="Voltar", bg='Light grey', width=15, height=1,
                            font='Calibri, 14', command = lambda: Voltar(JanelaLocalProximo, "ConfirmarLixo", tipoDeLixo))
        BotaoVoltar.place(relx=0.5, rely=0.7, anchor=CENTER)
        JanelaLocalProximo.geometry('700x770+0+0')
        JanelaLocalProximo.mainloop()

HomePage(1)