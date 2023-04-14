lista = []
while True:
    num = int(input("Digite um numero: "))
    if num < 0:
        break
    if num not in lista:
        lista.append(num)

print(f'seus numeros digitados (sem repetição) foram: {lista}')
