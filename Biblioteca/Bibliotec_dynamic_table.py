import pickle, os#, datetime
from CripHash2 import *
from New_RB_Tree import *
from Authenticator import *
from datetime import datetime #Função datetime.now() e datetime.today() funcionam do memso jeito retornando data e hora, já o date.today() não só retorna a data.
#datetime trabalha com data e hora e a date somente com data, com relação a data, ambas são muito parecidas.

class Bibliotec:
    def __init__(self, tableFunction=RBTree, maxBooks=3):
        self.__tableFunction = tableFunction #Função Arvore vermelho e preto
        self.__booksDataBase = self.__tableFunction() #Arvore dos livros
        self.__usersDataBase = self.__tableFunction() #arvore dos usuarios

        self.__superUser = 0
        self.__maxBooks = maxBooks
        self.__inviteBook = []
        self.__currentUserTable = ''
        self.__currentBookTable = ''
        
        #Diretórios
        self.__rootPath = os.getcwd()
        self.__pathUsersDataBase = self.__rootPath+'%sDataBase%sUser'%(os.sep, os.sep)
        self.__pathBooksDataBase = self.__rootPath+'%sDataBase%sBook'%(os.sep, os.sep)
        self.__pathUsersTemp = self.__rootPath+'%sTemp%sUser'%(os.sep, os.sep)
        self.__pathBooksTemp = self.__rootPath+'%sTemp%sBook'%(os.sep, os.sep)
        self.__pathUsersDeleted = self.__rootPath+'%sTemp%sDUser'%(os.sep, os.sep)
        self.__pathBooksDeleted = self.__rootPath+'%sTemp%sDBook'%(os.sep, os.sep)
        
        self.loadDataBase()
        #self.createTempPath()
        if(__name__ == '__main__'):
            if(self.__superUser == 0):
                self.signupUser('07947643474', 'Edson', '0000')
                
    #Cria as pastas necessárias.
    def createSystemPath(self):
        self.rootPath()
        if('Temp' not in os.listdir()):
            os.mkdir('Temp')
        if('User' not in os.listdir('Temp')):
            os.mkdir('Temp%sUser'%(os.sep))
        if('Book' not in os.listdir('Temp')):
            os.mkdir('Temp%sBook'%(os.sep))

        if('DUser' not in os.listdir('Temp')):
            os.mkdir('Temp%sDUser'%(os.sep))
        if('DBook' not in os.listdir('Temp')):
            os.mkdir('Temp%sDBook'%(os.sep))

        if('DataBase' not in os.listdir()):
            os.mkdir('DataBase')
        if('User' not in os.listdir('DataBase')):
            os.mkdir('DataBase%sUser'%(os.sep))
        if('Book' not in os.listdir('DataBase')):
            os.mkdir('DataBase%sBook'%(os.sep))

        if('Reports' not in os.listdir()):
            os.mkdir('Reports')

    def refresh(self): #Atualiza os arquivos temporários
        self.changeUserTable('')
        self.changeBookTable('')
        
    #Muda a tabela de usuário a ser utilizada.
    def changeUserTable(self, CPF):
        try:
            os.chdir('Temp%sUser'%(os.sep))
        except:
            self.createSystemPath()
            os.chdir('Temp%sUser'%(os.sep))

        if(self.__currentUserTable !=  ''): #Verifica se uma tabela já foi carregada
            if(len(self.__usersDataBase) > 0): #Verifica se a tabela carregada contém elementos
                pickle.dump(self.__usersDataBase, open(self.__currentUserTable+'.tmp', 'wb')) #Salvando tabela carregada em arquivo temporário
                if(self.__currentUserTable in os.listdir(self.__pathUsersDeleted)): #Verifica se existe referência a tabela carregada
                    os.remove(self.__pathUsersDeleted+os.sep+self.__currentUserTable) #Exclui a referência a Tabela carregada
            else:
                if(self.__currentUserTable+'.tmp' in os.listdir()): #Caso não haja elementos na tabela carregada, exclui o arquivo temporário
                    os.remove(self.__currentUserTable+'.tmp') #Excluído arquivo temporário
                if(self.__currentUserTable+'.aed' in os.listdir(self.__pathUsersDataBase)): #Caso a tabela carregada esteja salva na pasta Database\Book, cria uma referência na pasta Temp\DBook para excluir o arquivo na pasta Database\Book quando banco de dados for salvo.
                    open(self.__pathUsersDeleted+os.sep+self.__currentUserTable, 'w').close() # Criando referência na pasta Temp\Dbook
                
            
        
        if(CPF[:3]+'.tmp' in os.listdir()): #Carrega tabela se ela está na pasta de temporários
            self.__usersDataBase = pickle.load(open(CPF[:3]+'.tmp', 'rb'))
        elif(CPF[:3]+'.aed' in os.listdir(self.__pathUsersDataBase) and CPF[:3] not in os.listdir(self.__pathUsersDeleted)): #Carrega tabela se ela está na pasta de DataBase e não existe referência a tabela
            self.__usersDataBase = pickle.load(open(self.__pathUsersDataBase+os.sep+CPF[:3]+'.aed', 'rb'))
        else: #Cria tabela vazia
            self.__usersDataBase = self.__tableFunction()

        self.__currentUserTable = CPF[:3]
        self.rootPath()

    #Muda a tabela de livros a ser utilizada.
    def changeBookTable(self, discipline):
        try:
            os.chdir('Temp%sBook'%(os.sep))
        except:
            self.createSystemPath()
            os.chdir('Temp%sBook'%(os.sep))

        if(self.__currentBookTable !=  ''): #Verifica se uma tabela já foi carregada
            if(len(self.__booksDataBase) > 0):#Verifica se a tabela carregada contém elementos
                pickle.dump(self.__booksDataBase, open(self.__currentBookTable+'.tmp', 'wb')) #Salvando tabela carregada em arquivo temporário
                if(self.__currentBookTable in os.listdir(self.__pathBooksDeleted)): #Verifica se existe referência a tabela carregada
                    os.remove(self.__pathBooksDeleted+os.sep+self.__currentBookTable) #Exclui a referência a Tabela carregada
            else:
                if(self.__currentBookTable+'.tmp' in os.listdir()): #Caso não haja elementos na tabela carregada, exclui o arquivo temporário
                    os.remove(self.__currentBookTable+'.tmp') #Excluído arquivo temporário
                if(self.__currentBookTable+'.aed' in os.listdir(self.__pathBooksDataBase)): #Caso a tabela carregada esteja salva na pasta Database\Book, cria uma referência na pasta Temp\DBook para excluir o arquivo na pasta Database\Book quando banco de dados for salvo.
                    open(self.__pathBooksDeleted+os.sep+self.__currentBookTable, 'w').close() # Criando referência na pasta Temp\Dbook
                    
        
        if(discipline+'.tmp' in os.listdir()): #Carrega tabela se ela está na pasta de Temporários
            self.__booksDataBase = pickle.load(open(discipline+'.tmp', 'rb'))
        elif(discipline+'.aed' in os.listdir(self.__pathBooksDataBase) and discipline not in os.listdir(self.__pathBooksDeleted)): #Carrega tabela se ela está na pasta de DataBase e não existe referência a tabela
            self.__booksDataBase = pickle.load(open(self.__pathBooksDataBase+os.sep+discipline+'.aed', 'rb'))
        else: #Cria tabela vazia
            self.__booksDataBase = self.__tableFunction()

        self.__currentBookTable = discipline
        self.rootPath()

    #Cadastro de usuários
    def signupUser (self, CPF, name, password='8888'):
        if(CPFVerify(CPF)):
            self.changeUserTable(CPF)
            if(self.__superUser == 0):
                self.__usersDataBase.insert(CPF, {'name':name, 'books':[], 'refund':[], 'discipline':[], 'password':cripHash(password), 'superUser':1})
                self.__superUser = 1
                return 1, 'Administrador cadastrado com sucesso.'
                #return print('Administrador cadastrado com sucesso.')
                
            elif(self.__usersDataBase.insert(CPF, {'name':name, 'books':[], 'refund':[], 'discipline':[], 'password':cripHash(password), 'superUser':0})):
                return 1, 'Usuário cadastrado com sucesso.'
                #return print('%s cadastrado com sucesso.'%(name))
            else:
                return 0, 'CPF de número %s já está cadastrado no sistema.'%(CPF)
                #return print('CPF de número %s já está cadastrado no sistema.'%(CPF))
        else:
            return 0, 'CPF inválido.'
            #return print('CPF inválido.')

    #Pesquisar Usuário
    def searchUser(self, CPF):
        self.changeUserTable(CPF)
        return self.__usersDataBase.search(CPF)
        
    #Exclui usuário do banco de dados
    def deleteUser(self, CPF):
        self.changeUserTable(CPF)
        user = self.__usersDataBase.search(CPF)

        if(user.getKey() != None):
            if(len(user.getData()['books']) != 0):
                return -1, '%s não pode ser excluído antes de devolver:\n•%s'%(user.getData()['name'], '\n•'.join(user.getData()['books']))
                #return print('%s não pode ser excluído antes de devolver:\n%s'%(user.getData()['name'], '\n'.join(user.getData()['books'])))
            elif(user.getData()['superUser'] == 1):
                return -1, 'Administrador não pode ser excluído.'
                #return print('Administrador não pode ser excluído.')
            else:
                self.__usersDataBase.delete(CPF)
                for x in self.__inviteBook[:]: #Removendo pedidos que continham o Usuário
                    if(str(CPF) in x):
                        self.__inviteBook.remove(x)
                return 1, '%s foi excluído do banco de dados.'%(user.getData()['name'])
                #return print('%s foi excluído do banco de dados.'%(user.getData()['name']))
        else:
            return 0, 'Usuário não Cadastrado'
            #return print('Usuário não encontrado')
        
    #Muda o privilégio de administrador de um usuário.
    def changeSuperUser(self, CPF):
        self.changeUserTable(CPF)
        user = self.__usersDataBase.search(CPF)

        if(user.getKey() != None):
            if(user.getData()['superUser'] == 1):
                user.getData()['superUser'] = 0
                return -1, 'Agora %s não é mais um administrador.' %(user.getData()['name'])
            else:
                user.getData()['superUser'] = 1
                return 1, 'Agora %s é administrador.' %(user.getData()['name'])
        else:
            return 0, 'Usuário não Cadastrado'
    
    #Cria arquivo .TXT com os dados dos usuários
    def reportUsers(self):
        report = []
        report.append('Relatório gerado às %s:%s do dia %d/%d/%d'%(str(datetime.now().hour).rjust(2,'0'), str(datetime.now().minute).rjust(2,'0'), datetime.now().day, datetime.now().month, datetime.now().year))
        self.saveDataBase()
        
        for file in os.listdir(self.__pathUsersDataBase):
            self.changeUserTable(file[:3])
            alist = self.__usersDataBase.list()
            
            for x in range(len(alist)):
                y = self.__usersDataBase.search(alist[x])
                books = 'Nenhum' if y.getData()['books']==[] else '\n• '+'\n• '.join([y.getData()['books'][x]+' || Entrega: '+str(y.getData()['refund'][x].date()) for x in range(len(y.getData()['books']))])
                report.append('CPF: '+str(y.getKey())+'\n'+'Nome: '+y.getData()['name']+'\n'+'Livros emprestado: '+books)

        os.chdir('Reports') #Muda o diretório
        arq = open('Report_Users-%s.txt'%(str(datetime.now())[:19].replace(':','꞉')), 'w')
        arq.write('\n\n'.join(report))
        arq.close()

        del alist, report
        self.rootPath()
        
    #Autenticação de login de usuário
    def login(self, login, password):
        self.changeUserTable(login)
        user = self.__usersDataBase.search(login)
        
        if(user.getKey() == login and user.getData()['password'] == cripHash(password)):
            return user.getData()['superUser']
        return -1

    #Autenticação de login de administrador
    '''def superLogin(self, login, password):
        self.changeUserTable(login)
        user = self.__usersDataBase.search(login)
        
        if(user.getKey() == login and user.getData()['password'] == password and user.getData()['superUser'] == 1):
            return 1
        return 0
    '''
    #Solicitação de livro.
    def requestBook(self, CPF, book, discipline='Sem Categoria'):
        self.changeUserTable(CPF)
        user = self.__usersDataBase.search(CPF)
        if(user.getKey() == None):
            return 0, 'CPF não cadastrado.'
            #return print('CPF não cadastrado.')
        
        self.changeBookTable(discipline)
        request = self.__booksDataBase.search(book)
        if(request.getKey() == None):
            return 0, 'Livro não cadastrado.'
            #return print('Livro não cadastrado.')

        self.__inviteBook.append([CPF, book, discipline])
        return 1, 'Livro encaminhado para aprovação.'
        #return print('Livro encaminhado para aprovação.')
        
    #Lista de solicitação de livros.
    def getRequestBook(self):
        return self.__inviteBook

    def getMaxBooks(self):
        return self.__maxBooks

    #Aprovar solicitação de livros.
    def approveRequestBook(self, CPF, book, discipline='Sem categoria'):
        self.changeUserTable(CPF)
        user = self.__usersDataBase.search(CPF)

        self.changeBookTable(discipline)
        request = self.__booksDataBase.search(book)

        if(book in user.getData()['books']):
            return 0, '%s já está com o uma cópia do livro %s emprestado.'%(str(user.getData()['name']), str(book))
            #return print('%s já está com o uma cópia do livro %s emprestado.'%(str(user.getData()['name']), str(book)))
        if(request.getKey() == book):
            if(len(user.getData()['books']) >= self.__maxBooks):
                return 0, 'Emprestimo recusado, %s já com o número máximo de livros.'%(str(user.getData()['name']))
                #return print('Emprestimo recusado, %s já com o número máximo de livros.'%(CPF))
            elif(request.getData()['numbers'] > 0):
                request.getData()['numbers'] -= 1
                request.getData()['users'].append(CPF)
                user.getData()['books'].append(book)
                user.getData()['discipline'].append(discipline)
                user.getData()['refund'].append(datetime.fromordinal(datetime.now().toordinal()+7))
                return 1, 'Livro, %s emprestado com sucesso.\nPrazo de entrega: %s/%s/%s'%(book, user.getData()['refund'][-1].day, user.getData()['refund'][-1].month, user.getData()['refund'][-1].year)
                #return print('Livro, %s emprestado com sucesso'%(book))
            else:
                return -1, 'Livro, %s indisponível.'%(book)
                #return print('Livro, %s indisponível.'%(book))
        return 0, 'Livro não cadastrado.'
        #return print('Livro não cadastrado.')

    #Cadastro de livros.
    def registerBook (self, bookName, ISBN=None, numbers=1, discipline='Sem categoria'):
        if(ISBN==None or ISBNVerify(ISBN)):
            self.changeBookTable(discipline)
            if(self.__booksDataBase.insert(bookName, {'ISBN':ISBN, 'numbers':numbers, 'total':numbers, 'users':[]})):
                return 1, 'Livro, %s cadastrado com sucesso'%(bookName)#1
                #return print('Livro, %s cadastrado com sucesso'%(bookName))
            else:
                book = self.__booksDataBase.search(bookName)
                book.getData()['numbers'] += numbers
                book.getData()['total'] += numbers
                return 1, '%d livros %s foram adicionados com sucesso.'%(int(numbers), bookName) if int(numbers) > 1 else '%d livro %s foi adicionado com sucesso.'%(int(numbers), bookName)
                #return print('%d livro(s) %s adicionado(s) com sucesso.'%(int(numbers), bookName))
                
        else:
            return 0, 'ISBN incorreto.'
            #return print('ISBN incorreto.')

    #Pesquisa Livro
    def searchBook (self, bookName, discipline='Sem categoria'):
        self.changeBookTable(discipline)
        return self.__booksDataBase.search(bookName)
    
    #Retorna uma lista das chaves dos livros que estão disponíveis.
    def searchDisponibleBooks (self, discipline='Sem categoria'):
        self.changeBookTable(discipline)
        self.__listBooks = self.__booksDataBase.list()

        for x in self.__listBooks[:]:
            if(self.__booksDataBase.search(x).getData()['numbers'] <= 0):
                self.__listBooks.remove(x)

        return self.__listBooks

    #Retorna uma lista dos objetos dos livros que estão disponíveis.
    def searchDisponibleBooks2 (self, discipline='Sem categoria'):
        self.changeBookTable(discipline)
        self.__listBooks = self.__booksDataBase.list2()

        for x in self.__listBooks[:]:
            if(x.getData()['numbers'] <= 0):
                self.__listBooks.remove(x)

        return self.__listBooks
    
    #Exclui livro do banco de dados.
    def deleteBook (self, bookName, numbers=1, discipline='Sem categoria'):
        self.changeBookTable(discipline)
        book = self.__booksDataBase.search(bookName)    
        if(book.getKey() != None):
            if(len(book.getData()['users']) == 0):
                #return 0, 'Impossível excluir %d livros, pois existem cópias dele com os usuários: %s.'%(numbers, ', '.join(book.getData()['users'])) if len(book.getData()['users']) > 1 else 'Impossível excluir 1 livro, pois existe uma cópia dele com o usuário: %s.'%(', '.join(book.getData()['users']))
                #return print('Impossível excluir %d livro, pois existem cópias do livro com: %s.'%(numbers, ', '.join(book.getData()['users'])))
                if(book.getData()['total'] <= numbers):
                    self.__booksDataBase.delete(bookName)
                    for x in self.__inviteBook: #Removendo pedidos que continham o Livro
                        if(str(bookName) in x):
                            self.__inviteBook.remove(x)
                    return 1, 'Livro %s excluído do banco de dados.'%(str(bookName))
                    #return print('Livro %s excluído do banco de dados.'%(str(bookName)))
                else:
                    book.getData()['numbers'] -= numbers
                    book.getData()['total'] -= numbers
                    return 1, 'Resta %d/%d unidades %s no banco de dados.'%(book.getData()['numbers'], book.getData()['total'], str(bookName))
                    #return print('Resta %d unidades %s no banco de dados.'%(book.getData()['numbers'], str(bookName)))
            else:
                if(book.getData()['numbers'] > numbers):
                    book.getData()['numbers'] -= numbers
                    book.getData()['total'] -= numbers
                else:
                    book.getData()['numbers'] = 0
                    book.getData()['total'] = len(book.getData()['users'])

                return 1, 'Restam %d/%d unidades de %s no banco de dados.'%(book.getData()['numbers'], book.getData()['total'], str(bookName)) if book.getData()['total'] > 1 else 'Resta %d/%d unidades %s no banco de dados.'%(book.getData()['numbers'], book.getData()['total'], str(bookName))
                #return print('Resta %d unidades %s no banco de dados.'%(book.getData()['numbers'], str(bookName)))
        return 0, 'Livro não encontrado'
        #return print('Livro não encontrado')
        
    #Cria arquivo .TXT com todos os livros no banco de dados.
    def reportBooks(self):
        alistAll = []
        self.saveDataBase()
        
        for file in os.listdir(self.__pathBooksDataBase):
            self.changeBookTable(file[:-4])
            alist = ['\n'+'--'+file[:-4]+'--'+'\n']+self.__booksDataBase.list() #Tópico de Categoria
            
            for x in range(1,len(alist)):
                alist[x] = alist[x]+' - Livros em estoque: %d/%d'%(int(self.__booksDataBase.search(alist[x]).getData()['numbers']),int(self.__booksDataBase.search(alist[x]).getData()['total']))
            alistAll =  alistAll+alist

        zeros = len(str(len(alistAll)))
        numbers = 1
        for x in range(len(alistAll)):
            if(alistAll[x][:3] != '\n--'):
                alistAll[x] = str(numbers).rjust(zeros,'0')+' - '+alistAll[x]
                numbers += 1
            
        os.chdir('Reports') #Muda o diretório
        arq = open('Report_Books-%s.txt'%(str(datetime.now())[:19].replace(':','꞉')), 'w')
        today = 'Relatório gerado às %s:%s do dia %d/%d/%d\n'%(str(datetime.today().hour).rjust(2,'0'), str(datetime.today().minute).rjust(2,'0'), datetime.today().day, datetime.today().month, datetime.today().year)
        arq.write(today+'\n'.join(alistAll))
        arq.close()
        self.rootPath()

        #del alist
        del alistAll

    #Registra a Devolução de livro
    def refundBook(self, CPF, book, discipline='Sem categoria'):
        self.changeUserTable(CPF)
        user = self.__usersDataBase.search(CPF)
        if(user.getKey() == None):
            return 0, 'CPF não cadastrado.'
            #return print('CPF não cadastrado.')
        
        self.changeBookTable(discipline)
        refund = self.__booksDataBase.search(book)
        if(refund.getKey() == None):
            return 0, 'Livro não cadastrado.'
            #return print('Livro não cadastrado.')

        try:
            index = user.getData()['books'].index(book)
        except:
            return 0, 'Livro, %s não está com %s'%(str(refund.getKey()), str(user.getData()['name']))
            #return print('Livro, %s não está com %s'%(str(refund.getKey()), str(user.getData()['name'])))
        
            
        del user.getData()['books'][index]
        del user.getData()['discipline'][index]
        refundday = user.getData()['refund'].pop(index).toordinal()
        today = datetime.today().toordinal()

        index = refund.getData()['users'].index(CPF)
        del refund.getData()['users'][index]
        refund.getData()['numbers'] += 1

        if(refundday-today < 0):
            return -1, 'Livro entregue com %d dias de atraso.'%((refundday-today)*-1) if ((refundday-today)*-1) > 1 else 'Livro entregue com %d dia de atraso.'%((refundday-today)*-1)
            #return print('Livro entregue com %d dia(s) de atraso.'%((refundday-today)*-1))
        return 1, 'Livro devolvido com sucesso.'
        #return print('Livro devolvido com sucesso.')
            
    #Retorna para o diretório raiz do programa.
    def rootPath(self):
        os.chdir(self.__rootPath)

    #Salva banco de dados.    
    def saveDataBase(self):
        self.createSystemPath()
        self.refresh()
        #self.changeUserTable(self.__currentUserTable), self.changeBookTable(self.__currentBookTable)

        for file in os.listdir(self.__pathUsersTemp): #Movendo arquivos temporários dos usuários para a pasta DataBase\User
            try:
                os.rename(self.__pathUsersTemp+os.sep+file, self.__pathUsersDataBase+os.sep+file[:-3]+'aed')
            except:
                os.remove(self.__pathUsersDataBase+os.sep+file[:-3]+'aed')
                os.rename(self.__pathUsersTemp+os.sep+file, self.__pathUsersDataBase+os.sep+file[:-3]+'aed')

        for file in os.listdir(self.__pathUsersDeleted): #Excluindo da pasta DataBase\User arquivos referênciados para serem apagados
            try:
                os.remove(self.__pathUsersDataBase+os.sep+file+'.aed')
            except:
                pass

        for file in os.listdir(self.__pathUsersDeleted): #Excluindo referências de arquivos a serem deletados (Usuários)
            os.remove(self.__pathUsersDeleted+os.sep+file)
        
        #archive = open('databooks.aed', 'wb')
        #pickle.dump(self.__booksDataBase, open('databooks.aed', 'wb'))
        #pickle.dump(self.__booksDataBase, archive)
        #archive.close()

        for file in os.listdir(self.__pathBooksTemp): #Movendo arquivos temporários dos Livros para a pasta DataBase\Book
            try:
                os.rename(self.__pathBooksTemp+os.sep+file, self.__pathBooksDataBase+os.sep+file[:-3]+'aed')
            except:
                os.remove(self.__pathBooksDataBase+os.sep+file[:-3]+'aed')
                os.rename(self.__pathBooksTemp+os.sep+file, self.__pathBooksDataBase+os.sep+file[:-3]+'aed')

        for file in os.listdir(self.__pathBooksDeleted): #Excluindo da pasta DataBase\Book arquivos referênciados para serem apagados
            try:
                os.remove(self.__pathBooksDataBase+os.sep+file+'.aed')
            except:
                pass

        for file in os.listdir(self.__pathBooksDeleted): #Excluindo referências de arquivos a serem deletados (Livros)
            os.remove(self.__pathBooksDeleted+os.sep+file)
        
        #archive = open('datausers.aed', 'wb')
        #pickle.dump(self.__usersDataBase, open('datausers.aed', 'wb'))
        #pickle.dump(self.__usersDataBase, archive)
        #archive.close()

        os.chdir('DataBase')
        pickle.dump(self.__superUser, open('superuser.aed', 'wb'))
        pickle.dump(self.__maxBooks, open('maxbooks.aed', 'wb'))
        pickle.dump(self.__inviteBook, open('invitebook.aed', 'wb'))

        self.rootPath()

    #Carrega banco de dados.
    def loadDataBase(self):
        self.rootPath()
        self.createSystemPath()
        
        for file in os.listdir(self.__pathUsersTemp): #Excluindo arquivos Temporários (Usuários)
            os.remove(self.__pathUsersTemp+os.sep+file)
        for file in os.listdir(self.__pathBooksTemp): #Excluindo arquivos Temporários (Livros)
            os.remove(self.__pathBooksTemp+os.sep+file)

        for file in os.listdir(self.__pathUsersDeleted): #Excluindo referências de arquivos a serem deletados (Usuários)
            os.remove(self.__pathUsersDeleted+os.sep+file)
        for file in os.listdir(self.__pathBooksDeleted): #Excluindo referências de arquivos a serem deletados (Livros)
            os.remove(self.__pathBooksDeleted+os.sep+file)

        if('DataBase' in os.listdir()):
            os.chdir('DataBase')
            try:
                self.__superUser, self.__maxBooks, self.__inviteBook = pickle.load(open('superuser.aed', 'rb')), pickle.load(open('maxbooks.aed', 'rb')), pickle.load(open('invitebook.aed', 'rb'))
            except:
                self.rootPath()
                if(len(os.listdir('DataBase')) > 2):
                    return print('Erro ao carregar banco de dados. Favor verificar a integridade dos arquivos.')
        self.rootPath()
        self.__currentUserTable = '' #Ao carregar o banco de dados e ter uma tabela de um elemento excluido carregada, onde a exclusão não foi salva, evita que o elemento excluido não seja impedido de ser acessado.
        self.__currentBookTable = '' #Ao carregar o banco de dados e ter uma tabela de um elemento excluido carregada, onde a exclusão não foi salva, evita que o elemento excluido não seja impedido de ser acessado.
        
