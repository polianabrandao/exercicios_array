notas_alunos = []
soma = 0
aprovados = 0
notas = 0
for y in range(5):
    notas = float(input('Digite a nota: '))
    notas_alunos.append(notas)
    soma = soma + notas
print(soma)
media = soma / 5
for notas in notas_alunos:
    if notas >= media:
        aprovados += 1
print(notas_alunos)
print(f'Média: {media}')
print(f'Quantidade de alunos aprovados: {aprovados}')
