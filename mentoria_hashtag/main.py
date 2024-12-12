

class Vendedor():    
    def __init__(self,nome_vendedor):
        self.nome = nome_vendedor
        self.vendas = 0
        self.meta = 500
        self.bonus = 0        
    def vendeu(self, quantitade_vendas):
        self.vendas = quantitade_vendas
    def calcular_bonus(self):
        if self.vendas > self.meta:
            self.bonus = 30
        else:
            self.bonus = 0
            
        
vendedor1 = Vendedor("Lira")
vendedor1.vendeu(1500)
print(vendedor1.vendas)
# ((((( IMPORTANTE ))))) Eu poderia atribuir um valor dessa forma?: (vendedor1.vendas = 1500) em vez de (  vendedor1.vendeu(1500)  )??  --- (ATRIBUIR DIRETAMENTE EM VEZ DE USAR O MÉTODO)
# A resposta é: Poderia, não vai dar erro no código, MAS NÃO É O IDEAL , pois se o método vendeu possuir uma condicional if por exemplo, 
# não iria executar essa condicional, pois o metodo "vendeu" não foi executado, e digamos que daria problema no codigo caso alguma funcionalidade precisa-se dessa informação da condicional.

# PORTANTO quando quiser editar uma informação de uma classe, nunca deve-se editar diretamente um parametro, somente criando e usando metodos.
# Chamar os métodos são uma boa prática para alterar os valores
 
# Caso for preciso editar um parametro da classe principal, usando metodos todas as outras funcionalidades vão rodar normalmente, 
# e não vou precisar editar todo o meu código (precisaria de edição se eu usa-se atribuição direta), deixando como se fosse um código perpetuo (com pouca manutenção)



# 40 minutos de video da mentoria