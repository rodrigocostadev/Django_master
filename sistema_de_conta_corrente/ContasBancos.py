

class ContaCorrente:
    # VARIÁVEL DE CLASSE: ela é comum a todos os objetos daquela classe. Isso significa que qualquer alteração no valor da variável de classe 
    # afeta todas as instâncias da classe e suas subclasses, a menos que a variável seja sobrescrita de forma específica em uma instância.
    # cartao = 'gold' # essa é uma variavel de classe, e vai ser comum a todas as classes herdadas a partir dela. seria como se fosse uma variavel global a todas as classes
    
    def __init__(self,nome,cpf,agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None        
        self.agencia = agencia       # parametro criado apos o programa ja estar rodando (ver explicação abaixo no comunicado: MUITO IMPORTANTE)
        self.num_conta = num_conta   # parametro criado apos o programa ja estar rodando (ver explicação abaixo no comunicado: MUITO IMPORTANTE)
        
    def consultar_saldo(self):
        print ('Seu saldo atual é de R${:,.2f}'.format(self.saldo))
        # print(f'Seu saldo é de {self.saldo} reais')
        
    def depositar(self,valor):
        self.saldo += valor
        
    def _limite_conta(self):   # (((( MÉTODO PRIVADO ))) "tem um underline", é um método auxiliar a classe, só serve para ser usado dentro do programa
        self.limite = -1000    # permite ficar com 1000 reais no negativo
        return self.limite
        
    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Voce não tem saldo sufciente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor
        # self.saldo -= valor
        
    def consultar_limite_chequeespecial(self):
        print('seu limite de Cheque Especial é de R${:,.2f}'.format(self._limite_conta()))
        
# Programa
conta_lira = ContaCorrente("Lira","111.222.333-45","334","1502")
print(conta_lira.cpf)
conta_lira.consultar_saldo()

#depositando dinheiro na conta
conta_lira.saldo = 10000
conta_lira.depositar(4000)
conta_lira.consultar_saldo()

#sacando dinheiro na conta
conta_lira.sacar_dinheiro(10500)
conta_lira.consultar_saldo()

print("Saldo Final:")
conta_lira.consultar_saldo()
conta_lira.consultar_limite_chequeespecial()


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
