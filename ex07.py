nome = []
senha = []
for x in range(5):
    nome.append(input('Digite um nome: '))
    senha.append(int(input('Digite a senha: ')))
for x in range(5):
    print(f'O usuário {nome[x]} com senha {senha[x]} está na posição {x} do vetor.')