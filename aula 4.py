palavra = ''

while True:
    letra = str(input("escreva uma letra (digite espaço para parar): "))
    palavra += letra
    if letra == " " :
        break
print(f'Você escreveu: {palavra}')

palavra = str(input("frase: "))
conv = palavra.replace(" ", "")
print (conv)
