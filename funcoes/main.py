

pessoas = [
    {
        'nome':'Felipe',
        'email':'felipe@gmail.com'
    },
    {
        'nome':'jose',
        'email':'jose@gmail.com'
    },
    {
        'nome':'joao',
        'email':'joao@gmail.com'
    }
]

def envia_email(nome,email):
    return f'Email enviado para {nome}, dono(a) do email{email}'

for pessoa in pessoas: 
    email_enviado = envia_email(pessoa['nome'],pessoa['email'])
    print(email_enviado)