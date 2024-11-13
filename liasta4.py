# Classe simples com Getter e Setter
# class Pessoa:
#     def _init_(self, nome, idade):
#         self.__nome = nome                        # Atributo privado
#         self.__idade = idade                      # Atributo privado
                                                  
#     def get_nome(self):                           # Getter para o atributo 'nome'
#         return self.__nome

#     def set_nome(self, nome):                     # Setter para o atributo 'nome'
#         if isinstance(nome, str) and len(nome) > 0:
#             self.__nome = nome
#         else:
#             print("Nome inválido!")

#     def get_idade(self):                          # Getter para o atributo 'idade'
#         return self.__idade

#     def set_idade(self, idade):                   # Setter para o atributo 'idade'
#         if isinstance(idade, int) and idade > 0:
#             self.__idade = idade
#         else:
#             print("Idade inválida!")
                                   
# nome = input("Digite o nome: ")                   # Criando um objeto da classe Pessoa usando entrada do usuário
# idade = int(input("Digite a idade: "))

# pessoa = Pessoa(nome, idade)

#                                                   # Usando os getters para obter os valores
# print(pessoa.get_nome())                          # Exibe o nome fornecido
# print(pessoa.get_idade())                         # Exibe a idade fornecida
                                  
# novo_nome = input("Digite o novo nome: ")         # Usando os setters para modificar os valores com entrada do usuário
# pessoa.set_nome(novo_nome)

# nova_idade = int(input("Digite a nova idade: "))
# pessoa.set_idade(nova_idade)

#                                                   # Verificando as alterações
# print(pessoa.get_nome())                          # Exibe o novo nome
# print(pessoa.get_idade())                         # Exibe a nova idade

#                                                   # Tentando definir um valor inválido
# nome_invalido = input("Digite um nome inválido (por exemplo, um número): ")
# pessoa.set_nome(nome_invalido)                    # Tenta definir um nome inválido

# idade_invalida = int(input("Digite uma idade inválida (por exemplo, um valor negativo): "))
# pessoa.set_idade(idade_invalida)                  # Tenta definir uma idade inválida


# exercicio 1, 2, 3 

# class Pessoa:
#     def _init_(self,nome):
#         self.__nome = nome

#     def get_nome(self):
#         return self.__nome
    
#     def set_nome(self,nome):
#         if isinstance (nome,str) and len(nome) > 0:
#             self.__nome = nome
#         else:
#             print('Nome Invalido')

# # Testar a função
# abc = Pessoa('Joaqui 5555666n')
# print(abc.get_nome())

# abc.set_nome('Maria Joaquina')
# print(abc.get_nome())

# execicio 4

# class ContaBancaria:
#     def _init_(self, saldo):
#         self.__saldo = saldo if saldo >= 0 else 0  # Inicializa o saldo, garantindo que não seja negativo

#     # Método para depositar valor na conta
#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor
#         else:
#             print("Valor depositado inválido")

#     # Método para sacar valor da conta
#     def sacar(self, valor):
#         if 0 < valor <= self.__saldo:
#             self.__saldo -= valor
#         else:
#             print("Valor de saque inválido!")
    
#     # Método para obter o saldo atual
#     def get_saldo(self):
#         return self.__saldo

# # Testar código pela entrada de dados
# conta = ContaBancaria(1000)  # Inicializa a conta com saldo de 1000
# conta.depositar(500)  # Deposita 500 na conta
# print(conta.get_saldo())  # Exibe o saldo atual: 1500

# conta.sacar(2000)  # Tenta sacar 2000, mas o saldo é insuficiente

# print(conta.get_saldo())  # Exibe o saldo atual: 1500

# exercicio 5

# class Aluno:
#     def get__nota(self):
#         return self.get__nota
#     def set__nota(self, nota):
#         if 0 <= nota <= 10:
#             self.__nota =nota
#         else:
#             print(' nota invalida ')

# aluno = Aluno(' darcio', 0)
# print(aluno .get__nota())

# aluno.set__nota(9)
# aluno.set__nome(input(' digite um nome: '))
# print(aluno.get__nota(),aluno.get__nome())
    
# exercicio 6

# class Produto:
#     def __init__(self, preco): 
#         self.__preco = None
#         self.set_preco(preco)      
    
#     def get_preco(self):
#         return self.__preco
    
#     def set_preco(self,preco):
#         if preco > 0:
#            self.__preco = preco
        
#         else:
#             print('preco invalido!!!')
            
#     def get_produto(self): 
#         return self.__preco
            
# preco = float(200)
# preco1 = Produto(preco)

# print(preco1.get_preco())

# preco1.set_preco(int(input("digite produto : ")))
# print('valor do produto:  ',preco1.get_produto()) 

# exercicio 7

# class livro:
#     def __init__(self, autor, titulo):
#         self.__autor = autor
#         self.__titulo = titulo       
#     def get_autor(self):
#         return self.__autor
    
#     def set_autor(self,autor):
#         if isinstance (autor, str) and len(autor) > 0:
#            self.__autor = autor
        
#         else:
#             print('nome invalido!!!')
            
#     def get_titulo(self):
#         return self.__titulo
    
    
#     def set_titulo(self, titulo):
#         if isinstance (titulo, str) and len(titulo) >0:
#             self.__titulo = titulo
#         else:
#             print('invalida!!!')
 
# livros = livro('O pequeno príncipe ','Antoine de saint-exupéry ' )

# print(livros.get_autor())

# livros.set_autor(input("digite autor: "))
# livros.set_titulo(input("digite titulo do livro: "))
# print('Autor do livro: ',livros.get_autor(),'\ntitulo do livro', livros.get_titulo())


# exercicio 8

# class Funcionario:
#     def __init__(self, salario):
#         self.__salario = salario
             
#     def get_salario(self):
#         return self.__salario
    
#     def set_salario(self, salario):
#         if salario > 0:
#            self.__salario = salario
        
#         else:
#             print(' valor invalido!!!')
            
 
# funcionario = Funcionario(4500)

# funcionario.set_salario(float(input("digite salario: ")))
# print('salario do funcionario: ',funcionario.get_salario())

# exercicio 9

class Casa:
    def __init__(self, endereco, valor):
        self.__endereco = endereco
        self.__valor = valor      
    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self,endereco):
        if isinstance (endereco, str) and len(endereco) > 0:
           self.__endereco = endereco
        
        else:
            print('endereço invalido!!!')
            
    def get_valor(self):
        return self.__valor
    
    
    def set_valor(self, valor):
        if isinstance (valor, int) and len(valor) >0:
            self.__valor = valor
        else:
            print('valor invalido!!!')


enderecoCasa = Casa('Rua cora coralina  ', 0)  

print(enderecoCasa.get_endereco())

enderecoCasa.set_endereco(input("digite o endereco da casa: "))
enderecoCasa.set_valor(input("digite o valor da casa: "))
print('o endereco da casa é: ',enderecoCasa.get_endereco(),'\n o valor da casa é:', enderecoCasa.get_valor())







