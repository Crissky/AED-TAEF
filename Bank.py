class Account:
    def __init__(self, number, agency):
        self.number = number
        self.agency = agency
        self.cash = 0

    def draw(self, value):
        if(self.cash-value > 0):
            print('Saldo insuficiente.')
        else:
            self.cash -= value
            print('seu novo saldo é de:', self.cash)

    def deposit(self, value):
        self.cash += value
        print('seu novo saldo é de:', self.cash)

    def getNumber(self):
        return self.number
    def getCash(self):
        return self.cash

class Client:
    def __init__(self, name, cpf, address, phone):
        self.name = name
        self.cpf = cpf
        self.address = address
        self.phone = phone
        self.account = []

    def addAcc(self, number, agency):
        self.x = Account(number, agency)
        self.account.append(self.x)

    def getName(self):
        return self.name
    def getCPF(self):
        return self.cpf
    def getAcc(self):
        return self.account[0]


class Bank:
    def __init__(self, bankAgency):
        self.clients = []
        self.numGenerator = '0'
        self.bankAgency = bankAgency

    def addNumGenerator(self):
        self.numGenerator = str(int(self.numGenerator)+1).rjust(16, '0')
        return self.numGenerator  

    def __str__(self):
        text = '\n=== Relatório de clientes ===\n\n'
        for y in range(len(self.clients)):
            text = text+'Nome: '+self.clients[y].getName()+'\n'+'CPF: '+self.clients[y].getCPF()+'\n'+'Conta: '+self.clients[y].getAcc().getNumber()+'\n'+'Saldo: '+str(self.clients[y].getAcc().getCash())+'\n\n'
        return text[0:-2]
            
    def addClient(self, name, cpf, address, phone):
        x = True
        for y in self.clients:
            if(y.getCPF() == cpf):
                x = False
                break
        if(x == True):
            self.x = Client(name, cpf, address, phone)
            self.x.addAcc(self.addNumGenerator(), self.bankAgency)
            self.clients.append(self.x)
        else:
            print('CPF',cpf, 'já cadastrado.')

    def searchCPF(self, cpf):
        for y in self.clients:
            if(y.getCPF() == cpf):
                return y
        print('CPF:', cpf,'não cadastrado.')
        return None
    
    def addCash(self, cpf, value):
        x = self.searchCPF(cpf)
        if(x != None):
            print(x.getName(), end=', ')
            x.getAcc().deposit(value)

    def subCash(self, cpf, value):
        x = self.searchCPF(cpf)
        if(x != None):
            print(x.getName(), end=', ')
            x.getAcc().draw(value)
         
if(__name__ == '__main__'):     
    bank = Bank('252627')
    bank.addClient('João das Neves','12345678900','Winterfell','8188564785')
    bank.addClient('Fagner Cristovam','98765432188','Paulista','2134333163')
    bank.addClient('Nick Westfield','15935785246','Westcamp','65988646657')
    bank.addClient('Maria Gonzaga','95175385287','Sertãozin','5787956432188')
    bank.addClient('Maria Severina','95175385287','Sertão','6855949487')
    print(bank)
