
clientes = ['Ana','Jonas','Felipe','Cláudio','Renato']

def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}')    

# FOR serve para iterar quando voce sabe que tem um limite de itens para iterar
for cliente in clientes:
    envia_email(cliente)

# a função enumerate alem de retornar o item vai retornar o indice, que foi chamado de "i"
for i, cliente in enumerate(clientes):
    print(i, cliente)

for i, cliente in enumerate(clientes):
    if i ==2:                 
        break          # a utilização do break interrompe o laço de repetição tanto em for quanto em while
    envia_email(cliente)

for i, cliente in enumerate(clientes):
    if i ==2:                 
        continue
    # Utilização do continue: vai executar envia_email(cliente) 1 vez i=0, segunda vez i=1, 
    # quando for iterar a tercerira vez( i=2 ) vai:
    # executar o continue, NÃO vai executar o envia_email(cliente) (que está abaixo de continue), 
    # e vai iterar o próximo elemento da lista clientes, sendo assim "pulando" o indice 2,
    # resumindo, vai imprimir que o email foi enviado para Ana, Jonas, (Vai pular felipe e não vai imprimir nada) Claudio, Renato     
    envia_email(cliente)


# WHILE serve para iterar quando voce sabe que não tem limite ou controle de iterações, 
# que ele DEPENDE DE UMA CONDIÇÃO,
# como uma expressão booleana, "ex: vai iterar enquanto for verdadeiro"
numero = 0

while numero < 5:
    # if numero ==2:                 
    #     break          # a utilização do break interrompe o laço de repetição tanto em for quanto em while
    print(numero)
    numero += 1

