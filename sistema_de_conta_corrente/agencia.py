
from random import randint

class Agencia:    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nivel recomendado, Caixa Atual: {}'.format(self.caixa))
        else:
           print('O valor de caixa está ok. Caixa atual {}'.format(self.caixa)) 
           
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor,cpf,juros))
        else:
            print("Emprestimo não é possivel. Dinheiro não disponível em caixa")
            
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
        
        
        
# Ao criar uma subclasse sem o metodo init, ela vai herdardtodos os parametros da superclasse (classe pai)
class AgenciaVirtual(Agencia):
    
    # CUIDADO, AO DEFINIR UM METODO INIT EM UMA SUBCLASSE, ELE SUBSTITUI O METODO INIT DA CLASSE PRINCIPAL, 
    # JOGANDO FORA TODA A HERANÇA DA CLASSE PAI SE NÃO FOR COLOCADO O METODO super().__init__
    def __init__(self, site, telefone, cnpj): #aqui estou definindo que preciso dos dados telefone e o cnpj. que serão diferentes da superclasse (classe pai)
        self.site = site
        super().__init__(telefone, cnpj, 1000)  # ESSE MÉTODO super().__init__ GARANTE QUE TODOS OS PARAMETROS DA CLASSE PAI (SUPERCLASSE) SEJAM HERDADOS. 
        # no caso estou definindo que todas as agencias terão um numero de agencia com numero 1000, e herdando as propriedades telefone e cnpj da superclasse
        self.caixa = 7000000
        self.caixa_paypal = 0
        
    def depositar_paypal(self,valor):
        self.caixa -= valor
        self.caixa_paypal += valor
    
    def sacar_paypal(self,valor):
        self.caixa += valor
        self.caixa_paypal -= valor
        

class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 90000000 
        
    def adicionar_cliente(self, nome, cpf, patrimonio):
        # O método adicionar_cliente adiciona clientes na agencia virtual,agencia comum, 
        # mas na agencia premium esse método só vai adicionar clientes que tenham patrimonio acima de 1000000. ISSO É POLIMORFISMO
        if patrimonio > 1000000:
            super().adicionar_cliente( nome, cpf, patrimonio)
            print("Cliente adicionado com sucesso")
        else:
            print("O cliente não tem o patrimonio minimo necessário para entrar na Agencia Premium")   
     


# O if __name__ == '__main__': permite que eu rode os meus testes somente como script, ou seja, somente nesse arquivo.
# ao executar o arquivo main esses testes não serão rodados no arquivo main
if __name__ == '__main__':
    # PROGRAMA
    agencia1 = Agencia(222222, 654654, 4568)
    agencia1.caixa = 100000000
    agencia1.verificar_caixa()
    agencia1.emprestar_dinheiro(1500, 123123123, 0.1)
    print(agencia1.emprestimos)
    agencia1.adicionar_cliente('lira', 123123123, 70000)
    agencia1.adicionar_cliente('Rodrigo', 123123123, 500000)
    print(agencia1.clientes)

    agencia_virtual_1 = AgenciaVirtual( 34341254, 23232323, 1234)
    agencia_virtual_1.caixa = 60000
    print("Caixa agencia Virtual 1")
    agencia_virtual_1.verificar_caixa()

    # agencia_comum_1 = AgenciaComum( 34341254, 23232323)
    # print("Caixa agencia Comum 1")
    # agencia_comum_1.verificar_caixa()

    # agencia_premium_1 = AgenciaPremium( 34341254, 23232323, 1234)
    # agencia_premium_1.caixa = 6000000
    # print("Caixa agencia Premium")
    # agencia_premium_1.verificar_caixa()

    agencia_virtual_2 = AgenciaVirtual( "www.agenciavirtual2.com.br", 23232323, 1234)
    print("Caixa agencia Virtual 2")
    agencia_virtual_2.verificar_caixa()
    print(agencia_virtual_2.site)
    # agencia_virtual_2(__dict__)
    print(agencia_virtual_2.__dict__)

    agencia_premium_2 = AgenciaPremium( 34341254, 23232323) #não precisa mais do numero de conta, pois ja está gerando automaticamente na subclasse AgenciaPremium
    agencia_premium_2.caixa = 6000000
    print("Caixa agencia Premium 2")
    agencia_premium_2.verificar_caixa()

    # # TESTANDO O METODO DE TRANSFERENCIAS ENTRE CAIXA PAYPAL E CAIXA AGENCIA
    agencia_virtual_3 = AgenciaVirtual( "www.agenciavirtual3.com.br", 23232323, 1234)
    print("Caixa agencia Virtual 3 PAYPALL")
    agencia_virtual_3.verificar_caixa()
    print(agencia_virtual_3.site)
    print(agencia_virtual_3.caixa)
    agencia_virtual_3.depositar_paypal(20000)
    print(f'Esse é o caixa da ag virtual 3 apos o deposito na conta PAYPALL: {agencia_virtual_3.caixa}')
    print(f'Esse é o caixa da CONTA PAYPALL da ag virtual 3 apos o deposito do caixa da agencia na conta PAYPALL: {agencia_virtual_3.caixa_paypal}')
    print(agencia_virtual_3.__dict__)


    # ADICIONANDO CLIENTE PREMIUM APOS A CONDIÇÃO DE PATRIMONIO MINIMO DE 1 MILHAO DE REAIS (na agencia premium-2)
    agencia_premium_2.adicionar_cliente('RODRIGO', 8560045961, 5000000 ) #( nome, cpf, patrimonio)
    print(agencia_premium_2.clientes)
    # O método adicionar_cliente adiciona clientes na agencia virtual,agencia comum, 
    # mas na agencia premium esse método só vai adicionar clientes que tenham patrimonio acima de 1000000. ISSO É POLIMORFISMO








        
