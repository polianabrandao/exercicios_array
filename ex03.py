qtdalunos = int(input('Quantos alunos são? '))
nomes = []
for x in range(qtdalunos):
    nomes.append(input('Digite os nome do aluno: '))

posicao = input('Digite um nome para achar sua posição: ')

if posicao in nomes:
    print(f'{posicao} está na posiçao {x}')