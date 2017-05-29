# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi, cgitb
cgitb.enable()

from createcode import *
import pickle, os
from AVL_TREE3 import *
from random import *
from codify import *

class Server(BaseHTTPRequestHandler):


    if os.path.isfile('Codes_DataBase.lab'):
        database = pickle.load(open('Codes_DataBase.lab', 'rb'))
    else:
        database = AVLTree()
        pickle.dump(database, open('Codes_DataBase.lab', 'wb'))

    def do_GET(self):
        if self.path=="/":    
            output = ""
            output += "<!DOCTYPE html><html><head>"
            output +='<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">'
            output += "</head><body>"
            output += '''
                <div class="jumbotron text-center">
                  <h1>Check Codigo</h1>
                  <p>Verificador de Codigos Promocionais</p> 
                </div>
                <div class="container">
                <div class="form-group">
                    <form method='POST' enctype='multipart/form-data' action='/check'>
                         <div class="form-group">
                            <label for="Codigo">digite seu Codigo:</label>
                            <input name="code" type="text" class="form-control" id="Codigo" placeholder="Codigos">
                        </div>
                        <input type="submit" class="btn btn-success" value="Submit">
                    </form>
                </div>                
            '''  
            output += "</body></html>"

            self.setaTopo()
            self.wfile.write(output.encode(encoding = 'utf_8'))

    
    def do_POST(self):
        form = cgi.FieldStorage(fp=self.rfile,headers= self.headers,environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],})
        usuario = form.getvalue('user')
        
        if usuario == "Admin":
            command = form.getvalue('command')

            if command =='insert':
                tam = int(form.getvalue('tam'))

                listaMsg = []
                for i in range(0,tam):
                    listaMsg.append(self.insertCode())

                naoInsert = listaMsg.count(False)

                if naoInsert > 0:
                    msg = "Foram inseridos "+str(tam-naoInsert)+" de "+str(tam)
                else:
                    msg = "Total inserido "+str(tam)
        
                self.setaTopo()
                self.wfile.write(msg.encode(encoding = 'utf_8'))
            else:
                tam = int(form.getvalue('tam'))
                archivo = open("Lista de Códigos.txt","r")
                lista = archivo.read()
                archivo.close()

                lista = lista.replace("\n",",")
                lista = lista.split(',')
                lista.pop()
                lista.reverse()

                msg = ','.join(lista[0:tam])
        
                self.setaTopo()
                self.wfile.write(msg.encode(encoding = 'utf_8'))                       
                
        else:
            codigo = form.getvalue('code')
            outpute = self.checkCode(str(codigo))
            self.setaTopo()
            self.wfile.write(outpute.encode(encoding = 'utf_8'))

    def setaTopo(self, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()


    def checkCode(self, code):
        code = codify(code)
        status = self.database.search20(code)
        if(status != None):
            if(status.getData()['used'] < status.getData()['available']):
                status.getData()['used'] += 1
                pickle.dump(self.database, open('Codes_DataBase.lab', 'wb'))
                return "Código cadastrado com sucesso!"#'available'
            else:
                return 'Código já utilizado.'#'used'
        else:
            return 'Código inválido.'#'not found'

    def insertCode(self):
        code = createCode()
        hashcode = codify(code)
        inseriu = False
        tentativa = 0

        data = {"available": randint(0,5), 'used': 0}

        
        while inseriu == False and tentativa < 10:
            if(self.database.insert(hashcode, data) != 0):
                inseriu = True
                save = open('Lista de Códigos.txt', 'a')
                save.write(code+'\n')
                save.close()
                pickle.dump(self.database, open('Codes_DataBase.lab', 'wb'))
            else:
                tentativa +=1

        if inseriu:
            return True
        else:
            return False
        
    


def run(Host, Porta):
  server_address = (Host, Porta)
  httpd = HTTPServer(server_address, Server)
  httpd.serve_forever()

if __name__ == "__main__":
    run('127.0.0.1', 80)
