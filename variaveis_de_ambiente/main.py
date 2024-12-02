import api
import os

# metodo tradicional:
# usuario = 'pycodebr'
# senha = '1234'

# SETANDO VARIÁVEIS DE AMBIENTE
# $env:USUARIO_API = 'pycodebr'     -> para setar uma variavel de ambiente (variavel de usuário)
# $env:SENHA_API = '1234'           -> para setar uma variavel de ambiente (variavel de senha)
# echo $env:SENHA_API               -> para verificar o valor da variavel de ambiente (vai mostrar no terminal o valor)

# apos setar as variaveis de ambiente, 
# importar o modulo OS, que é um modulo nativo em python para interagir com o sistema operacional

# definir usuario e senha com a variavel de ambiente
usuario = os.environ.get('USUARIO_API')
senha = os.environ.get('SENHA_API')
ambiente = os.environ.get('AMBIENTE')

print(usuario)
print(senha)

login = api.login(usuario,senha)
print(login)

# $env:AMBIENTE = 'dev'  
if ambiente == 'dev':
    print(api.envia_email_log())