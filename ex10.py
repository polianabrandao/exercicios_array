numeros = []
cont = 0
for n in range(10):
    numeros.append(int(input('Digite um número: ')))
numero_qualquer = int(input('Digite um número para saber se ele está na lista: '))
for n in range (10):
    if numero_qualquer in numeros:
        cont += 1
print(f'O número {numero_qualquer} aparece {cont} vezes.')
