qtdalunos = int(input('Quantos alunos são? '))
nomes = []
for x in range(qtdalunos):
    nomes.append(input('Digite os nome do aluno: '))
for x in range(qtdalunos):
    print(f'{nomes[x]} está na posição {x}')
