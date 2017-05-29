from Bibliotec_dynamic_table import *
from tkinter import *
from tkinter import messagebox
from Variables import *
from New_RB_Tree import *
from Authenticator import *
from Autocomplete import Autocomplete
#import messagebox
import os

#Centraliza as janelas
def centerWindow(master, width=300, height=200):
    width = width if master.winfo_width() <=100 else master.winfo_width() #Largura da janela
    height = height if master.winfo_height() <=100 else master.winfo_height() #Altura da janela
    screenWidth = master.winfo_screenwidth() #Largura da tela
    screenHeight = master.winfo_screenheight() #Altura da tela

    posX = (screenWidth/2) - (width/2) #Posição X da janela
    posY = (screenHeight/2) - (height/2) #Pasição Y da janela
    
    master.geometry('%dx%d+%d+%d' % (width, height, posX, posY))
    master.iconbitmap('Image%sicon.ico'%(os.sep))
    master.resizable(width=False, height=False)
    master['bg'] = bgColor1
    master.focus_force()

class Windows:
    def __init__(self):
        print('Bem-vindo a biblioteca da UFRPE.')
        self.__needSave = 0 #Variavel que verifica se houve alguma alteração realizada pelo ADM para questionar se ele deseja salvar quanto for deslogar.
        self.loginWindow()
        
    #Tela de Login
    def loginWindow(self, master=None):
        #Migrando CPF e Senha da tela de Cadastro
        if(master != None):
            try:
                self.__CPF, self.__password = self.__entry1.get(), self.__entry2.get()
            except:
                pass
            master.destroy()
        self.__loginWindow = Tk()
        self.__loginWindow.title('-- Biblioteca UFRPE -- (Login)')
        centerWindow(self.__loginWindow, 300, 500)
        self.__loginWindow.bind('<Escape>', lambda event:self.quitConfirm(self.__loginWindow))
        self.__loginWindow.protocol('WM_DELETE_WINDOW', lambda :self.quitConfirm(self.__loginWindow))
        
        #Conteiners
        self.loginFrame1 = Frame(self.__loginWindow, bg=bgColor1)
        self.loginFrame2 = Frame(self.__loginWindow, bg=bgColor1)
        self.loginFrame3 = Frame(self.__loginWindow, bg=bgColor1)
        self.loginFrame4 = Frame(self.__loginWindow, bg=bgColor1)
        self.loginFrame5 = Frame(self.__loginWindow, bg=bgColor1)
        self.loginFrame6 = Frame(self.__loginWindow, bg=bgColor1, height=30)
        self.loginFrame7 = Frame(self.loginFrame4, bg=bgColor1, width=23) #Espaço entre os self.loginButton1 e self.loginButton2
        self.loginFrame8 = Frame(self.__loginWindow, bg='white')#bgColor1)
        self.loginFrame1['pady'] = 40
        self.loginFrame4['pady'] = 10
        
        #Packing Conteiners
        self.loginFrame1.pack()
        self.loginFrame6.pack()
        self.loginFrame2.pack()
        self.loginFrame3.pack()
        self.loginFrame4.pack()#(fill=X)
        self.loginFrame5.pack()
        self.loginFrame8.pack(side=BOTTOM, fill=X)

        self.__entry1 = StringVar()
        #Carregando CPF da tela de Cadastro
        if(master != None):
            try:
                self.__entry1.set(self.__CPF)
            except:
                pass
        self.__entry2 = StringVar()
        #Carregando Senha da tela de Cadastro
        if(master != None):
            try:
                self.__entry2.set(self.__password)
            except:
                pass
        self.__loginMsg = ''
        
        #Logo
        self.loginImage = PhotoImage(file='Image%slogo.png'%(os.sep))
        
        #Entradas
        self.loginEntry1 = Entry(self.loginFrame2, width=23, textvariable=self.__entry1, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.loginEntry2 = Entry(self.loginFrame3, width=23, show='●', textvariable=self.__entry2, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.loginEntry2.bind('<Return>', lambda event:self.loginAuthentication(self.__loginWindow))
        

        #Etiquetas
        self.loginLabel1 = Label(self.loginFrame1, image=self.loginImage, bg=bgColor1, fg=ftColor1)
        self.loginLabel2 = Label(self.loginFrame2, text='Login:', font=loginFont, bg=bgColor1, fg=ftColor1)
        self.loginLabel3 = Label(self.loginFrame3, text='Senha:', font=loginFont, bg=bgColor1, fg=ftColor1)

        self.loginMsg = Label(self.loginFrame8, relief=SUNKEN, text='', font=msgFont, bg=bgColor1, fg=msgColor1)
        
        #Botões
        self.loginButton1 = Button(self.loginFrame4, width=10, text='Cadastrar',
                                   command=lambda:self.signupWindow(self.__loginWindow),
                                   font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.loginButton2 = Button(self.loginFrame4, width=10, text='Entrar',
                                   command=lambda:self.loginAuthentication(self.__loginWindow),
                                   font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.loginButton3 = Button(self.loginFrame5, width=10, text='Sair',
                                   command=lambda:self.quitConfirm(self.__loginWindow),
                                   font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.loginButton1['padx'] = 5
        self.loginButton2['padx'] = 9
        self.loginButton3['padx'] = 5
        self.loginButton1.bind('<Return>', lambda event:self.signupWindow(self.__loginWindow))
        self.loginButton2.bind('<Return>', lambda event:self.loginAuthentication(self.__loginWindow))
        self.loginButton3.bind('<Return>', lambda event:self.quitConfirm(self.__loginWindow))
        
        #Packs
        self.loginEntry1.pack(side=RIGHT)
        self.loginEntry1.focus()
        self.loginEntry2.pack(side=RIGHT)
        self.loginLabel1.pack()
        self.loginLabel2.pack(side=RIGHT)
        self.loginLabel3.pack(side=RIGHT)
        self.loginButton1.pack(side=LEFT)
        self.loginFrame7.pack(side=LEFT)
        self.loginButton2.pack(side=RIGHT)
        self.loginButton3.pack()
        self.loginMsg.pack(fill=X)

        self.__loginWindow.mainloop()

    #Autenticação de Usuário
    def loginAuthentication(self, master):
        #print('Login pressionado:', self.__entry1.get())
        self.__authentication = library.login(self.__entry1.get(), self.__entry2.get())

        #Autenticação de Usuário ou administrador
        if(self.__authentication == 0):
            #print('Usuário')
            self.loginMsg['text'] = 'Usuário logado'
            self.__entry2.set('') #Limpando o campo senha
            self.userWindow(master)
        elif(self.__authentication == 1):
            #print('Administrador')
            self.loginMsg['text'] = 'Administrador logado'
            self.__entry2.set('') #Limpando o campo senha
            self.superWindow(master)
        else:
            self.loginMsg['text'] = 'Usuário ou senha incorretos.'

    #Tela de Cadastro
    def signupWindow(self, master):
        self.__CPF, self.__password = self.__entry1.get(), self.__entry2.get()
        master.destroy()
        self.__signupWindow = Tk()
        self.__signupWindow.title('-- Biblioteca UFRPE -- (Cadastro de Usuário)')
        centerWindow(self.__signupWindow, 515, 350)
        self.__signupWindow.bind('<Escape>', lambda event:self.loginWindow(self.__signupWindow))
        self.__signupWindow.protocol('WM_DELETE_WINDOW', lambda :self.loginWindow(self.__signupWindow))
        
        
        
        #Imagem
        self.signupImage = PhotoImage(file='Image%susers.png'%(os.sep))

        #Armazena valores das Entradas
        self.__entry1 = StringVar(); self.__entry1.set(self.__CPF)
        self.__entry2 = StringVar(); self.__entry2.set(self.__password)
        self.__entry3 = StringVar()
        self.__entry4 = StringVar()
        self.__loginMsg = ''
        
        #Etiquetas
        self.signupLabel1 = Label(self.__signupWindow, text='CPF', font=loginFont, bg=bgColor1, fg=ftColor1)
        self.signupLabel2 = Label(self.__signupWindow, text='Nome', font=loginFont, bg=bgColor1, fg=ftColor1)
        self.signupLabel3 = Label(self.__signupWindow, text='Senha', font=loginFont, bg=bgColor1, fg=ftColor1)
        self.signupLabel4 = Label(self.__signupWindow, text='Confirmar Senha', font=loginFont, bg=bgColor1, fg=ftColor1)
        
        self.signupTitle = Label(self.__signupWindow, text='CADASTRO', font=titleFont, bg=bgColor1, fg=titleColor1)
        self.signupImageLabel = Label(self.__signupWindow, width=266, image=self.signupImage, bg=bgColor1, fg=ftColor1)

        self.signupMsg = Label(self.__signupWindow, width=64, relief=SUNKEN, text='', font=msgFont, bg=bgColor1, fg=msgColor1)

        #Entrada
        self.signupEntry1 = Entry(self.__signupWindow, width=35, textvariable=self.__entry1, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.signupEntry2 = Entry(self.__signupWindow, width=35, textvariable=self.__entry3, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.signupEntry3 = Entry(self.__signupWindow, show='●', width=35, textvariable=self.__entry2, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.signupEntry4 = Entry(self.__signupWindow, show='●', width=35, textvariable=self.__entry4, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.signupEntry4.bind('<Return>', lambda event:self.saveSignup(self.__signupWindow))

        #Botões
        self.signupButton1 = Button(self.__signupWindow, width=10, text='Voltar',
                                    command=lambda:self.loginWindow(self.__signupWindow),
                                    font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.signupButton2 = Button(self.__signupWindow, width=10, text='Cadastrar',
                                    command=lambda:self.saveSignup(self.__signupWindow),
                                    font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.signupButton1.bind('<Return>', lambda event:self.loginWindow(self.__signupWindow))
        self.signupButton2.bind('<Return>', lambda event:self.saveSignup(self.__signupWindow))

        #Grids
        self.signupLabel1.grid(row=2, column=2, sticky=W, padx=5)
        self.signupLabel2.grid(row=4, column=2, sticky=W, padx=5)
        self.signupLabel3.grid(row=6, column=2, sticky=W, padx=5)
        self.signupLabel4.grid(row=8, column=2, sticky=W, padx=5)
        self.signupTitle.grid(row=1, column=1, columnspan=2)
        self.signupEntry1.grid(row=3, column=2, sticky=W, padx=8)
        self.signupEntry1.focus()
        self.signupEntry2.grid(row=5, column=2, sticky=W, padx=8)
        self.signupEntry3.grid(row=7, column=2, sticky=W, padx=8)
        self.signupEntry4.grid(row=9, column=2, sticky=W, padx=8)
        self.signupImageLabel.grid(row=2, column=1, rowspan=9)
        self.signupButton1.grid(row=10, column=2, padx=40, pady=15,sticky=W)
        self.signupButton2.grid(row=10, column=2, padx=16, pady=15, sticky=E)
        self.signupMsg.grid(row=11, column=1, columnspan=2, pady=33, sticky=E)

        self.__signupWindow.mainloop()

    #Verificação e armazenamento dos dados da Tela de Cadastro
    def saveSignup(self, master):
        self.__CPF = self.__entry1.get()
        self.__name = self.__entry3.get()
        self.__password = self.__entry2.get()
        self.__confirmPass = self.__entry4.get()
        self.__okPass = True

        #self.__CPF = self.__CPF.replace('.','')
        #self.__CPF = self.__CPF.replace('-','')

        #Verificação de requisitos para salvar o cadastros
        if(not CPFVerify(self.__CPF)):
            self.signupMsg['text'] = 'CPF inválido.'
            #messagebox.showerror('Erro', 'CPF inválido.')
            self.__okPass = False
        elif(len(self.__name) < 3):
            self.signupMsg['text'] = 'Nome muito curto.'
            #messagebox.showerror('Erro', 'Nome muito curto.')
            self.__okPass = False
        elif(len(self.__password) < 4 or len(self.__password) > 20):
            self.signupMsg['text'] = 'Insira uma senha que contenha entre 4 a 20 caracteres.'
            #messagebox.showerror('Erro', 'Insira uma senha com no minimo 4 caracteres.')
            self.__okPass = False
        elif(self.__password != self.__confirmPass):
            self.signupMsg['text'] = 'As senhas devem coincidir.'
            #messagebox.showerror('Erro', 'As senhas devem coincidir.')
            self.__okPass = False
        elif(self.__password == self.__CPF):
            self.signupMsg['text'] = 'A senha deve ser diferente do CPF.'
            #messagebox.showerror('Erro', 'A senha deve ser diferente do CPF.'
            self.__okPass = False
        elif(self.__okPass):
            self.__stateUser = library.signupUser(self.__CPF, self.__name, self.__password)
            if(self.__stateUser[0] == 0):
                self.signupMsg['text'] = self.__stateUser[1]
                #messagebox.showerror('Erro', self.__stateUser[1])
            else:
                self.signupMsg['text'] = ''
                self.__entry2.set(''); self.__entry3.set(''); self.__entry4.set('')
                messagebox.showinfo('Cadastro', self.__stateUser[1])
                library.saveDataBase()#library.refresh()
                self.loginWindow(master)
                        
    #Tela de Usuário
    def userWindow(self, master):
        self.userLogged = library.searchUser(self.__entry1.get())
        master.destroy()
        self.__userWindow = Tk()
        self.__userWindow.title('-- Biblioteca UFRPE -- (%s)'%(self.userLogged.getData()['name']))
        self.__userWindow.bind('<Escape>', lambda event:self.userQuitConfirm(self.__userWindow)) #Deslogar precionando ESC
        self.__userWindow.protocol('WM_DELETE_WINDOW', lambda :self.userQuitConfirm(self.__userWindow))
        
        centerWindow(self.__userWindow, 800, 450)

        #Conteiners
        self.userFrame1 = Frame(self.__userWindow, bg=bgColor1)
        self.userFrame2 = Frame(self.__userWindow, bg=bgColor1)
        self.userFrame3 = Frame(self.__userWindow, bg=bgColor1)
        self.userFrame4 = Frame(self.__userWindow, bg=bgColor1)
        self.userFrame4['padx'] = 30
        self.userFrame4['pady'] = 10

        #Packing Conteiners
        self.userFrame1.pack(fill=X)
        self.userFrame2.pack()
        self.userFrame3.pack(fill=BOTH, expand=True)
        self.userFrame4.pack(side=BOTTOM, anchor=E)
        
        #Etiquetas
        self.userLabel1 = Label(self.userFrame1, text='Usuário:', font=topFont, bg=bgColor1, fg=ftColor1)
        self.userLabel2 = Label(self.userFrame1, text=self.userLogged.getData()['name'], font=topFont, bg=bgColor1, fg=topColor2)
        self.userLabel3 = Label(self.userFrame1, text='CPF:', font=topFont, bg=bgColor1, fg=ftColor1)
        self.userLabel4 = Label(self.userFrame1, text=self.userLogged.getKey(), font=topFont, bg=bgColor1, fg=topColor2)
        self.userLabel5 = Label(self.userFrame1, text='Livros:', font=topFont, bg=bgColor1, fg=ftColor1)
        self.userLabel6 = Label(self.userFrame1, font=topFont, bg=bgColor1, fg=topColor2)
        self.userLabel6['text'] = [Label(self.userFrame1, text=self.userLogged.getData()['books'][x][:70]+' || Prazo de entrega: '+str(self.userLogged.getData()['refund'][x].date()), font=topFont, bg=bgColor1, fg=topColor2).grid(row=3+x, column=2, sticky=W) for x in range(len(self.userLogged.getData()['books']))] if len(self.userLogged.getData()['books']) > 0 else 'Nenhum'
        self.userLabel7 = Label(self.userFrame2, text='ESCOLHA UMA CATEGORIA', font=topFont, bg=bgColor1, fg=ftColor1)
        self.userLabel7['pady'] = 10
        
        #Botões
        self.userButton1 = Button(self.userFrame4, width=10, command=lambda:self.userQuitConfirm(self.__userWindow),
                                  text='Deslogar', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.userButton2 = Button(self.userFrame4, width=10, command=lambda:self.userSelectBookTopLevel(self.userListbox.get(ACTIVE), self.userLogged.getKey()),
                                  text='Selecionar', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.userButton1.bind('<Return>', lambda event:self.userQuitConfirm(self.__userWindow))
        self.userButton2.bind('<Return>', lambda event:self.userSelectBookTopLevel(self.userListbox.get(ACTIVE), self.userLogged.getKey()))
        
        #Pack e Grid etiquetas e botões
        self.userLabel1.grid(row=1, column=1, sticky=E)
        self.userLabel2.grid(row=1, column=2, sticky=W)
        self.userLabel3.grid(row=2, column=1, sticky=E)
        self.userLabel4.grid(row=2, column=2, sticky=W)
        self.userLabel5.grid(row=3, column=1, sticky=E)
        self.userLabel6.grid(row=3, column=2, sticky=W)
        self.userLabel7.pack()
        self.userButton1.pack(side=LEFT)
        self.userFrame5 = Frame(self.userFrame4, bg=bgColor1, width=10).pack(side=LEFT) #Espaço entre os botões Deslogar e Selecionar
        self.userButton2.pack(side=LEFT)
        
        #Armazenando Disciplinas em lista
        self.__disciplineList = []
        for file in os.listdir('DataBase%sBook'%(os.sep)):
            if(file[:-4] not in self.__disciplineList and file[:-4] not in os.listdir('Temp%sDBook'%(os.sep))):
                self.__disciplineList.append(file[:-4])

        for file in os.listdir('Temp%sBook'%(os.sep)):
            if(file[:-4] not in self.__disciplineList):
                self.__disciplineList.append(file[:-4])

        self.__disciplineList.sort()
        
        #ScrollBar
        self.userScrollbar = Scrollbar(self.userFrame3)
        self.userScrollbar.pack(side=RIGHT, fill=Y)

        #ListBox
        self.userListbox = Listbox(self.userFrame3, font=listFont1, yscrollcommand=self.userScrollbar.set, bg=bgListColor1,
                                   fg=ftListColor, selectbackground=bgSelListColor, selectforeground=ftSelListColor)
        self.userListbox.bind('<Return>', lambda event:self.userSelectBookTopLevel(self.userListbox.get(ACTIVE), self.userLogged.getKey()))
        self.userListbox.bind('<Double-Button-1>', lambda event:self.userSelectBookTopLevel(self.userListbox.get(ACTIVE), self.userLogged.getKey()))

        #Inserindo Disciplinas na Listbox
        for i in range(len(self.__disciplineList)):
            self.userListbox.insert(END, str(i+1).rjust(len(str(len(self.__disciplineList))),'0')+'. '+self.__disciplineList[i])
            if(i%2 != 0): #Alternando as cores de fundo dos itens da Listbox
                self.userListbox.itemconfig(i, bg=bgListColor2)
                    
        #Linkando o Scrollbar ao Listbox
        self.userListbox.pack(side=RIGHT, fill="both", expand=True)
        self.userListbox.focus()
        self.userScrollbar.config(command=self.userListbox.yview)
        
        self.__userWindow.mainloop()

    #Tela de seleção de Livros pelo Usuário
    def userSelectBookTopLevel(self, selection, CPF):
        self.__userSelectBookTopLevel = Toplevel()
        centerWindow(self.__userSelectBookTopLevel, 800, 450)
        self.__userSelectBookTopLevel.grab_set()
        self.__userSelectBookTopLevel.bind('<Escape>', lambda event:self.__userSelectBookTopLevel.destroy()) #Voltar pressionando ESC
        
        selection = selection[selection.index('.')+2:] #Categoria escolhida, limpando caracteres indesejados

        #Conteiners
        self.userSelectBookFrame1 = Frame(self.__userSelectBookTopLevel, bg=bgColor1)
        self.userSelectBookFrame2 = Frame(self.__userSelectBookTopLevel, bg=bgColor1)
        self.userSelectBookFrame3 = Frame(self.__userSelectBookTopLevel, bg=bgColor1)
        self.userSelectBookFrame4 = Frame(self.__userSelectBookTopLevel, bg=bgColor1)
        self.userSelectBookFrame4['padx'] = 30
        self.userSelectBookFrame4['pady'] = 10

        #Empacotando Conteiners
        self.userSelectBookFrame1.pack()
        self.userSelectBookFrame2.pack()
        self.userSelectBookFrame3.pack(fill=BOTH, expand=True)
        self.userSelectBookFrame4.pack(side=BOTTOM, anchor=E)
        
        #Etiquetas
        self.userSelectBookLabel1 = Label(self.userSelectBookFrame1, text=selection, font=titleFont, bg=bgColor1, fg=ftColor2)
        self.userSelectBookLabel2 = Label(self.userSelectBookFrame2, text='ESCOLHA UM LIVRO', font=loginFont, bg=bgColor1, fg=ftColor1)
        self.userSelectBookLabel2['pady'] = 10
        
        #Botões
        self.userSelectBookButton1 = Button(self.userSelectBookFrame4, width=10, command=self.__userSelectBookTopLevel.destroy,
                                  text='Voltar', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.userSelectBookButton2 = Button(self.userSelectBookFrame4, width=10, text='Reservar', font=defaultFont,
                                            bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                            command=lambda:self.userRequestBook(CPF, self.userSelectBookListbox.get(ACTIVE),selection))
        self.userSelectBookButton1.bind('<Return>', lambda event:self.__userSelectBookTopLevel.destroy())
        self.userSelectBookButton2.bind('<Return>', lambda event:self.userRequestBook(CPF, self.userSelectBookListbox.get(ACTIVE),selection))
        
        #Pack Etiquetas e Botões
        self.userSelectBookLabel1.pack()
        self.userSelectBookLabel2.pack()
        self.userSelectBookButton1.pack(side=LEFT)
        self.userSelectBookFrame5 = Frame(self.userSelectBookFrame4, bg=bgColor1, width=10).pack(side=LEFT) #Espaço entre os botões Deslogar e Selecionar
        self.userSelectBookButton2.pack(side=LEFT)

        #Lista de livros
        self.__bookList = library.searchDisponibleBooks2(selection) #library.searchDisponibleBooks(selection)
        
        #ScrollBar
        self.userSelectBookScrollbar = Scrollbar(self.userSelectBookFrame3)
        self.userSelectBookScrollbar.pack(side=RIGHT, fill=Y)

        #Listbox
        self.userSelectBookListbox = Listbox(self.userSelectBookFrame3, yscrollcommand=self.userSelectBookScrollbar.set,
                                   font=listFont2, bg=bgListColor1, fg=ftListColor, selectbackground=bgSelListColor, selectforeground=ftSelListColor)
        self.userSelectBookListbox.bind('<Return>', lambda event:self.userRequestBook(CPF, self.userSelectBookListbox.get(ACTIVE),selection))
        self.userSelectBookListbox.bind('<Double-Button-1>', lambda event:self.userRequestBook(CPF, self.userSelectBookListbox.get(ACTIVE),selection))
        
        #Inserindo Livros na Listbox
        for i in range(len(self.__bookList)):
            self.userSelectBookListbox.insert(END, str(i+1).rjust(len(str(len(self.__bookList))),'0')+'. '+self.__bookList[i].getKey()+' - %s/%s'%(str(self.__bookList[i].getData()['numbers']), str(self.__bookList[i].getData()['total'])))
            if(i%2 != 0): #Alternando as cores de fundo dos itens da Listbox
                self.userSelectBookListbox.itemconfig(i, bg=bgListColor2)
        
        #Linkando o Scrollbar ao Listbox
        self.userSelectBookListbox.pack(side=RIGHT, fill="both", expand=True)
        self.userSelectBookListbox.focus()
        self.userSelectBookScrollbar.config(command=self.userSelectBookListbox.yview)

    #Envia o pedido de livro do Usuário
    def userRequestBook(self, CPF, book, discipline):
        self.__requestList = library.getRequestBook()
        self.__user = library.searchUser(CPF)
        self.__solicited = len(self.__user.getData()['books'])
        
        for i in range(len(self.__requestList)): #Verifica se existe um pedido em espera
            if(self.__requestList[i][0] == CPF):
                self.__solicited += 1

        if(self.__solicited >= library.getMaxBooks()): #Mensagem de erro quando há livro em espera
            messagebox.showerror('Erro!', 'Não é possível solicitar um novo livro no momento, pois já foi feito o número máximo de pedidos.')
        else: #Realizando o pedido de empréstimo de livro
            self.__request = library.requestBook(CPF, book[book.index('.')+2:book.rindex(' - ')], discipline)
            if(self.__request[0] == 1): #Sucesso na realização do pedido
                library.saveDataBase()#library.refresh()
                messagebox.showinfo('Confirmação', self.__request[1])
            else: #Falha na realização do pedido
                messagebox.showerror('Erro!', self.__request[1])
            
    #Tela do Administrador
    def superWindow(self, master):
        self.userLogged = library.searchUser(self.__entry1.get())
        master.destroy()
        self.__superWindow = Tk()
        self.__superWindow.title('-- Biblioteca UFRPE -- (Administrador(a): %s)'%(self.userLogged.getData()['name'].upper()))
        self.__superWindow.bind('<Escape>', lambda event:self.userQuitConfirm(self.__superWindow)) #Deslogar precionando ESC
        self.__superWindow.protocol('WM_DELETE_WINDOW', lambda :self.userQuitConfirm(self.__superWindow))
        centerWindow(self.__superWindow, 900, 300)

        #Conteiners
        self.superWindowFrame1 = Frame(self.__superWindow, bg=bgColor1)
        self.superWindowFrame2 = Frame(self.__superWindow, bg=bgColor1)
        #self.superWindowFrame3 = Frame(self.__superWindow, bg=bgColor1)
        self.superWindowFrame4 = Frame(self.__superWindow, bg=bgColor1)
        
        #Empacotando Conteiners
        self.superWindowFrame4.pack(side=LEFT)
        #self.superWindowFrame3.pack(side=BOTTOM, fill=BOTH)
        self.superWindowFrame1.pack(side=LEFT, fill=BOTH, expand=True)
        self.superWindowFrame2.pack(side=LEFT, fill=BOTH, expand=True)
        
        #Image
        self.superWindowImage = PhotoImage(file='Image%sadm.png'%(os.sep))

        self.superWindowImage1 = PhotoImage(file='Image%sBookApprove.png'%(os.sep))
        self.superWindowImage2 = PhotoImage(file='Image%sBookReceive.png'%(os.sep))
        self.superWindowImage3 = PhotoImage(file='Image%sBookRegister.png'%(os.sep))
        self.superWindowImage4 = PhotoImage(file='Image%sBookDelete.png'%(os.sep))
        self.superWindowImage5 = PhotoImage(file='Image%sUserDelete.png'%(os.sep))
        self.superWindowImage6 = PhotoImage(file='Image%sUserChangePrivilege.png'%(os.sep))
        self.superWindowImage7 = PhotoImage(file='Image%sReportUsers.png'%(os.sep))
        self.superWindowImage8 = PhotoImage(file='Image%sReportBooks.png'%(os.sep))
        self.superWindowImage9 = PhotoImage(file='Image%sSave.png'%(os.sep))
        self.superWindowImage10 = PhotoImage(file='Image%sLogoff.png'%(os.sep))
        
        #Image Label
        self.superWindowImageLabel = Label(self.superWindowFrame4, image=self.superWindowImage, bg=bgColor1)

        #Botões
        self.superWindowButton1 = Button(self.superWindowFrame1, text=' APROVAR PEDIDO', anchor=W, font=admBtnFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                         command=self.superApprovesTopLevel, image=self.superWindowImage1, compound=LEFT)
        self.superWindowButton2 = Button(self.superWindowFrame2, text=' RECEBER LIVRO', anchor=W, font=admBtnFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                         command=self.receiveBookTopLevel, image=self.superWindowImage2, compound=LEFT)
        self.superWindowButton3 = Button(self.superWindowFrame1, text=' CADASTRAR LIVRO', anchor=W, font=admBtnFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                         command=self.registerBookTopLevel, image=self.superWindowImage3, compound=LEFT)
        self.superWindowButton4 = Button(self.superWindowFrame2, text=' EXCLUIR LIVRO', anchor=W, font=admBtnFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                         command=self.deleteBookTopLevel, image=self.superWindowImage4, compound=LEFT)
        self.superWindowButton5 = Button(self.superWindowFrame1, text=' EXCLUIR USUÁRIO', anchor=W, font=admBtnFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                         command=self.deleteUserTopLevel, image=self.superWindowImage5, compound=LEFT)
        self.superWindowButton6 = Button(self.superWindowFrame2, text=' MUDAR PRIVILÉGIO', anchor=W, font=admBtnFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                         command=self.changeSuperTopLevel, image=self.superWindowImage6, compound=LEFT)
        self.superWindowButton7 = Button(self.superWindowFrame1, text=' RELATÓRIO DE USUÁRIOS', anchor=W, font=admBtnFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                         command=self.reportUsersTopLevel, image=self.superWindowImage7, compound=LEFT)
        self.superWindowButton8 = Button(self.superWindowFrame2, text=' RELATÓRIO DE LIVROS', anchor=W, font=admBtnFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                         command=self.reportBooksTopLevel, image=self.superWindowImage8, compound=LEFT)
        self.superWindowButton9 = Button(self.superWindowFrame1, text=' SALVAR', anchor=W, font=admBtnFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                         command=self.saveDataBaseToplevel, image=self.superWindowImage9, compound=LEFT)
        self.superWindowButton10 = Button(self.superWindowFrame2, text=' DESLOGAR', anchor=W, font=admBtnFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                         command=lambda:self.userQuitConfirm(self.__superWindow), image=self.superWindowImage10, compound=LEFT)

        self.superWindowButton1.bind('<Return>', lambda event:self.superApprovesTopLevel())
        self.superWindowButton2.bind('<Return>', lambda event:self.receiveBookTopLevel())
        self.superWindowButton3.bind('<Return>', lambda event:self.registerBookTopLevel())
        self.superWindowButton4.bind('<Return>', lambda event:self.deleteBookTopLevel())
        self.superWindowButton5.bind('<Return>', lambda event:self.deleteUserTopLevel())
        self.superWindowButton6.bind('<Return>', lambda event:self.changeSuperTopLevel())
        self.superWindowButton7.bind('<Return>', lambda event:self.reportUsersTopLevel())
        self.superWindowButton8.bind('<Return>', lambda event:self.reportBooksTopLevel())
        self.superWindowButton9.bind('<Return>', lambda event:self.saveDataBaseToplevel())
        self.superWindowButton10.bind('<Return>', lambda event:self.userQuitConfirm(self.__superWindow))
        
        #Empacotando Botões
        self.superWindowButton1.pack(fill=BOTH, expand=True)
        self.superWindowButton2.pack(fill=BOTH, expand=True)
        self.superWindowButton3.pack(fill=BOTH, expand=True)
        self.superWindowButton4.pack(fill=BOTH, expand=True)
        self.superWindowButton5.pack(fill=BOTH, expand=True)
        self.superWindowButton6.pack(fill=BOTH, expand=True)
        self.superWindowButton7.pack(fill=BOTH, expand=True)
        self.superWindowButton8.pack(fill=BOTH, expand=True)
        self.superWindowButton9.pack(fill=BOTH, expand=True)
        self.superWindowButton10.pack(fill=BOTH, expand=True)
        
        self.superWindowImageLabel.pack()
        self.__superWindow.mainloop()

    #Aprovação de pedido de emprestimo de livros
    def superApprovesTopLevel(self):
        #self.__superApprovesTopLevel = Toplevel()
        #centerWindow(self.__superApprovesTopLevel, 800, 500)
        #self.__superApprovesTopLevel.grab_set()
        #self.__superApprovesTopLevel.bind('<Escape>', lambda event:self.__superApprovesTopLevel.destroy()) #Voltar pressionando ESC

        #Lista de pedidos de empréstimo
        self.__requestList = library.getRequestBook()
        self.__deleteList = []

        if(len(self.__requestList) == 0): #Sem pedido de empréstimo de livros
            messagebox.showwarning('Sem Pedidos', 'Não há pedidos pendentes.')
        else:
            messagebox.showinfo('Informação', 'Existem %d pedidos pendentes.'%(len(self.__requestList)) if len(self.__requestList) > 1 else 'Existe %d pedido pendente.'%(len(self.__requestList)))
            self.__resquestCount = 1
            for x in self.__requestList: #For na lista de pedidos de empréstimo de livros
                self.__userRequesting = library.searchUser(str(x[0])) #Objeto com os dados do usuário
                self.confirmRequest = messagebox.askquestion('Aprovar?', 'Pedido: %d\nLivro: %s \n\nUsuário: %s'%(self.__resquestCount, str(x[1]), str(self.__userRequesting.getData()['name'])))
                self.__resquestCount += 1
                if(self.confirmRequest == 'yes'): #Analisando o 'sim' na janela de confirmação de pedido 
                    self.requestReturn = library.approveRequestBook(x[0], x[1], x[2])
                    if(self.requestReturn[0] == 0):
                        messagebox.showerror('Erro!', self.requestReturn[1]) #Erro no emprestimo, Usuário com o número máximo de livros ou livro não cadastrado
                        self.__deleteList.append(x)
                    elif(self.requestReturn[0] == -1): #Livro não disponível, Ainda permanece na lista
                        messagebox.showerror('Erro!', self.requestReturn[1])
                    else:
                        messagebox.showinfo('Aprovado', self.requestReturn[1]) #Pedido aprovado
                        self.__deleteList.append(x)

            for x in self.__deleteList:
                self.__requestList.remove(x)
                self.__needSave = 1
                
            library.refresh()#library.saveDataBase()
            
    #Tela de pesquisa do usuário que vai devolver livro
    def receiveBookTopLevel(self, master=None):
        if(master != None):
            master.destroy()
            
        self.__receiveBookTopLevel = Toplevel()
        self.__receiveBookTopLevel.title('Pesquisar CPF (Devolução)')
        centerWindow(self.__receiveBookTopLevel, 300, 70)
        self.__receiveBookTopLevel.grab_set()
        self.__receiveBookTopLevel.bind('<Escape>', lambda event:self.__receiveBookTopLevel.destroy()) #Voltar pressionando ESC

        self.__Entry = StringVar()

        #Conteiners
        self.__receiveBookTopLevelFrame00 = Frame(self.__receiveBookTopLevel, bg=bgColor1, width=5) #Evitar que o Entry encoste na borda da janela
        self.__receiveBookTopLevelFrame01 = Frame(self.__receiveBookTopLevel, bg=bgColor1, width=5) #Evitar que o Entry encoste na borda da janela
        self.__receiveBookTopLevelFrame1 = Frame(self.__receiveBookTopLevel, bg=bgColor1)
        self.__receiveBookTopLevelFrame2 = Frame(self.__receiveBookTopLevel, bg=bgColor1)
        self.__receiveBookTopLevelFrame3 = Frame(self.__receiveBookTopLevel, bg=bgColor1)

        #Empacotando Conteiners
        self.__receiveBookTopLevelFrame00.pack(side=LEFT, fill=Y)
        self.__receiveBookTopLevelFrame01.pack(side=RIGHT, fill=Y)
        self.__receiveBookTopLevelFrame1.pack(fill=X)
        self.__receiveBookTopLevelFrame2.pack(fill=X)
        self.__receiveBookTopLevelFrame3.pack()

        #Etiqueta
        self.__receiveBookTopLevelLabel = Label(self.__receiveBookTopLevelFrame1, text='CPF', font=loginFont, bg=bgColor1, fg=ftColor1)

        #Entrada
        self.__receiveBookTopLevelEntry = Entry(self.__receiveBookTopLevelFrame2, textvariable=self.__Entry, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.__receiveBookTopLevelEntry.bind('<Return>', lambda event:self.receiveBookSearchCPF(self.__receiveBookTopLevel))
        
        #Botões
        self.__receiveBookTopLevelButton1 = Button(self.__receiveBookTopLevelFrame3, width=10, text='Voltar', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                                   command=self.__receiveBookTopLevel.destroy)
        self.__receiveBookTopLevelButton2 = Button(self.__receiveBookTopLevelFrame3, width=10, text='OK', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                                   command=lambda:self.receiveBookSearchCPF(self.__receiveBookTopLevel))
        self.__receiveBookTopLevelButton1.bind('<Return>', lambda event:self.__receiveBookTopLevel.destroy())
        self.__receiveBookTopLevelButton2.bind('<Return>', lambda event:self.receiveBookSearchCPF(self.__receiveBookTopLevel))

        #Empacotando Etiqueta, Entrada e Botões
        self.__receiveBookTopLevelLabel.pack(side=LEFT)
        self.__receiveBookTopLevelEntry.pack(side=LEFT, fill=X, expand=True)
        self.__receiveBookTopLevelEntry.focus()
        self.__receiveBookTopLevelButton1.pack(side=LEFT)
        self.__receiveBookTopLevelButton2.pack(side=RIGHT)

        self.__receiveBookTopLevel.mainloop()

    #Pesquisa de usuário que vai devolver livro.
    def receiveBookSearchCPF(self, master):
        if(CPFVerify(self.__Entry.get()) == 0): #Verificando se o CPF digitado é válido
            messagebox.showerror('Erro!', 'CPF inválido.')
            return

        self.__user = library.searchUser(self.__Entry.get())

        if(self.__user.getKey() == None):
            messagebox.showerror('Erro!', 'Usuário não cadastrado.')
            self.__Entry.set('')
        elif(len(self.__user.getData()['books']) == 0):
            messagebox.showwarning('Aviso!', 'Usuário não tem livros para devolver no momento.')
            self.__Entry.set('')
        else: #Carregando Janela com os livros que estão com o usuário
            master.destroy()
            self.selectReceiveBookTopLevel(self.__user)
        
    #Tela de escolha do livro a ser devolvido
    def selectReceiveBookTopLevel(self, user):
        self.__selectReceiveBookTopLevel = Toplevel()
        self.__selectReceiveBookTopLevel.title('Devolução')
        centerWindow(self.__selectReceiveBookTopLevel, 500, 300)
        self.__selectReceiveBookTopLevel.grab_set()
        self.__selectReceiveBookTopLevel.bind('<Escape>', lambda event:self.receiveBookTopLevel(self.__selectReceiveBookTopLevel)) #Voltar pressionando ESC
        self.__selectReceiveBookTopLevel.protocol('WM_DELETE_WINDOW', lambda :self.receiveBookTopLevel(self.__selectReceiveBookTopLevel))
        
        #Conteiners
        self.selectReceiveBookTopLevelFrame1 = Frame(self.__selectReceiveBookTopLevel, bg=bgColor1)
        self.selectReceiveBookTopLevelFrame2 = Frame(self.__selectReceiveBookTopLevel, bg=bgColor1)
        self.selectReceiveBookTopLevelFrame3 = Frame(self.__selectReceiveBookTopLevel, bg=bgColor1)
        self.selectReceiveBookTopLevelFrame4 = Frame(self.__selectReceiveBookTopLevel, bg=bgColor1)
        self.selectReceiveBookTopLevelFrame4['padx'] = 30
        self.selectReceiveBookTopLevelFrame4['pady'] = 10
        
        #Empacotando Conteiners
        self.selectReceiveBookTopLevelFrame1.pack()
        self.selectReceiveBookTopLevelFrame2.pack()
        self.selectReceiveBookTopLevelFrame3.pack(fill=BOTH, expand=True)
        self.selectReceiveBookTopLevelFrame4.pack(side=BOTTOM, anchor=E)
        
        #Etiquetas
        self.selectReceiveBookTopLevelLabel1 = Label(self.selectReceiveBookTopLevelFrame1, text=user.getData()['name'], font=titleFont, bg=bgColor1, fg=ftColor2)
        self.selectReceiveBookTopLevelLabel2 = Label(self.selectReceiveBookTopLevelFrame2, text='ESCOLHA UM LIVRO', font=loginFont, bg=bgColor1, fg=ftColor1)
        self.selectReceiveBookTopLevelLabel2['pady'] = 10
        
        #Botões
        self.selectReceiveBookTopLevelButton1 = Button(self.selectReceiveBookTopLevelFrame4, width=10, command=lambda :self.receiveBookTopLevel(self.__selectReceiveBookTopLevel),
                                  text='Voltar', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.selectReceiveBookTopLevelButton2 = Button(self.selectReceiveBookTopLevelFrame4, width=10, text='Devolver', font=defaultFont,
                                            bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                            command=lambda:self.receivingBook(user, self.selectReceiveBookTopLevelListbox.get(ACTIVE), self.__selectReceiveBookTopLevel))
        self.selectReceiveBookTopLevelButton1.bind('<Return>', lambda event:self.receiveBookTopLevel(self.__selectReceiveBookTopLevel))
        self.selectReceiveBookTopLevelButton2.bind('<Return>', lambda event:self.receivingBook(user, self.selectReceiveBookTopLevelListbox.get(ACTIVE), self.__selectReceiveBookTopLevel))
        
        #Pack Etiquetas e Botões
        self.selectReceiveBookTopLevelLabel1.pack()
        self.selectReceiveBookTopLevelLabel2.pack()
        self.selectReceiveBookTopLevelButton1.pack(side=LEFT)
        self.selectReceiveBookTopLevelFrame4 = Frame(self.selectReceiveBookTopLevelFrame4, bg=bgColor1, width=10).pack(side=LEFT) #Espaço entre os botões Deslogar e Selecionar
        self.selectReceiveBookTopLevelButton2.pack(side=LEFT)
        
        #ScrollBar
        self.selectReceiveBookTopLevelScrollbar = Scrollbar(self.selectReceiveBookTopLevelFrame3)
        self.selectReceiveBookTopLevelScrollbar.pack(side=RIGHT, fill=Y)

        #Listbox
        self.selectReceiveBookTopLevelListbox = Listbox(self.selectReceiveBookTopLevelFrame3, yscrollcommand=self.selectReceiveBookTopLevelScrollbar.set,
                                   font=listFont2, bg=bgListColor1, fg=ftListColor, selectbackground=bgSelListColor, selectforeground=ftSelListColor)
        self.selectReceiveBookTopLevelListbox.bind('<Return>', lambda event:self.receivingBook(user, self.selectReceiveBookTopLevelListbox.get(ACTIVE), self.__selectReceiveBookTopLevel))
        self.selectReceiveBookTopLevelListbox.bind('<Double-Button-1>', lambda event:self.receivingBook(user, self.selectReceiveBookTopLevelListbox.get(ACTIVE), self.__selectReceiveBookTopLevel))
        
        #Inserindo Livros na Listbox
        for i in range(len(user.getData()['books'])):
            self.selectReceiveBookTopLevelListbox.insert(END, str(i+1).rjust(len(str(len(user.getData()['books']))),'0')+'. '+user.getData()['books'][i])
            if(i%2 != 0): #Alternando as cores de fundo dos itens da Listbox
                self.selectReceiveBookTopLevelListbox.itemconfig(i, bg=bgListColor2)
        
        #Linkando o Scrollbar ao Listbox
        self.selectReceiveBookTopLevelListbox.pack(side=RIGHT, fill="both", expand=True)
        self.selectReceiveBookTopLevelListbox.focus()
        self.selectReceiveBookTopLevelScrollbar.config(command=self.selectReceiveBookTopLevelListbox.yview)

        self.__selectReceiveBookTopLevel.mainloop()
        
    #Devolvendo livro
    def receivingBook(self, user, selection, master):
        selection = selection[selection.index('.')+2:] #Livro Selecionado. Limpando caracteres indesejados
        self.index = user.getData()['books'].index(selection)
        self.__confirmRefund = library.refundBook(user.getKey(), selection, user.getData()['discipline'][self.index])

        if(self.__confirmRefund[0] == 0): #Mensagens de erro
            messagebox.showerror('Erro!', self.__confirmRefund[1])
        else:
            if(self.__confirmRefund[0] == 1): #Mensagem de confirmação de entrega de livro.
                messagebox.showinfo('Devolução', self.__confirmRefund[1])
            elif(self.__confirmRefund[0] == -1): #Mensagem de confirmação de entrega de livro e Quantos dias houve de atraso
                messagebox.showwarning('Atenção!', self.__confirmRefund[1])

            library.refresh()#library.saveDataBase()
            self.__needSave = 1 
            user = library.searchUser(user.getKey())
            if(len(user.getData()['books']) == 0):
                messagebox.showinfo('Concluído', 'Todos os livros foram devolvidos.')
                self.receiveBookTopLevel(self.__selectReceiveBookTopLevel)
                #master.destroy()
            else:
                master.destroy()
                self.selectReceiveBookTopLevel(user)
                
    #Tela de cadastro de Livro
    def registerBookTopLevel(self):
        self.__registerBookTopLevel = Toplevel()
        self.__registerBookTopLevel.title('-- Biblioteca UFRPE -- (Cadastro de Livros)')
        self.__registerBookTopLevel.grab_set()
        centerWindow(self.__registerBookTopLevel, 515, 350)
        self.__registerBookTopLevel.bind('<Escape>', lambda event:self.__registerBookTopLevel.destroy())
        
        #Imagem
        self.registerBookTopLevelImage = PhotoImage(file='Image%sbook.png'%(os.sep))

        #Armazena valores das Entradas
        self.__entry5 = StringVar() 
        self.__entry6 = StringVar()
        self.__entry7 = StringVar()
        self.__entry8 = StringVar()
        self.__loginMsg = ''

        #Armazenando Disciplinas em lista
        self.__disciplineList = []
        for file in os.listdir('DataBase%sBook'%(os.sep)):
            if(file[:-4] not in self.__disciplineList and file[:-4] not in os.listdir('Temp%sDBook'%(os.sep))):
                self.__disciplineList.append(file[:-4])

        for file in os.listdir('Temp%sBook'%(os.sep)):
            if(file[:-4] not in self.__disciplineList):
                self.__disciplineList.append(file[:-4])

        self.__disciplineList.sort()
        
        #Etiquetas
        self.registerBookTopLevelLabel1 = Label(self.__registerBookTopLevel, text='Título', font=loginFont, bg=bgColor1, fg=ftColor1)
        self.registerBookTopLevelLabel2 = Label(self.__registerBookTopLevel, text='Categoria', font=loginFont, bg=bgColor1, fg=ftColor1)
        self.registerBookTopLevelLabel3 = Label(self.__registerBookTopLevel, text='ISBN', font=loginFont, bg=bgColor1, fg=ftColor1)
        self.registerBookTopLevelLabel4 = Label(self.__registerBookTopLevel, text='Quantidade', font=loginFont, bg=bgColor1, fg=ftColor1)
        
        self.registerBookTopLevelTitle = Label(self.__registerBookTopLevel, text='CADASTRO DE LIVROS', font=titleFont, bg=bgColor1, fg=titleColor1)
        self.registerBookTopLevelImageLabel = Label(self.__registerBookTopLevel, width=266, image=self.registerBookTopLevelImage, bg=bgColor1, fg=ftColor1)

        self.registerBookTopLevelMsg = Label(self.__registerBookTopLevel, width=64, relief=SUNKEN, text='', font=msgFont, bg=bgColor1, fg=msgColor1)

        #Entrada
        self.registerBookTopLevelEntry1 = Entry(self.__registerBookTopLevel, width=35, textvariable=self.__entry5, selectbackground=bgSelColor, selectforeground=ftSelColor)

        self.registerBookTopLevelEntry2 = Autocomplete(self.__disciplineList, self.__registerBookTopLevel, width=35, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.__entry6 = self.registerBookTopLevelEntry2.text

        self.registerBookTopLevelEntry3 = Entry(self.__registerBookTopLevel, width=35, textvariable=self.__entry7, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.registerBookTopLevelSpinbox = Spinbox(self.__registerBookTopLevel, width=33, textvariable=self.__entry8, from_=1, to=99, state='readonly')
        self.registerBookTopLevelEntry3.bind('<Return>', lambda event:self.saveRegisterBook())
        #self.registerBookTopLevelSpinbox.bind('<Return>', lambda event:self.saveRegisterBook())

        #Botões
        self.registerBookTopLevelButton1 = Button(self.__registerBookTopLevel, width=10, text='Voltar',
                                    command=lambda:self.__registerBookTopLevel.destroy(),
                                    font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.registerBookTopLevelButton2 = Button(self.__registerBookTopLevel, width=10, text='Cadastrar',
                                    command=self.saveRegisterBook,
                                    font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.registerBookTopLevelButton1.bind('<Return>', lambda event:self.__registerBookTopLevel.destroy())
        self.registerBookTopLevelButton2.bind('<Return>', lambda event:self.saveRegisterBook())

        #Grids
        self.registerBookTopLevelLabel1.grid(row=2, column=2, sticky=W, padx=5)
        self.registerBookTopLevelLabel2.grid(row=4, column=2, sticky=W, padx=5)
        self.registerBookTopLevelLabel3.grid(row=6, column=2, sticky=W, padx=5)
        self.registerBookTopLevelLabel4.grid(row=8, column=2, sticky=W, padx=5)
        self.registerBookTopLevelTitle.grid(row=1, column=1, columnspan=2)
        self.registerBookTopLevelEntry1.grid(row=3, column=2, sticky=W, padx=8)
        self.registerBookTopLevelEntry1.focus()
        self.registerBookTopLevelEntry2.grid(row=5, column=2, sticky=W, padx=8)
        self.registerBookTopLevelEntry3.grid(row=7, column=2, sticky=W, padx=8)
        self.registerBookTopLevelSpinbox.grid(row=9, column=2, sticky=W, padx=8)
        self.registerBookTopLevelImageLabel.grid(row=2, column=1, rowspan=9)
        self.registerBookTopLevelButton1.grid(row=10, column=2, padx=40, pady=15,sticky=W)
        self.registerBookTopLevelButton2.grid(row=10, column=2, padx=16, pady=15, sticky=E)
        self.registerBookTopLevelMsg.grid(row=11, column=1, columnspan=2, pady=33, sticky=E)

        self.__registerBookTopLevel.mainloop()

    #Cadastrando livro no Banco de Dados
    def saveRegisterBook(self):
        self.__book = self.__entry5.get()
        self.__discipline = self.__entry6.get().capitalize()
        self.__ISBN = self.__entry7.get() if self.__entry7.get() != '' else None
        self.__numbers = self.__entry8.get()

        if(len(self.__book) < 3):
            messagebox.showerror('Erro!', 'Insira um "Título" com no mínimo 3 caracteres.')
        elif(len(self.__discipline) < 3):
            messagebox.showerror('Erro!', 'Insira uma "Categoria" com no mínimo 3 caracteres.')
        elif(ISBNVerify(self.__ISBN) == 0 and self.__ISBN != None):
            messagebox.showerror('Erro!', "ISBN inválido.")
        elif(self.__numbers.isnumeric() and int(self.__numbers) > 0): #Verificando se foram digitados números válidos
            self.__confirmRegister = library.registerBook(self.__book, self.__ISBN, int(self.__numbers), self.__discipline)
            if(self.__confirmRegister[0] == 1): #Confirmação
                messagebox.showinfo('Sucesso', self.__confirmRegister[1])
                library.refresh()#library.saveDataBase()
                self.__needSave = 1
                self.__registerBookTopLevel.destroy()
                self.registerBookTopLevel()
            else:
                messagebox.showerror('Erro!', self.__confirmRegister[1])
        else:
            messagebox.showerror('Erro!', 'No campo "Quantidade", insira um número inteiro positivo.')

    #Tela de exclusão livros (Seleção de categoria)
    def deleteBookTopLevel(self):
        self.__deleteBookTopLevel = Toplevel()
        self.__deleteBookTopLevel.title('Pesquisar Categoria (Excluir Livro)')
        self.__deleteBookTopLevel.bind('<Escape>', lambda event:self.__deleteBookTopLevel.destroy()) #Voltar precionando ESC
        centerWindow(self.__deleteBookTopLevel, 400, 450)
        self.__deleteBookTopLevel.grab_set()

        #Conteiners
        self.deleteBookTopLevelFrame1 = Frame(self.__deleteBookTopLevel, bg=bgColor1)
        self.deleteBookTopLevelFrame2 = Frame(self.__deleteBookTopLevel, bg=bgColor1)
        self.deleteBookTopLevelFrame3 = Frame(self.__deleteBookTopLevel, bg=bgColor1)
        self.deleteBookTopLevelFrame3['padx'] = 30
        self.deleteBookTopLevelFrame3['pady'] = 10

        #Packing Conteiners
        self.deleteBookTopLevelFrame1.pack()
        self.deleteBookTopLevelFrame2.pack(fill=BOTH, expand=True)
        self.deleteBookTopLevelFrame3.pack(side=BOTTOM, anchor=E)
        
        #Etiquetas
        self.deleteBookTopLevelLabel1 = Label(self.deleteBookTopLevelFrame1, text='ESCOLHA UMA CATEGORIA', font=topFont, bg=bgColor1, fg=ftColor1)
        self.deleteBookTopLevelLabel1['pady'] = 10
        
        #Botões
        self.deleteBookTopLevelButton1 = Button(self.deleteBookTopLevelFrame3, width=10, command=self.__deleteBookTopLevel.destroy,
                                                text='Voltar', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.deleteBookTopLevelButton2 = Button(self.deleteBookTopLevelFrame3, width=10, command=lambda:self.deleteBookSelectionTopLevel(self.deleteBookTopLevelListbox.get(ACTIVE), self.__deleteBookTopLevel),
        text='Selecionar', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1)
        self.deleteBookTopLevelButton1.bind('<Return>', lambda event:self.__deleteBookTopLevel.destroy())
        self.deleteBookTopLevelButton2.bind('<Return>', lambda event:self.deleteBookSelectionTopLevel(self.deleteBookTopLevelListbox.get(ACTIVE), self.__deleteBookTopLevel))
        
        #Pack e Grid etiquetas e botões
        self.deleteBookTopLevelLabel1.pack()
        self.deleteBookTopLevelButton1.pack(side=LEFT)
        self.deleteBookTopLevelFrame4 = Frame(self.deleteBookTopLevelFrame3, bg=bgColor1, width=10).pack(side=LEFT) #Espaço entre os botões Deslogar e Selecionar
        self.deleteBookTopLevelButton2.pack(side=LEFT)
        
        #Armazenando Disciplinas em lista
        self.__disciplineList = []
        for file in os.listdir('DataBase%sBook'%(os.sep)):
            if(file[:-4] not in self.__disciplineList and file[:-4] not in os.listdir('Temp%sDBook'%(os.sep))):
                self.__disciplineList.append(file[:-4])

        for file in os.listdir('Temp%sBook'%(os.sep)):
            if(file[:-4] not in self.__disciplineList):
                self.__disciplineList.append(file[:-4])

        self.__disciplineList.sort()
        
        #ScrollBar
        self.deleteBookTopLevelScrollbar = Scrollbar(self.deleteBookTopLevelFrame2)
        self.deleteBookTopLevelScrollbar.pack(side=RIGHT, fill=Y)

        #ListBox
        self.deleteBookTopLevelListbox = Listbox(self.deleteBookTopLevelFrame2, font=listFont1, yscrollcommand=self.deleteBookTopLevelScrollbar.set, bg=bgListColor1,
                                   fg=ftListColor, selectbackground=bgSelListColor, selectforeground=ftSelListColor)
        self.deleteBookTopLevelListbox.bind('<Return>', lambda event:self.deleteBookSelectionTopLevel(self.deleteBookTopLevelListbox.get(ACTIVE), self.__deleteBookTopLevel))
        self.deleteBookTopLevelListbox.bind('<Double-Button-1>', lambda event:self.deleteBookSelectionTopLevel(self.deleteBookTopLevelListbox.get(ACTIVE), self.__deleteBookTopLevel))

        #Inserindo Disciplinas na Listbox
        for i in range(len(self.__disciplineList)):
            self.deleteBookTopLevelListbox.insert(END, str(i+1).rjust(len(str(len(self.__disciplineList))),'0')+'. '+self.__disciplineList[i])
            if(i%2 != 0): #Alternando as cores de fundo dos itens da Listbox
                self.deleteBookTopLevelListbox.itemconfig(i, bg=bgListColor2)
                
        #Linkando o Scrollbar ao Listbox
        self.deleteBookTopLevelListbox.pack(side=RIGHT, fill="both", expand=True)
        self.deleteBookTopLevelListbox.focus()
        self.deleteBookTopLevelScrollbar.config(command=self.deleteBookTopLevelListbox.yview)

        
        self.__deleteBookTopLevel.mainloop()

    #Tela de exclusão de livros (Seleção de Livro)
    def deleteBookSelectionTopLevel(self, selection, master):
        self.__deleteBookSelectionTopLevel = Toplevel()
        self.__deleteBookSelectionTopLevel.title('Excluir Livro')
        centerWindow(self.__deleteBookSelectionTopLevel, 800, 450)
        self.__deleteBookSelectionTopLevel.grab_set()
        master.destroy()
        self.__deleteBookSelectionTopLevel.bind('<Escape>', lambda event:self.quitDeleteBookSelectionTopLevel(self.__deleteBookSelectionTopLevel)) #Voltar pressionando ESC
        self.__deleteBookSelectionTopLevel.protocol('WM_DELETE_WINDOW', lambda :self.quitDeleteBookSelectionTopLevel(self.__deleteBookSelectionTopLevel))
        
        selection = selection[selection.index('.')+2:] #Categoria Selecionada. Limpando caracteres indesejados
        self.__entry = StringVar()
        
        #Conteiners
        self.deleteBookSelectionTopLevelFrame1 = Frame(self.__deleteBookSelectionTopLevel, bg=bgColor1)
        self.deleteBookSelectionTopLevelFrame2 = Frame(self.__deleteBookSelectionTopLevel, bg=bgColor1)
        self.deleteBookSelectionTopLevelFrame2['pady'] = 10
        self.deleteBookSelectionTopLevelFrame3 = Frame(self.__deleteBookSelectionTopLevel, bg=bgColor1)
        self.deleteBookSelectionTopLevelFrame3['padx'] = 32
        self.deleteBookSelectionTopLevelFrame4 = Frame(self.__deleteBookSelectionTopLevel, bg=bgColor1)
        self.deleteBookSelectionTopLevelFrame4['padx'] = 30
        self.deleteBookSelectionTopLevelFrame4['pady'] = 10
        
        #Empacotando Conteiners
        self.deleteBookSelectionTopLevelFrame1.pack()
        self.deleteBookSelectionTopLevelFrame2.pack(fill=BOTH, expand=True)
        self.deleteBookSelectionTopLevelFrame4.pack(side=BOTTOM, anchor=E) 
        self.deleteBookSelectionTopLevelFrame3.pack(side=BOTTOM, anchor=E) 
        
        #Etiquetas
        self.deleteBookSelectionTopLevelLabel1 = Label(self.deleteBookSelectionTopLevelFrame1, text=selection, font=titleFont, bg=bgColor1, fg=ftColor2)
        self.deleteBookSelectionTopLevelLabel2 = Label(self.deleteBookSelectionTopLevelFrame1, text='ESCOLHA UM LIVRO', font=loginFont, bg=bgColor1, fg=ftColor1)
        self.deleteBookSelectionTopLevelLabel2['pady'] = 10
        self.deleteBookSelectionTopLevelLabel3 = Label(self.deleteBookSelectionTopLevelFrame3, text='Quantidade:', font=loginFont, bg=bgColor1, fg=ftColor1)
        
        #Botões
        self.deleteBookSelectionTopLevelButton1 = Button(self.deleteBookSelectionTopLevelFrame4, width=10, text='Voltar', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                                         command=lambda:self.quitDeleteBookSelectionTopLevel(self.__deleteBookSelectionTopLevel))
        self.deleteBookSelectionTopLevelButton2 = Button(self.deleteBookSelectionTopLevelFrame4, width=10, text='Excluir', font=defaultFont,
                                            bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                            command=lambda:self.superDeleteBook(self.deleteBookSelectionTopLevelListbox.get(ACTIVE), selection, self.__deleteBookSelectionTopLevel))
        self.deleteBookSelectionTopLevelButton1.bind('<Return>', lambda event:self.quitDeleteBookSelectionTopLevel(self.__deleteBookSelectionTopLevel))
        self.deleteBookSelectionTopLevelButton2.bind('<Return>', lambda event:self.superDeleteBook(self.deleteBookSelectionTopLevelListbox.get(ACTIVE), selection, self.__deleteBookSelectionTopLevel))
        
        #SpinBox
        self.deleteBookSelectionTopLevelSpinbox = Spinbox(self.deleteBookSelectionTopLevelFrame3, width=6, textvariable=self.__entry, from_=1, to=99, state='readonly')
        #self.deleteBookSelectionTopLevelSpinbox.bind('<Return>', lambda event:self.superDeleteBook(self.deleteBookSelectionTopLevelListbox.get(ACTIVE), selection, self.__deleteBookSelectionTopLevel))
        #self.deleteBookSelectionTopLevelSpinbox.bind('<FocusIn>', lambda event:self.deleteBookSelectionTopLevelButton1.focus_force())
        
        #Pack Etiquetas e Botões
        self.deleteBookSelectionTopLevelLabel1.pack()
        self.deleteBookSelectionTopLevelLabel2.pack()
        self.deleteBookSelectionTopLevelLabel3.pack(side=LEFT)
        self.deleteBookSelectionTopLevelButton1.pack(side=LEFT)
        self.deleteBookSelectionTopLevelFrame4 = Frame(self.deleteBookSelectionTopLevelFrame4, bg=bgColor1, width=10).pack(side=LEFT) #Espaço entre os botões Deslogar e Selecionar
        self.deleteBookSelectionTopLevelButton2.pack(side=LEFT)
        self.deleteBookSelectionTopLevelSpinbox.pack(side=RIGHT)

        #Lista de livros
        self.__bookList = library.searchDisponibleBooks2(selection) #library.searchDisponibleBooks(selection)
        if(len(self.__bookList) <= 0): #Fecha janela se não há mais livros na categoria selecionada. Necessário para a atualizar (recarregar) janela após exclusão de livro. 
            self.__deleteBookSelectionTopLevel.destroy()
            
        #ScrollBar
        self.deleteBookSelectionTopLevelScrollbar = Scrollbar(self.deleteBookSelectionTopLevelFrame2)
        self.deleteBookSelectionTopLevelScrollbar.pack(side=RIGHT, fill=Y)

        #Listbox
        self.deleteBookSelectionTopLevelListbox = Listbox(self.deleteBookSelectionTopLevelFrame2, yscrollcommand=self.deleteBookSelectionTopLevelScrollbar.set,
                                   font=listFont2, bg=bgListColor1, fg=ftListColor, selectbackground=bgSelListColor, selectforeground=ftSelListColor)
        self.deleteBookSelectionTopLevelListbox.bind('<Return>', lambda event:self.superDeleteBook(self.deleteBookSelectionTopLevelListbox.get(ACTIVE), selection, self.__deleteBookSelectionTopLevel))
        self.deleteBookSelectionTopLevelListbox.bind('<Double-Button-1>', lambda event:self.superDeleteBook(self.deleteBookSelectionTopLevelListbox.get(ACTIVE), selection, self.__deleteBookSelectionTopLevel))
        
        #Inserindo Livros na Listbox
        for i in range(len(self.__bookList)):
            self.deleteBookSelectionTopLevelListbox.insert(END, str(i+1).rjust(len(str(len(self.__bookList))),'0')+'. '+self.__bookList[i].getKey()+' - %s/%s'%(str(self.__bookList[i].getData()['numbers']), str(self.__bookList[i].getData()['total'])))
            if(i%2 != 0): #Alternando as cores de fundo dos itens da Listbox
                self.deleteBookSelectionTopLevelListbox.itemconfig(i, bg=bgListColor2)
        
        #Linkando o Scrollbar ao Listbox
        self.deleteBookSelectionTopLevelListbox.pack(side=RIGHT, fill="both", expand=True)
        self.deleteBookSelectionTopLevelListbox.focus()
        self.deleteBookSelectionTopLevelScrollbar.config(command=self.deleteBookSelectionTopLevelListbox.yview)

        self.__deleteBookSelectionTopLevel.mainloop()

    #Excluíndo livro do banco de dados
    def superDeleteBook(self, book, discipline, master):
        self.__numbers = self.__entry.get()
        self.__book = book[book.index('.')+2:book.rindex(' - ')]
        self.deleteConfirmBox = messagebox.askquestion('Excluir?', 'Deseja excuir %s?'%(self.__book)) #Janela de confirmação de exclusão de livro

        if(self.deleteConfirmBox == 'yes'):
            if(self.__numbers.isnumeric() and int(self.__numbers) > 0):
                self.__confirm = library.deleteBook(self.__book, int(self.__numbers), discipline)
                if(self.__confirm[0] == 1):
                    messagebox.showinfo('Informação', self.__confirm[1])
                    library.refresh()#library.saveDataBase()
                    self.__needSave = 1

                    try: #Evitar erro caso a Table fique vazia.
                        self.deleteBookSelectionTopLevel('. '+discipline, master) # O '. '+ serve para evitar que a função modifique o valor que fizer 'selection = selection[selection.index('.')+2:]'
                    except:
                        master.destroy()
                        self.deleteBookTopLevel()
                    
                    
                else:
                    messagebox.showerror('Erro!', self.__confirm[1])
            else:
                messagebox.showerror('Erro!', 'No campo "Quantidade", insira um número inteiro positivo.')

    #Tela de exclusão de usuário (Digitar CPF)
    def deleteUserTopLevel(self):
        self.__deleteUserTopLevel = Toplevel()
        self.__deleteUserTopLevel.title('Pesquisar CPF (Excluir)')
        centerWindow(self.__deleteUserTopLevel, 300, 70)
        self.__deleteUserTopLevel.grab_set()
        self.__deleteUserTopLevel.bind('<Escape>', lambda event:self.__deleteUserTopLevel.destroy()) #Voltar pressionando ESC

        self.__Entry = StringVar()

        #Conteiners
        self.__deleteUserTopLevelFrame00 = Frame(self.__deleteUserTopLevel, bg=bgColor1, width=5) #Evitar que o Entry encoste na borda da janela
        self.__deleteUserTopLevelFrame01 = Frame(self.__deleteUserTopLevel, bg=bgColor1, width=5) #Evitar que o Entry encoste na borda da janela
        self.__deleteUserTopLevelFrame1 = Frame(self.__deleteUserTopLevel, bg=bgColor1)
        self.__deleteUserTopLevelFrame2 = Frame(self.__deleteUserTopLevel, bg=bgColor1)
        self.__deleteUserTopLevelFrame3 = Frame(self.__deleteUserTopLevel, bg=bgColor1)

        #Empacotando Conteiners
        self.__deleteUserTopLevelFrame00.pack(side=LEFT, fill=Y)
        self.__deleteUserTopLevelFrame01.pack(side=RIGHT, fill=Y)
        self.__deleteUserTopLevelFrame1.pack(fill=X)
        self.__deleteUserTopLevelFrame2.pack(fill=X)
        self.__deleteUserTopLevelFrame3.pack()

        #Etiqueta
        self.__deleteUserTopLevelLabel = Label(self.__deleteUserTopLevelFrame1, text='CPF', font=loginFont, bg=bgColor1, fg=ftColor1)

        #Entrada
        self.__deleteUserTopLevelEntry = Entry(self.__deleteUserTopLevelFrame2, textvariable=self.__Entry, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.__deleteUserTopLevelEntry.bind('<Return>', lambda event:self.deletingUser(self.__deleteUserTopLevel))
        
        #Botões
        self.__deleteUserTopLevelButton1 = Button(self.__deleteUserTopLevelFrame3, width=10, text='Voltar', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                                   command=self.__deleteUserTopLevel.destroy)
        self.__deleteUserTopLevelButton2 = Button(self.__deleteUserTopLevelFrame3, width=10, text='OK', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                                   command=lambda:self.deletingUser(self.__deleteUserTopLevel))
        self.__deleteUserTopLevelButton1.bind('<Return>', lambda event:self.__deleteUserTopLevel.destroy())
        self.__deleteUserTopLevelButton2.bind('<Return>', lambda event:self.deletingUser(self.__deleteUserTopLevel))

        #Empacotando Etiqueta, Entrada e Botões
        self.__deleteUserTopLevelLabel.pack(side=LEFT)
        self.__deleteUserTopLevelEntry.pack(side=LEFT, fill=X, expand=True)
        self.__deleteUserTopLevelEntry.focus()
        self.__deleteUserTopLevelButton1.pack(side=LEFT)
        self.__deleteUserTopLevelButton2.pack(side=RIGHT)

        self.__deleteUserTopLevel.mainloop()

    #Excluíndo Usuário
    def deletingUser(self, master):
        if(CPFVerify(self.__Entry.get()) == 0): #Verificando se o CPF digitado é válido
            messagebox.showerror('Erro!', 'CPF inválido.')
            self.__Entry.set('')
            return
        
        self.deletingUserConfirmBox = messagebox.askquestion('Confirmação', 'Deseja realmente excluir o usuário: %s?'%(self.__Entry.get()))

        if(self.deletingUserConfirmBox == 'yes'):            
            self.__user = library.deleteUser(self.__Entry.get())

            if(self.__user[0] == 0):
                messagebox.showerror('Erro!', self.__user[1])
            elif(self.__user[0] == -1):
                messagebox.showwarning('Não Excluído!', self.__user[1])
            elif(self.__user[0] == 1):
                messagebox.showinfo('Excluído', self.__user[1])
                library.refresh()#library.saveDataBase()
                self.__needSave = 1

        self.__Entry.set('')

    #Tela de alteração de privilégio (Digitar CPF)
    def changeSuperTopLevel(self):
        self.__changeSuperTopLevel = Toplevel()
        self.__changeSuperTopLevel.title('Pesquisar CPF (Alterar Privilégio)')
        centerWindow(self.__changeSuperTopLevel, 300, 70)
        self.__changeSuperTopLevel.grab_set()
        self.__changeSuperTopLevel.bind('<Escape>', lambda event:self.__changeSuperTopLevel.destroy()) #Voltar pressionando ESC

        self.__Entry = StringVar()

        #Conteiners
        self.__changeSuperTopLevelFrame00 = Frame(self.__changeSuperTopLevel, bg=bgColor1, width=5) #Evitar que o Entry encoste na borda da janela
        self.__changeSuperTopLevelFrame01 = Frame(self.__changeSuperTopLevel, bg=bgColor1, width=5) #Evitar que o Entry encoste na borda da janela
        self.__changeSuperTopLevelFrame1 = Frame(self.__changeSuperTopLevel, bg=bgColor1)
        self.__changeSuperTopLevelFrame2 = Frame(self.__changeSuperTopLevel, bg=bgColor1)
        self.__changeSuperTopLevelFrame3 = Frame(self.__changeSuperTopLevel, bg=bgColor1)

        #Empacotando Conteiners
        self.__changeSuperTopLevelFrame00.pack(side=LEFT, fill=Y)
        self.__changeSuperTopLevelFrame01.pack(side=RIGHT, fill=Y)
        self.__changeSuperTopLevelFrame1.pack(fill=X)
        self.__changeSuperTopLevelFrame2.pack(fill=X)
        self.__changeSuperTopLevelFrame3.pack()

        #Etiqueta
        self.__changeSuperTopLevelLabel = Label(self.__changeSuperTopLevelFrame1, text='CPF', font=loginFont, bg=bgColor1, fg=ftColor1)

        #Entrada
        self.__changeSuperTopLevelEntry = Entry(self.__changeSuperTopLevelFrame2, textvariable=self.__Entry, selectbackground=bgSelColor, selectforeground=ftSelColor)
        self.__changeSuperTopLevelEntry.bind('<Return>', lambda event:self.changingSuper())
        
        #Botões
        self.__changeSuperTopLevelButton1 = Button(self.__changeSuperTopLevelFrame3, width=10, text='Voltar', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                                   command=self.__changeSuperTopLevel.destroy)
        self.__changeSuperTopLevelButton2 = Button(self.__changeSuperTopLevelFrame3, width=10, text='OK', font=defaultFont, bg=btColor1, activebackground=btColor2, fg=ftColor1,
                                                   command=lambda:self.changingSuper())
        self.__changeSuperTopLevelButton1.bind('<Return>', lambda event:self.__changeSuperTopLevel.destroy())
        self.__changeSuperTopLevelButton2.bind('<Return>', lambda event:self.changingSuper())

        #Empacotando Etiqueta, Entrada e Botões
        self.__changeSuperTopLevelLabel.pack(side=LEFT)
        self.__changeSuperTopLevelEntry.pack(side=LEFT, fill=X, expand=True)
        self.__changeSuperTopLevelEntry.focus()
        self.__changeSuperTopLevelButton1.pack(side=LEFT)
        self.__changeSuperTopLevelButton2.pack(side=RIGHT)

        self.__changeSuperTopLevel.mainloop()

    #Alterando privilégio.
    def changingSuper(self):
        if(CPFVerify(self.__Entry.get()) == 0): #Verificando se o CPF digitado é válido
            messagebox.showerror('Erro!', 'CPF inválido.')
            self.__Entry.set('')
            return
        if(self.userLogged.getKey() == self.__Entry.get()):
            messagebox.showerror('Erro!', 'Não é possível alterar seu próprio privilégio.')
            self.__Entry.set('')
            return
            
        self.changingSuperConfirmBox = messagebox.askquestion('Alterar Privilégio?', 'Deseja realmente alterar os privilégios do usuário: %s?'%(self.__Entry.get()))

        if(self.changingSuperConfirmBox == 'yes'):            
            self.__user = library.changeSuperUser(self.__Entry.get())

            if(self.__user[0] == 0):
                messagebox.showerror('Erro!', self.__user[1])
            elif(self.__user[0] == -1):
                messagebox.showwarning('Privilégio revogado!', self.__user[1])
                library.refresh()#library.saveDataBase()
                self.__needSave = 1
            elif(self.__user[0] == 1):
                messagebox.showinfo('Privilegio concedido', self.__user[1])
                library.refresh()#library.saveDataBase()
                self.__needSave = 1

        self.__Entry.set('')

    #Relatório de Livros
    def reportBooksTopLevel(self):
        self.reportBooksTopLevelConfirmBox = messagebox.askquestion('Relatório de Livros, salvar banco de dados?', 'Para gerar um relatório dos livros é necessário salvar o banco de dados.\n\nDeseja salvar o Banco de dados?')

        if(self.reportBooksTopLevelConfirmBox == 'yes'):
            self.__superWindow.withdraw() #Escondendo a Janela
            print('Gerando relatório...')
            library.reportBooks()
            self.__needSave = 0
            self.__superWindow.deiconify() #Revelando a Janela
            print('Relatório gerado.')
            messagebox.showinfo('Concluído', 'Relatório de livros gerado com sucesso.')
        else:
            messagebox.showinfo('Cancelado', 'Relatório não foi gerado.')
            
    #Relatório de Usuário
    def reportUsersTopLevel(self):
        self.reportUsersTopLevelConfirmBox = messagebox.askquestion('Relatório de Usuários, salvar banco de dados?', 'Para gerar um relatório dos usuários é necessário salvar o banco de dados.\n\nDeseja salvar o Banco de dados?')

        if(self.reportUsersTopLevelConfirmBox == 'yes'):
            self.__superWindow.withdraw() #Escondendo a Janela
            print('Gerando relatório...')
            library.reportUsers()
            self.__needSave = 0
            self.__superWindow.deiconify() #Revelando a Janela
            print('Relatório gerado.')
            messagebox.showinfo('Concluído', 'Relatório de usuários gerado com sucesso.')
        else:
            messagebox.showinfo('Cancelado', 'Relatório não foi gerado.')

    #Salvar Banco de Dados
    def saveDataBaseToplevel(self):
        self.saveDataBaseToplevelConfirmBox = messagebox.askquestion('Salvar?', 'Deseja salvar todas as alterações realizadas?')

        if(self.saveDataBaseToplevelConfirmBox == 'yes'):
            self.__superWindow.withdraw() #Escondendo a Janela
            library.saveDataBase()
            self.__needSave = 0
            self.__superWindow.deiconify() #Revelando a Janela
            messagebox.showinfo('Concluído', 'Banco de dados salvo com sucesso.')
        
    #Sair do programa
    def quitConfirm(self, master):
        self.quitConfirmBox = messagebox.askquestion('Sair?','Realmente deseja sair?')
        if(self.quitConfirmBox == 'yes'):
            master.destroy()
        else:
            del self.quitConfirmBox

    #Deslogar Usuário ou Administrador
    def userQuitConfirm(self, master):
        if(self.__needSave == 1):#Se foi feita alguma alteração pelo ADM, programa questionará se deseja salva banco de dados
            self.saveDataBaseToplevel()

        self.userQuitConfirmBox = messagebox.askquestion('Deslogar?','Realmente deseja Deslogar?')
        if(self.userQuitConfirmBox == 'yes'):
            self.__needSave = 0
            library.loadDataBase()#Carrega Banco de dados para descartar alterações realizadas.
            self.loginWindow(master)
        else:
            del self.userQuitConfirmBox

    #Retorna a Seleção de categoria na tela de exclusão de livros
    def quitDeleteBookSelectionTopLevel(self, master):
        master.destroy()
        self.deleteBookTopLevel()

############################################################################
library = Bibliotec()
Windows()
