
# MÉTODO NORMAL
numeros = [1,2,3,4,5]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero*2)
print(numeros_dobrados)


# COM COMPRESSÃO DE LISTAS
numeros2 = [1,2,3,4,5]
numeros_dobrados2 = [numero *2 for numero in numeros2]
print(numeros_dobrados2)


# COM COMPRESSÃO DE LISTAS de outra forma
numeros3 = [1,2,3,4,5]
def dobro(numero):
    return numero *2
numeros_dobrados3 = [dobro(numero) for numero in numeros3]
print(numeros_dobrados3)


# COMPRESSÃO DE LISTAS COM STRING
nomes = ['ana','felipe','joao','arlindo','carlos']
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)


# COMPRESSÃO DE LISTAS COM STRING
nomes = ['ana','felipe','joao','arlindo','carlos']
nomes_maiusculos = [nome.upper() for nome in nomes if nome[0] == 'a']
print(nomes_maiusculos)