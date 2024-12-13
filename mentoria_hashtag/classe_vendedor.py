
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////       EXEMPLO SEM USAR CLASSE:       /////////////////////////////////////////////////////
# VENDEDOR 1
vendedor__1 = "joao"
vendas = 1000
meta = 500

if vendas > meta:
    bonus = 20
else:
    bonus = 0
    
print("Vendedor:",vendedor__1, ",Vendeu: ", vendas, ",Bonus:", bonus)


vendedor__2 = "jose"
vendas = 300
meta = 500

if vendas > meta:
    bonus = 20
else:
    bonus = 0
    
print("Vendedor:",vendedor__2, ",Vendeu: ", vendas, ",Bonus:", bonus)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# obs: veja que a cada criação de um novo vendedor o codigo é duplicado, uma forma de não duplicar código é utilizando as classes. vejamos a seguir:



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////       EXEMPLO USANDO CLASSE:       /////////////////////////////////////////////////////

class Vendedor():    
    def __init__(self,nome_vendedor):
        self.nome = nome_vendedor
        self.vendas = 0
        self.meta = 500
        self.bonus = 0        
    def vendeu(self, quantitade_vendas):
        self.vendas = quantitade_vendas
        self.calcular_bonus() # Ao informar o valor das vendas, além de rodar a função normalmente, ele tambem roda a função que calcula o bonus
    def calcular_bonus(self):
        if self.vendas > self.meta:
            self.bonus = 30
        else:
            self.bonus = 0
            
        
vendedor1 = Vendedor("Lira")
vendedor1.vendeu(1500)
vendedor1.calcular_bonus()

vendedor2 = Vendedor("Rodrigo")
vendedor2.vendeu(300)
vendedor2.calcular_bonus()

print(vendedor1.nome, vendedor2.nome)
# print("Vendas:")
print(vendedor1.vendas,vendedor2.vendas)
# print("Bonus:")
print(vendedor1.bonus, vendedor2.bonus)

# ((((( IMPORTANTE ))))) Eu poderia atribuir um valor dessa forma?: (vendedor1.vendas = 1500) em vez de (  vendedor1.vendeu(1500)  )??  --- (ATRIBUIR DIRETAMENTE EM VEZ DE USAR O MÉTODO)
# A resposta é: Poderia, não vai dar erro no código, MAS NÃO É O IDEAL , pois se o método vendeu possuir uma condicional if por exemplo, 
# não iria executar essa condicional, pois o metodo "vendeu" não foi executado, e digamos que daria problema no codigo caso alguma funcionalidade precisa-se dessa informação da condicional.

# PORTANTO quando quiser editar uma informação de uma classe, nunca deve-se editar diretamente um parametro, somente criando e usando metodos.
# Chamar os métodos são uma boa prática para alterar os valores
 
# Caso for preciso editar um parametro da classe principal, usando metodos todas as outras funcionalidades vão rodar normalmente, 
# e não vou precisar editar todo o meu código (precisaria de edição se eu usa-se atribuição direta), deixando como se fosse um código perpetuo (com pouca manutenção)




