
class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5
    def acelerar(self):
        print("Acelerando ...")
    def frear(self):
        print("freando ...")
    def buzinar(self):
        print("buzinando ...")

# carro = Carro()
# carro.acelerar()
# carro.frear()
# carro.buzinar()

################## Criando uma nova classe pegando algumas caracteristicas da classe carro , mas SEM USAR A HERANÇA
class Uno:
    modelo = "Uno"
    marca = "Fiat"
    ano = 1992
    numero_rodas = 4
    quantidade_passageiros = 5
    def acelerar(self):
        print("Acelerando ...")
    def frear(self):
        print("freando ...")
    def buzinar(self):
        print("buzinando ...")

# uno = Uno()
# uno.acelerar()
# uno.frear()
# uno.buzinar()

################### Criando uma nova classe COM HERANÇA
class Uno_Fire(Carro):
    modelo = "Uno-fire"
    marca = "Fiatt"
    ano = 1994
    
unoFire = Uno_Fire()
print(unoFire.modelo)
print(unoFire.marca)
print(unoFire.ano)
unoFire.acelerar()
unoFire.frear()
unoFire.buzinar()

