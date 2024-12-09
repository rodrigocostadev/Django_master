

class ContaCorrente:
    
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        
    def consultar_saldo(self):
        print ('Seu saldo atual é de R${:,.2f}'.format(self.saldo))
        # print(f'Seu saldo é de {self.saldo} reais')
        
    def depositar(self,valor):
        self.saldo = valor
        
    def _limite_conta(self):   # (((( MÉTODO PRIVADO ))) "tem um underline", é um método auxiliar a classe, só serve para ser usado dentro do programa
        self.limite = -1000    # permite ficar com 1000 reais no negativo
        return self.limite
        
    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Voce não tem saldo sufciente para sacar esse valor')
            self.consultar_saldo
        else:
            self.saldo -= valor
        # self.saldo -= valor
        
    def consultar_limite_chequeespecial(self):
        print('seu limite de Cheque Especial é de R${:,.2f}'.format(self._limite_conta()))
        
# Programa
conta_lira = ContaCorrente("Lira","111.222.333-45")
print(conta_lira.cpf)
conta_lira.consultar_saldo()

#depositando dinheiro na conta
conta_lira.saldo = 10000
conta_lira.consultar_saldo()

#sacando dinheiro na conta
conta_lira.sacar_dinheiro(10500)
conta_lira.consultar_saldo()

print("Saldo Final:")
conta_lira.consultar_saldo()
conta_lira.consultar_limite_chequeespecial()