#############################################################
if(__name__ == '__main__'):
    from random import randint, choice
    listalivros = open('Lista Nova.txt', 'r').read().split('\n')
    limite = len(listalivros)#100
    bli = Bibliotec(RBTree)
    letras = []
    livros = []
    usuarios = []
    devolucao = [None]*(limite//2)
    disciplinas = ('História', 'Geografia', 'Matemática', 'Português', 'Biologia', 'Química', 'Física', 'Informática', 'Arte', 'Sociologia', 'Filosofia', 'Inglês')
    #bli.loadDatabase()

    for x in range(97,123):
        letras.append(chr(x))

    for x in range(limite):#Registrando livros
        '''nome = ''
        for y in range(randint(5,15)):#Criando nome do livro.
            if(y%2 == 0):
                nome+= choice(letras)
            else:
                nome+= choice(['a','e','i','o','u'])
        '''
        #livros.append([str(nome).capitalize(), choice(disciplinas)])
        ##bli.registerBook(str(nome).capitalize(), ISBNRandom(), randint(1, 50))
        #bli.registerBook(str(nome).capitalize(), ISBNRandom(), randint(1, 50), livros[x][1])
        livros.append([listalivros[x], choice(disciplinas)])
        bli.registerBook(listalivros[x], ISBNRandom(), randint(1, 50), livros[x][1])
        
    #bli.reportBooks()

    for x in range(limite):#Cadastrando usuários
        nome = ''
        for y in range(randint(5,20)):#Criando nome de usuário
            if(y%2 == 0):
                nome+= choice(letras)
            elif(x%y == 1):
                nome += ' '
            else:
                nome+= choice(['a','e','i','o','u'])
        y = CPFRandom()
        usuarios.append(str(y))
        bli.signupUser(str(y),nome.capitalize())
    
    for x in range(limite//2): #Usuário pedindo livros.
        devolucao[x] = [choice(usuarios),choice(livros)]
        bli.approveRequestBook(devolucao[x][0], devolucao[x][1][0], devolucao[x][1][1])
    '''
    for x in devolucao[:len(devolucao)//2]: #Devolvendo livro
        #print(x)
        bli.refundBook(x[0], x[1])
    '''
        
    bli.reportBooks()
    bli.reportUsers()
    bli.saveDataBase()
    #print(CPFVerify(input('Insira o CPF: ')))
