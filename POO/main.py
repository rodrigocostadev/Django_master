class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'infinita'

# qualquer função dentro de uma classe sempre tem que ter o primeiro parametro como self,
# pois self é uma instancia da propria classe
    def fazer_ligações(self):
        print('Fazendo ligação ...')
    def jogar_snake(self):
        print('Jogando snake ...')
    def despertador(self):
        print('Despertando ...')
    def calcular(self, v1,v2):
        return v1 + v2


# variavel celular passa a ser uma instancia da classe Celular
celular = Celular()

print(celular.marca)
print(celular.modelo)
print(celular.tem_camera)
print(celular.bateria)

celular.fazer_ligações()
celular.jogar_snake()
celular.despertador()
print(celular.calcular(2,4))
