

#EXPLICAÇÃO:
# FORMA é a minha classe base

class Forma():
    def area(self):
        pass

# Quadrado é uma classe especifica que eu criei e está herdando as propriedades de FORMA
class Quadrado(Forma):
    # DUNDER INIT ( __init__ ) :  É UM MÉTODO CONSTRUTOR DA MINHA CLASSE
    
    # DUNDER INIT é "COMO SE FOSSE" uma interface de entrada para dados, mas definitivae=mente ela não é uma interface de entrada no sentido tradicional, 
    # mas pode ser utilizado para configurar o estado inicial de um objeto com dados fornecidos ao criar a instância
    
    # POR QUE É CHAMADO DE POLIMORFISMO DE INTERFACE?
    # com o __init__ eu vou alterar a interface dessa classe, 
    # pra quando eu chamar ela no meu código eu vou conseguir passar parametros especificos pra ela, 
    # mesmo estando herdado caracteristicas de outra classe, no caso FORMA.
    def __init__(self,lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2


# DUNDER INIT é "COMO SE FOSSE" uma interface de entrada para dados, ela não é uma interface de entrada no sentido tradicional, 
# mas pode ser utilizado para configurar o estado inicial de um objeto com dados fornecidos ao criar a instância

# Quando eu chamar a minha classe ( Quadrado() ) e atribuir ela a uma variável ( quadrado), o método construtor (DUNDER INIT DA CLASSE QUADRADO) vai ser executado 
# e ele vai executar parametros que eu queira executar na criação de um objeto, como passar um parametro ( Lado).
# ENTÃO DEFININDO O DUNDER INIT NA MINHA CLASSE, EU CONSIGO DEFINIR QUAIS PARAMETROS SERÃO NECESSÁRIOS PARA EXECUTAR A MINHA CLASSE QUANDO ELA FOR CHAMADA OU INSTANCIADA, 
# como no exemplo abaixo:

quadrado = Quadrado(5)   # (agora a variável quadrado é uma instancia de Quadrado())
print(quadrado.area())

quadrado2 = Quadrado(7)   # (agora a variável quadrado2 é uma instancia de Quadrado())
print(quadrado2.area())

class Circulo(Forma):
    def __init__(self,raio):
        self.raio = raio
    def area(self):
            return 3.14 * self.raio **2
        
circulo = Circulo(4)   
print(circulo.area())

circulo2 = Circulo(6)   
print(circulo2.area())

          


# DEFINIÇÃO DE METODO CONSTRUTOR:
# É um metodo especial que é usado para inicializar um objeto instanciado  
# (É uma função que é executada automaticamente usando uma classe instanciada)
# ( quando crio um novo objeto a partir de uma classe, esse método é inicializado automaticamente)




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# EXPLICAÇÃO DO YOUTUBE SOBRE O METODO CONSTRUTOR __INIT__
# VIDEO:  https://www.youtube.com/watch?v=o_JHRtf-o-8

# class Gato2:
#     def __init__(self,nome):
#         self.nome = nome
#         print("seu gato se chama", self.nome)

# nome_gato = input("Digite o nome do seu gato: ")
# g1 = Gato2(nome_gato)

# Quando você usa o __init__, você está definindo como o objeto é criado, com um conjunto de dados que é configurado uma vez.



