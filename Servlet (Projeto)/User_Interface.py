#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from cliente import *
from os import sep

#Cores
bgColor1 =          '#1C1C1C'
btColor1 =          '#363636'
btColor2 =          '#131313'
bgSelColor =        '#EE4000'
ftSelColor =        '#FFFFFF'
ftColor1 =          '#EE4000'
msgColor1 =         '#00CD00'
msgColor2 =         '#CD0000'

#Fontes
defaultFont = ('Consolas', '14')
validateFont = ('Consolas', '18', 'bold')
msgFont = ('Consolas', '10', 'bold')

#Centraliza as janelas
def centerWindow(master, width=300, height=200):
    width = width #if master.winfo_width() <=100 else master.winfo_width() #Largura da janela
    height = height #if master.winfo_height() <=100 else master.winfo_height() #Altura da janela
    screenWidth = master.winfo_screenwidth() #Largura da tela
    screenHeight = master.winfo_screenheight() #Altura da tela
 
    posX = (screenWidth/2) - (width/2) #Posição X da janela
    posY = (screenHeight/2) - (height/2) #Pasição Y da janela
     
    master.geometry('%dx%d+%d+%d' % (width, height, posX, posY))
    master.iconbitmap('images%sicon.ico'%sep)
    master.resizable(width=False, height=False)
    master['bg'] = bgColor1
    master.focus_force()
    master.overrideredirect(True) #Retira as bordas da janela
    #master.attributes("-alpha",0.8) #Transparencia da janela

def charLimiter(text): #Limita o número de caracteres do StringVar()
    text.set(text.get()[0:12])


class Windows:
    def __init__(self):
        print('Bem-vindo ao SERVLET UFRPE.')
        self.__needSave = 0 #Variavel que verifica se houve alguma alteração realizada pelo ADM para questionar se ele deseja salvar quanto for deslogar.
        self.validateWindow()
         
    #Tela de Validação
    def validateWindow(self):
        self.__validateWindow = Tk()
        self.__validateWindow.title('-- SERVLET UFRPE -- (CHECKCODE)')
        centerWindow(self.__validateWindow, 700, 350)
        self.__validateWindow.bind('<Escape>', lambda event:self.quitConfirm(self.__validateWindow))
        self.__validateWindow.protocol('WM_DELETE_WINDOW', lambda :self.quitConfirm(self.__validateWindow))

        #Conteiners
        self.validateFrame1 = Frame(self.__validateWindow, bg='white')#bgColor1)
         
        #Packing Conteiners
        self.validateFrame1.pack(side=BOTTOM, fill=X)
        
        #Var Entry
        self.__entry1 = StringVar()
        self.__entry1.trace("w", lambda name, index, mode: charLimiter(self.__entry1)) #Chama função de limita caracteres sempre que algo for digitado.

        #Logo e Imagens
        self.validateImage1 = PhotoImage(file='images%slogo.png'%sep)
        self.validateImage2 = PhotoImage(file='images%sbtn.png'%sep)
        self.validateImage3 = PhotoImage(file='images%scode.png'%sep)
        self.validateCanvas = Canvas(self.__validateWindow, width=700, height=350, highlightthickness=0)
        self.validateCanvas.pack()
        
        self.validateCanvas.create_image(350, 175, image=self.validateImage1)
        
        #Entradas
        self.validateEntry1 = Entry(self.__validateWindow, width=12, font=validateFont[:2], textvariable=self.__entry1, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.validateEntry1.bind('<Return>', lambda event:self.sendCode(self.__entry1))
        self.validateEntry1.focus()

        #Etiquetas
        self.validateLabel1 = Label(self.__validateWindow, text='Code:', font=validateFont, bg="black", fg=ftColor1)
        self.validateLabel1.config(image=self.validateImage3)
        
        self.validateMsg = Label(self.validateFrame1, relief=SUNKEN, text='Insira o código de 12 dígitos', font=msgFont, bg=bgColor1, fg=msgColor1)
         
        #Botões
        self.validateButton1 = Button(self.__validateWindow, width=110, text='Ativar',
                                   command=lambda:self.sendCode(self.__entry1),
                                   font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1, bd=0)

        self.validateButton1['padx'] = 9
        self.validateButton1.bind('<Return>', lambda event:self.sendCode(self.__entry1))
        self.validateButton1.config(image=self.validateImage2)

        #Packs
        self.validateMsg.pack(fill=X)

        self.validateEntry1_window = self.validateCanvas.create_window(525, 53, anchor='nw', window=self.validateEntry1)
        self.validateLabel1_window = self.validateCanvas.create_window(430, 52, anchor='nw', window=self.validateLabel1)
        self.validateButton1_window = self.validateCanvas.create_window(573, 93, anchor='nw', window=self.validateButton1)
                
        self.__validateWindow.mainloop()


    #chama função que envia o codigo
    def sendCode(self, code):
        if len(str(code.get())) >= 12:
            print(code.get(),str(code.get()) is "")
            try:
                codigo = checacodCliente(str(code.get()))
                codigo = codigo.replace(r"\r\n", r" ")
                print(codigo)
                if(codigo == 'Código cadastrado com sucesso!'):
                    self.validateMsg['fg'] = msgColor1
                else:
                    self.validateMsg['fg'] = msgColor2
                self.validateMsg['text'] = codigo
            except Exception as e:
                self.validateMsg['fg'] = msgColor2
                self.validateMsg['text'] = e
        else:
            self.validateMsg['fg'] = msgColor2
            self.validateMsg['text'] = "O código deve conter 12 dígitos"

    #Sair do programa
    def quitConfirm(self, master):
        self.quitConfirmBox = messagebox.askquestion('Sair?','Realmente deseja sair?')
        if(self.quitConfirmBox == 'yes'):
            master.destroy()
        else:
            del self.quitConfirmBox



Windows()
