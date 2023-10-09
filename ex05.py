a = []
for y in range(10):
    a.append(int(input('Digite um número: ')))

x = int(input('Digite um número para multiplicar: '))
print(a)
print(x)

for y in a:
    m = a[y] * x
    print(f'{x} x {a[y]} = {m}')
