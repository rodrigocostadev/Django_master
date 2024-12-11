from ContasBancos3 import ContaCorrente, CartaoCredito
from agencia import AgenciaPremium

# Programa
# conta_lira = ContaCorrente("Lira","111.222.333-45","334","1502")

# cartao_lira = CartaoCredito('Lira', conta_lira)
# print(cartao_lira.titular)
# print(cartao_lira.conta_corrente._num_conta) #pegou os parametros definidos na classe ContaCorrente

# print(cartao_lira.conta_corrente._num_conta)
# # print(conta_lira._cartoes[0].numero)
# print(conta_lira.cartoes)
# print(cartao_lira.validade)
# print(cartao_lira.numero)
# print(cartao_lira.cod_seguranca)

# # conta_lira._saldo = 1000000
# # print("esse é o novo saldo lira")
# # print(conta_lira._saldo)

# cartao_lira.senha = '12' # vai imprimir nova senha invalida pela RESTRIÇÃO DE 4 DIGITOS PARA SENHA 
# print(cartao_lira.senha)

# # __dict__ é um metodo para verificar todas as informações da classe (Aula 25)
# print(conta_lira.__dict__)
# print(cartao_lira.__dict__)

agencia_premium_3 = AgenciaPremium(22222,11111)
print(agencia_premium_3.caixa)
