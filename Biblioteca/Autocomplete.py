from tkinter import *
import re

class Autocomplete(Entry):
    def __init__(self, dictionary, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.dictionary = dictionary
        self.text = StringVar()
        self["textvariable"] = self.text
        
        self.text.trace('w', lambda name, index, mode: self.written(*args, **kwargs))
        self.bind("<Return>", lambda event: self.selects())
        self.bind("<Right>", lambda event: self.selects())
        self.bind("<Up>", lambda event: self.up())
        self.bind("<Down>", lambda event: self.down())
        self.bind("<FocusIn>", lambda event: self.written(*args, **kwargs))
        self.bind("<FocusOut>", lambda event: self.destroyListbox())
        
        self.listBoxExist = False

    def written(self, *args, **kwargs):
        if self.text.get() == '':
            try:
                self.listBox.destroy()
                self.listBoxExist = False
            except:
                pass
        else:
            words = self.compare()
            if words:
                if self.listBoxExist == False:
                    self.listBox = Listbox(*args, **kwargs)
                    #self.listBox.bind("<Button-1>", lambda event: self.selects())
                    self.listBox.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())

                    self.listBoxExist = True
                
                self.listBox.delete(0, END)
                for x in words[:10]:
                    self.listBox.insert(END,x)
            else:
                if self.listBoxExist:
                    self.listBox.destroy()
                    self.listBoxExist = False
        
    def selects(self):
        if self.listBoxExist:
            self.text.set(self.listBox.get(ACTIVE))
            self.listBox.destroy()
            self.listBoxExist = False
            self.icursor(END)

    def up(self):
        if self.listBoxExist:
            #Evita erro na primeira chamada
            if self.listBox.curselection() == ():
                index = '0'
            else:
                index = self.listBox.curselection()[0]

            #Sobe uma seleção
            if index != '0':
                self.listBox.selection_clear(first=index)
                index = str(int(index)-1)
                self.listBox.selection_set(first=index)
                self.listBox.activate(index)

            #Salta para o final
            if self.listBox.curselection() == ():
                self.listBox.selection_clear(first=END)
                self.listBox.selection_set(first=END)
                self.listBox.activate(END)
            
    def down(self):
        if self.listBoxExist:
            #Evita erro na primeira chamada
            if self.listBox.curselection() == ():
                index = '-1'
            else:
                index = self.listBox.curselection()[0]
                
            #Desce uma seleção
            if index != END:
                self.listBox.selection_clear(first=index)
                index = str(int(index)+1)
                self.listBox.selection_set(first=index)
                self.listBox.activate(index)

            #Retorna ao Topo
            if self.listBox.curselection() == ():
                index = '0'
                self.listBox.selection_clear(first=index)
                self.listBox.selection_set(first=index)
                self.listBox.activate(index)

    def destroyListbox(self):
        try:
            self.listBox.destroy()
            self.listBoxExist = False
        except:
            pass
    
    #Gera lista com as palavras possíveis
    def compare(self):
        pattern = re.compile(self.text.get()+'.*', re.IGNORECASE)
        return [x for x in self.dictionary if pattern.match(x)]

if __name__ == '__main__':
    root = Tk()
    root.geometry('300x450')
    dictionary = ['a', 'abertura', 'acarreta', 'acima', 'acumuladas', 'agrega',
             'alavancagem', 'alternativas', 'análise', 'ao', 'aos', 'aponta',
             'apropriadas', 'as', 'assim', 'atitudes', 'atividade',
             'atribuições', 'atual', 'auxiliam', 'avanço', 'cada', 'capitais',
             'cenário', 'certificação', 'com', 'como', 'complexidade',
             'comunicação', 'condições', 'conduta', 'consenso', 'considerar',
             'consolidação', 'consulta', 'correntes', 'costumes', 'criação',
             'cumpre', 'da', 'das', 'de', 'demonstram', 'departamental',
             'desafiador', 'desenvolvimento', 'devidamente', 'diretrizes',
             'dirigentes', 'diversas', 'diversos', 'do', 'dos', 'dúvidas',
             'e', 'efetuados', 'entre', 'esperado', 'essencial',
             'estabelecimento', 'estas', 'estrutura', 'estruturas', 'estudos',
             'eventualidades', 'experiências', 'facilita', 'faz', 'fenômeno',
             'formação', 'formulação', 'funcionais', 'fundamental', 'futuro',
             'geral', 'gerenciamento', 'globalizado', 'hierarquias',
             'imparcial', 'importante', 'incentivo', 'inegavelmente',
             'interessante', 'internacionais', 'internet', 'início',
             'julgamento', 'levantam', 'levar', 'lidar', 'longo', 'mais',
             'melhoria', 'mesmo', 'metodologias', 'militantes', 'mobilidade',
             'modernização', 'modo', 'motivação', 'mundo', 'na', 'necessidade',
             'no', 'normativas', 'nos', 'novas', 'níveis', 'o', 'obriga',
             'oferece', 'oportunidade', 'organização', 'ortodoxas', 'papel',
             'para', 'parte', 'pensamento', 'pensando', 'percebemos', 'pode',
             'ponderadas', 'posturas', 'prazo', 'processo', 'processual',
             'promove', 'proposições', 'quadros', 'qualificação', 'quanto',
             'que', 'questionar', 'questões', 'reestruturação', 'reformulação',
             'regras', 'relacionamentos', 'relatividade', 'relação',
             'remanejamento', 'renovação', 'representa', 'ressaltar', 'retorno',
             'revolução', 'se', 'sobre', 'soluções', 'suas', 'talvez',
             'tecnológico', 'todas', 'todavia', 'todo', 'tudo', 'um', 'uma',
             'valor', 'venha', 'verificação', 'verticais', 'vez', 'à', 'às',
             'é', 'órgãos']

    entry = Autocomplete(dictionary, root, font=('Consolas', '20'))
    entry.pack()
    entry.focus()
    
    root.mainloop()
