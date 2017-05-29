from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import os

class GuiAdmin:
	def __init__(self, master):
		self.__janela = master
		#self.__janela.configure(background = 'DarkGreen') 
		self.__janela.bind('<Escape>', lambda event:self.quitConfirm(self.__janela))
		self.cont = StringVar(value=0)	
		self.ListboxVariavel = StringVar(value=("Códigos..."))
		self.tmpinserido = 0
		self.widgue()

	def widgue(self):

		style = ttk.Style()
		style.configure("TFrame", background="#333")

		self.janelaFrame1 = ttk.Frame(self.__janela, style = "TFrame")
		self.janelaFrame1.pack(fill=BOTH, expand=True)

		self.base_img = PhotoImage(file='images%sOffice-Apps-MS-Office-Upload-Center-Metro-icon96.png'%os.sep)
		self.base_img2 = PhotoImage(file='images%sOther-Notifications-Metro-icon.png'%os.sep)

		self.Button1 = Button(self.janelaFrame1, image=self.base_img, bg='#F6961B', activebackground="#333", bd=0, command=lambda:self.InsertCode())
		self.Button1.place(x=195, y=20)

		self.Button2 = Button(self.janelaFrame1, image=self.base_img2, bg='#009F3C', activebackground="#333", bd=0,command=lambda:self.ListarCode())
		self.Button2.place(x=195, y=170)


		self.listaBox = Frame(self.__janela, width=160, height=278, bg="#333")
		self.listaBox.place(x=345, y=20)

		self.contidade = Spinbox(self.listaBox, from_=1, to=100, state='readonly',textvariable=self.cont).pack(fill=X)

		self.lista = Frame(self.listaBox, height=17, bg="#333").pack(fill=X)

		self.lbox = Listbox(self.listaBox, listvariable=self.ListboxVariavel,font=('Consolas','10','bold') , height=15, bg='#666',fg='#ccc', selectbackground='#F6961B')
		
		self.scrollbar = Scrollbar(self.listaBox,bd=0)

		self.lbox.config(yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.lbox.yview)

		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.lbox.pack()
		

		self.janelaFrame2 = Frame(self.__janela)
		self.janelaFrame2.pack(side=TOP, fill=X)

		self.validateMsg = ttk.Label(self.janelaFrame2, relief=SUNKEN, text='Status', font=('Consolas', '8', 'bold'))
		self.validateMsg.pack(fill=X)

	def InsertCode(self):
		self.tmpinserido = self.cont.get()
		url = 'http://localhost/check'
		post_fields = {'user':'Admin','command':'insert','tam':self.tmpinserido} 
	
		try:
			request = Request(url, urlencode(post_fields).encode())
			json = urlopen(request).read().decode()
			self.validateMsg['text'] = json
			#print(json)
		except Exception as e:
			self.validateMsg['text'] = e
	
		
	def ListarCode(self):
                
		url = 'http://localhost/check'
		post_fields = {'user':'Admin','command':'lista','tam':self.tmpinserido} 
	
		try:
			request = Request(url, urlencode(post_fields).encode())
			json = urlopen(request).read().decode()
			
			#self.validateMsg['text'] = json

			
			self.ListboxVariavel.set(json.split(','))
			
			
	
		except Exception as e:
			self.validateMsg['text'] = e
		
	def priTam(self):
		print(self.cont.get())


	def quitConfirm(self, master):
		self.quitConfirmBox = messagebox.askquestion('Sair?','Realmente deseja sair?')
		if(self.quitConfirmBox == 'yes'):
			master.destroy()
		else:
			del self.quitConfirmBox



def main(width=300, height=200):
	root = Tk()
	root.geometry('%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth()/2) - (width/2), (root.winfo_screenheight()/2) - (height/2)))
	root.overrideredirect(True) 
	GuiAdmin(root)
	root.mainloop()


if __name__ == '__main__':
	main(700,350)
