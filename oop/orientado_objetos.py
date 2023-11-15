import sys

class Televisao():
    def __init__(self,marca,ano,n_canais,preco,propriedade):
        self.marca = marca
        self.ano = ano
        self.n_canais = n_canais
        self.preco = preco
        self.__propriedade = propriedade
        self.__ligada = False # O __ MOSTRAS A VARIAVEL COMO PRIVADA, O PYTHON SEMPRE DEIXARA VOCE ACESSAR E ALTERAR A VARIAVEL, MAS ISSO É UMA MA PRATICA

    @property
    def propriedade(self):
        return self.__propriedade

    def diminuir_canais(self):
        self.n_canais -= 1

    def aumente_canais(self,valor):
        self.n_canais += valor

    def ligar_tv(self):
        self.__ligada = True
        print("TV LIGADA")

    def desligar_tv(self):
        self.__ligada = False
        print("TV DESLIGADA")

    def __modelo_privado(self): #O __ É PARA DIZER QUE É PRIVADO, SO PODERA SER ACESSADO DE DENTRO DA CLASSE
        print("modelo privado")

    def acessar_modelo(self):
        self.__modelo_privado()
        return f"acessando modelo privado {self.__ligada}"
    
    def set_marca(self,marca):
        self.marca = marca

    def get_marca(self):
        return self.marca

    def set_ligada(self,valor):
        self.__ligada = valor

    def get_ligada(self):
        return self.__ligada

tv = Televisao("kk",2015,20,1905.89,"novas")
print(tv)
print(type(tv))

tv.acessar_modelo()
print(tv.propriedade)

lg =tv 
print(lg) #mesmo endereco de memoria, entao se alterar um o outro sera alterado tbm

lg = None #eliminar referencia de memoria

#tv.__modelo_privado()  #dara erro pois o metodo é privado

print(sys.argv)
sys.exit(1)

####################################################################################################################################################################

class Pessoa:
    _num_pressoas = 0

    def __init__(self,idade):
        self.__idade = idade
        Pessoa._num_pressoas += 1

    @staticmethod           #nao entra na herança
    def get_num_pressoas(): #nao se usa nada
        return Pessoa._num_pressoas
    
p1 = Pessoa(12)
p2 = Pessoa(18)
p3 = Pessoa(13)

class Pessoa:
    _num_pressoas = 0

    def __init__(self,idade):
        self.__idade = idade
        Pessoa._num_pressoas += 1

    @classmethod
    def get_num_pressoas(cls): #inves do self se usa o cls, pois se refere a classe, entra na herança
        return cls._num_pressoas
    
p1 = Pessoa(12)
p2 = Pessoa(18)
p3 = Pessoa(13)

####################################################################################################################################################################

class Funcionario():    #por padrao toda classe herda do tipo object, que contem metodos especificos de classes
    def __init__(self,nome,cpf,salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def mostrar_bonus(self):
        return self.salario * 0.10

class Gerente(Funcionario):
    def __init__(self,nome,cpf,salario,senha,qtd_funcionarios):
        super().__init__(nome,cpf,salario)              #usando o super voce inicializa a herança sem passar o self
        #Funcionario.__init__(self,nome,cpf,salario)    #usando a propria classe para herança voce precisar passar o self
        self.senha = senha
        self.qtd_funcionarios = qtd_funcionarios

    def validacao(self,senha):
        if self.senha == senha:
            print("Acesso valido")
            return True
        else:
            print("Acesso invalido")
            return False
        
    def mostrar_bonus(self):#metodo override
        return self.salario * 0.10 + self.qtd_funcionarios * 0.10
        
class Secretaria(Funcionario):
    def __init__(self,nome,cpf,salario,senha,qtd_gerentes):
        super().__init__(nome,cpf,salario)              #usando o super voce inicializa a herança sem passar o self
        self.senha = senha
        self.qtd_gerentes = qtd_gerentes
    
    def mostrar_bonus(self):    #metodo override
        return self.salario * 0.10 + self.qtd_gerentes * 0.10
    

