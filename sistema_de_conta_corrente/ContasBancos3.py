from datetime import datetime
import pytz #módulo que faz o ajuste de fusohorário (python time zone)
from random import randint

class ContaCorrente:
    
    @staticmethod # O @staticmethod sinaliza que esse é um metodo estático, ou seja, 
    # esse metodo não pega nenhuma informação da classe como parametro ou metodo, até por isso ele não utiliza o self
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        # return horario_BR
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
    
    def __init__(self,nome,cpf,agencia, num_conta):
        self._nome = nome
        self._cpf = cpf               
        self._saldo = 0
        self._limite = None        
        self._agencia = agencia       # parametro criado apos o programa ja estar rodando (ver explicação abaixo no comunicado: MUITO IMPORTANTE)
        self._num_conta = num_conta   # parametro criado apos o programa ja estar rodando (ver explicação abaixo no comunicado: MUITO IMPORTANTE)
        self._transacoes = []   # O UNDERLINE depois de self. indica que esses parametros devem ser usados e acessados somente por metodos da classe e não podem ser acessados diretamente, somente por metodos
        self.cartoes = []       #está sem underline pois é acessado por outra classe
        
    def consultar_saldo(self):
        print ('Seu saldo atual é de R${:,.2f}'.format(self.saldo))
        # print(f'Seu saldo é de {self.saldo} reais')
        
    def depositar(self,valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        
    def _limite_conta(self):   # (((( MÉTODO PRIVADO ))) "tem um underline", é um método auxiliar a classe, só serve para ser usado dentro do programa
        self.limite = -1000    # permite ficar com 1000 reais no negativo
        return self.limite
        
    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Voce não tem saldo sufciente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        # self.saldo -= valor
        
    def consultar_limite_chequeespecial(self):
        print('seu limite de Cheque Especial é de R${:,.2f}'.format(self._limite_conta()))
        
    def consultar_historico_transacoes(self):
        print("Histórico de Transações:")
        print("Valor, Saldo, Data e Hora") 
        for transacao in self.transacoes:
            print(transacao)
    
    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor 
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

class CartaoCredito:
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        # return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
        return horario_BR        
    
    def __init__(self, titular, conta_corrente): #tudo o que eu posso escolher está sendo usado como parametro inicial, tudo o que é gerado automaticamente não é declarado aqui inicialmente
        self.numero = randint(1000000000000000,9999999999999999) #define um numero randomico entre 10000... ate 99999...
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4) # adiciona 4 anos a data de validade.       #CartaoCredito._data_hora().month
        # self.cod_seguranca = randint(000,999) #alguns codigos de cartoes começam com 0, mas dessa forma ele não vai gerar o numero 0 inicialmente, ex 047 = vai gerar 47
        self.cod_seguranca = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9)) # vai gerar 3 numeros aleatórios para o cod. seg. com a possibilidade de aparecer o 0
        self.limite = None
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
        self.senha = '1234'        
        
    # método get para definir que a senha tenha no minimo 4 digitos ( RESTRIÇÃO DE 4 DIGITOS PARA SENHA )
    @property #o @property torna a minha função senha uma propriedade/atributo       
    def senha (self):
        return self._senha
        
    @senha.setter # método set para definir que a senha tenha no minimo 4 digitos ( RESTRIÇÃO DE 4 DIGITOS PARA SENHA )
    def senha(self,valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova Senha Invalida")
            
        
        # USO DE UNDERLINE NO INIT:
        # então usar o underline antes do parametro não deixa ele inacessivel? vou poder acessar ele diretamente? 
        # o uso do underline é somente para indicar que o melhor uso para ele é através de metodo?

        # O ChatGPT disse:
        # ChatGPT
        # Exatamente! O uso do underline (como em _saldo) no Python não torna o atributo inacessível. 
        # Ele não é protegido ou oculto como em outras linguagens, como Java ou C++, que realmente implementam modificadores de acesso como private ou protected. 
        # O underline em Python é apenas uma convenção para indicar que o atributo ou método é "privado" ou "protegido", 
        # ou seja, é um aviso para que os desenvolvedores evitem acessá-lo diretamente, mas ainda assim é acessível diretamente.
     
     
     
# O if __name__ == '__main__': permite que eu rode os meus testes somente como script, ou seja, somente nesse arquivo.
# ao executar o arquivo main esses testes não serão rodados no arquivo main
if __name__ == '__main__':   
    # Programa
    conta_lira = ContaCorrente("Lira","111.222.333-45","334","1502")

    cartao_lira = CartaoCredito('Lira', conta_lira)
    print(cartao_lira.titular)
    print(cartao_lira.conta_corrente._num_conta) #pegou os parametros definidos na classe ContaCorrente

    print(cartao_lira.conta_corrente._num_conta)
    # print(conta_lira._cartoes[0].numero)
    print(conta_lira.cartoes)
    print(cartao_lira.validade)
    print(cartao_lira.numero)
    print(cartao_lira.cod_seguranca)

    # conta_lira._saldo = 1000000
    # print("esse é o novo saldo lira")
    # print(conta_lira._saldo)

    cartao_lira.senha = '12' # vai imprimir nova senha invalida pela RESTRIÇÃO DE 4 DIGITOS PARA SENHA 
    print(cartao_lira.senha)

    # __dict__ é um metodo para verificar todas as informações da classe (Aula 25)
    print(conta_lira.__dict__)
    print(cartao_lira.__dict__)


