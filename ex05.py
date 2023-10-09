a = []
x = []
m = 0
for y in range(10):
    a.append(int(input('Digite um número: ')))

x.append(int(input('Digite um número para multiplicar: ')))
print(a)
print(x)

for y in a:
    m = a[y] * x
    print(m)