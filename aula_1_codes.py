palavra = input("digite uma palavra: ")
numero = int(input("digite um numero: "))
palavra_1 = str(palavra)[:numero]
palavra_2 = str(palavra)[numero:]
print(palavra_1)
print(palavra_2)

__________________________________________________________________


nome = input('digite nome:')
numero_de_letras = len(nome)
print(numero_de_letras)
__________________________________________________________________


nome =input('digite nome: ') ; nome_invertido = str(nome[::-1]).upper()
print (nome_invertido)
___________________________________________________________________


nome = input('digite nome:')

palavras = nome.split(' ')

print(len(palavras))
print(palavras)
___________________________________________________________________


nota = float(input("nota: "))
if nota >= 7:
    print("aprovado")
else:
    print("reprovado")
___________________________________________________________________    


import random
numero = int(input("digite um numero de 1 a 10: "))

numero_premiado = random.randint(1,10)

while numero != 0:
    if numero_premiado == numero:
        print("Venceu!!")
        break
    else:
        print("tente novamente")
        numero = int(input("digite um numero de 1 a 10 (digite 0 para parar): "))
    
