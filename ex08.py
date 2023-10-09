nome = []
senha = []
for x in range(5):
    nome.append(input('Digite um nome: '))
    senha.append(int(input('Digite a senha: ')))
senha_login = int(input('Digite a senha do login: '))

if senha_login in senha:
    for x in senha:
        print(f'Olá, {nome[x]}! Login efetuado com sucesso!')