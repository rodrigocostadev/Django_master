# class Animal:
#     def emitir_som(self):
#         print("Qualquer som ...")

# class Cachorro(Animal):
#     def emitir_som(self):
#         print("Au Au!")

# class Gato (Animal):
#     def emitir_som(self):
#         print("Miau!")

# cachorro = Cachorro()
# cachorro.emitir_som()

# gato = Gato()
# gato.emitir_som()

# //////////////////////////////////////////////  MESMO EXEMPLO ANTERIOR SÓ QUE ALTERADO ///////////////////////////////////////////////////////////////////////

# class Animal:
#     def emitir_som(self, som="Qualquer som ..."):
#         print(som)

# class Cachorro(Animal):
#     def emitir_som(self, som="Au Au!"):
#         print(som)

# class Gato(Animal):
#     def emitir_som(self, som="Miau!"):
#         print(som)

# cachorro = Cachorro()
# cachorro.emitir_som()  # Usando o som padrão, "Au Au!"

# gato = Gato()
# gato.emitir_som()  # Usando o som padrão, "Miau!"

# # Agora podemos passar um argumento para sobrescrever o som
# gato.emitir_som("Hahaha")  # Sobrescreve o som padrão para "Hahaha"


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# AO EXECUTAR UM, COMENTE O OUTRO:
# exemplo de polimorfismo de classe do chat GPT

# class Animal:
#     def fazer_som(self):
#         pass

# class Cachorro(Animal):
#     def fazer_som(self):
#         return "Latir"

# class Gato(Animal):
#     def fazer_som(self):
#         return "Miar"

# animais = [Cachorro(), Gato()]
# for animal in animais:
#     print(animal.fazer_som())

