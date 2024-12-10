
from datetime import datetime
import pytz #módulo que faz o ajuste de fusohorário (python time zone)

class ContaCorrente:
    # VARIÁVEL DE CLASSE: ela é comum a todos os objetos daquela classe. Isso significa que qualquer alteração no valor da variável de classe 
    # afeta todas as instâncias da classe e suas subclasses, a menos que a variável seja sobrescrita de forma específica em uma instância.
    # cartao = 'gold' # essa é uma variavel de classe, e vai ser comum a todas as classes herdadas a partir dela. seria como se fosse uma variavel global a todas as classes
    
    """
    Cria um objeto conta corrente para gerenciar as contas dos clientes
    atributos:
        nome: Nome do Cliente
        cpf: cpf do cliente
        agencia: numero da conta corrente do cliente
        num_conta: numero da conta
        saldo: saldo disponivelna conta do cliente
        limite: limite de cheque especial daquele cliente
        transacoes: historico de transações        
    """
    
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
        
        # self.__limite = None  # O UNDERLINE DUPLO indica que esse parametro só é utilizado nessa classe e não pode ser instanciado por outras classes que o herdam, 
        # e o torna inacessível para o lado de fora,impossibilitando o acesso desse parametro por outros usuários (o python vai esconder esse parametro)
        
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
        
        
# Programa
conta_lira = ContaCorrente("Lira","111.222.333-45","334","1502")
print(conta_lira.cpf)
conta_lira.consultar_saldo()

#depositando dinheiro na conta
conta_lira.saldo = 10000
conta_lira.depositar(4000)
conta_lira.consultar_saldo()

#sacando dinheiro na conta
conta_lira.sacar_dinheiro(500)
conta_lira.consultar_saldo()

print("Saldo Final:")
conta_lira.consultar_saldo()
conta_lira.consultar_limite_chequeespecial()

print('-' * 20)
# print(conta_lira.transacoes)
conta_lira.consultar_historico_transacoes()

print('-' * 20)
conta_maeLira = ContaCorrente('beth','3333.4444.555-6','555','64656667')
conta_lira.transferir(1500, conta_maeLira)

print("saldo lira:")
conta_lira.consultar_saldo()
conta_lira.consultar_historico_transacoes()

print("saldo mae-lira:")
conta_maeLira.consultar_saldo()
conta_maeLira.consultar_historico_transacoes()



# MUITO IMPORTANTE!!!
# Tomar cuidado ao editar os parametros do init, pois depois que o programa ja estiver rodando e for preciso fazer alterações no init, vai derrubar o sistema, 
# então os parametros do init tem que ser bem pensados quando forem criados 

# EXEMPLO:
# o programa anteriormente iniciava tendo que informar somente nome e cpf:
# conta_lira = ContaCorrente("Lira","111.222.333-45") 
# mas se depois o programa estiver funcionando eu quiser alterar o init adicionando os parametros conta e agencia 
# vai dar problema para todos os outros usuarios que antes usavam somente nome e cpf, vai aparecer um erro de que faltam 2 argumentosm (conta e agencia)

# QUAIS EDIÇÕES POSSO FAZER OU NÃO NO INIT DA CLASSE?
# NÃO POSSO FAZER: Criar um novo parametro no init vai dar problema
# POSSO FAZER: Criar um novo metododa minha classe
# POSSO FAZER: Adicionar uma coisa ou outra no meu metodo ja existente não da problema ( DESDE QUE NÃO IMPEÇA QUE O PROGRAMA CONTINUE FUNCIONANDO)