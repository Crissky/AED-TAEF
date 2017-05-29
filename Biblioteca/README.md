# Edson Fagner da Silva Cristovam

### Algoritmos e Estrutura de Dados - BSI – 2016.2 

### Professor Tiago Alessandro Espinola Ferreira 

#### Universidade Rural Federal de Pernambuco, Recife, PE 
 
 
## Biblioteca: Verificando Livros 

*O objetivo do programa é ser um banco de dados que armazena o cadastro de alunos, livros e o empréstimo dos livros para os alunos cadastrados.*
 
##### Armazenamento 

O programa é dividido em módulos. O módulo New_RB_Tree é responsável por armazenar os dados em uma estrutura de Árvore Vermelho e Preto. Ele importa do módulo New_Binary_Tree a classe responsável por armazenar os dados, que são pesquisados através de chaves.
 
##### Gerenciamento 

O módulo Bibliotec_dynamic_table é responsável de gerenciamento dos dados armazenados nas árvores. 
Os livros são agrupados por disciplinas, onde cada disciplina é uma Árvore Vermelho e Preto. 
Os usuários são agrupados em Árvores Vermelho e Preto nomeadas com os três primeiros dígitos do CPF. 
O programa carrega somente uma árvore de livros e uma de usuários por vez. Isso é feito para uma menor utilização de memória em banco de dados grandes, este ganho sobrepõe o processamento extra que esse método exige. 
As manipulações feitas são salvas em arquivos temporários, onde serão efetivamente salvas quando a função saveDataBase é chamada. Caso não se queira manter as alterações e retornar ao último estado salvo, a função loadDataBase realiza está operação. 
Este módulo também é responsável por gerar relatórios dos livros, com a quantia total e em estoque, assim como relatório de usuários com seus respectivos CPFs, nome e livros em sua posse. Os relatórios são armazenados em arquivos de texto (.txt). 
 
##### Autenticação 

O módulo Authenticator é responsável por verificar se os CPFs e ISBNs inseridos são válidos. É utilizado aritmética modular para verificar se os dígitos verificadores são compatíveis com a sequência numérica que os precedem.
Quebra de Página
 
##### Interface 

Windows é o módulo responsável pela interface gráfica, onde algumas variáveis estão contidas no módulo Variables. Essas variáveis são responsáveis pelas fontes e cores usadas na interface. 
 
![Figura 1 - Tela de Login](https://github.com/Crissky/AED-TAEF/blob/master/Biblioteca/Biblioteca%20(Prints)/Tela%20de%20Login.PNG)

**Figura 1 - Tela de Login**
 
![Figura 2 - Tela de Cadastro de Usuário](https://github.com/Crissky/AED-TAEF/blob/master/Biblioteca/Biblioteca%20(Prints)/Tela%20de%20Cadastro%20de%20Usu%C3%A1rio.PNG)

**Figura 2 - Tela de Cadastro de Usuário**
 
 
![Figura 3 - Tela de Usuário (Seleção de Categoria)](https://github.com/Crissky/AED-TAEF/blob/master/Biblioteca/Biblioteca%20(Prints)/Tela%20de%20Usu%C3%A1rio%20(Escolha%20de%20Livro%20-%2001).PNG)

**Figura 3 - Tela de Usuário (Seleção de Categoria)**
 
![Figura 4 - Tela de Usuário (Seleção de Livro)](https://github.com/Crissky/AED-TAEF/blob/master/Biblioteca/Biblioteca%20(Prints)/Tela%20de%20Usu%C3%A1rio%20(Escolha%20de%20Livro%20-%2002).PNG)

**Figura 4 - Tela de Usuário (Seleção de Livro)**
 
 
![Figura 5 - Tela do Administrador](https://github.com/Crissky/AED-TAEF/blob/master/Biblioteca/Biblioteca%20(Prints)/Tela%20de%20ADM.PNG)

**Figura 5 - Tela do Administrador**
 
![Figura 6 - Tela de cadastro de livros](https://github.com/Crissky/AED-TAEF/blob/master/Biblioteca/Biblioteca%20(Prints)/Tela%20de%20Cadastro%20de%20Livros.PNG)

**Figura 6 - Tela de cadastro de livros**
 
 
##### Login 

As senhas dos usuários não são armazenadas no banco de dados, o que fica armazenado é o hash para comparação no momento do login. O responsável pelo armazenamento e comparação é o módulo Bibliotec_dynamic_table, que utiliza o módulo CripHash para gerar o hash. O hash gerado consiste em sete blocos de seis caracteres que representa um número inteiro em base quarenta e dois, o módulo Base42 responsável por converter o hash da base dez para a base quarenta e dois utilizando o alfabeto: 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Δ Θ Π Σ Ψ Ω. 
 
##### Diretórios 

Ao ser carregado, o programa cria todas as pastas necessárias para o seu funcionamento. Na pasta DataBase é armazenado os arquivos salvos. Todos os arquivos são salvos em binário. 
invitebook.aed contém a lista de pedido a serem aprovados. 
maxbooks.aed contém o número máximo de livros que um usuário pode ficar simultaneamente. 
superuser.aed contém o registro de se um administrador já foi cadastrado. 
Dentro do diretório DataBase existem dois diretórios, Book e User, onde ficam armazenados as Árvores com os livros e com os usuários respectivamente. 
Reports é o diretório onde os relatórios são salvos. 
Temp é o diretório que contém quatro diretórios que armazenam arquivos temporários. 
Book armazena as árvores dos livros. 
User armazena as árvores de usuários. 
DBook armazena as árvores de livros que serão deletadas. 
DUser armazena as árvores de usuários que serão deletadas. 
Image armazena as imagens e ícone utilizado na interface gráfica. Esse diretório não é criado pelo sistema. 
 
##### Auto-completar 

Na tela de cadastro de livros, o campo categoria utiliza o recuso de auto completar do módulo Autocomplete que mostra sugestões de categorias com base no que foi digitado e nas categorias já existentes. 
