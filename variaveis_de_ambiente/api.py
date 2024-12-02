def login(usuario,senha):
    if usuario == 'pycodebr' and senha == '1234':
        return 'Login correto, voce está logado!'
    else:
        return 'Login incorreto, voce foi desconectado!'
    
def envia_email_log():
    return 'Email com log enviado'