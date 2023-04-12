#tarefa 1
_________________________________________________________________________________
#tarefa 2
palavra = ''

while True:
    letra = str(input("escreva uma letra (digite espaço para parar): "))
    palavra += letra
    if letra == " " :
        break
_________________________________________________________________________________
#tarefa 3
_________________________________________________________________________________

#tarefa 4 :

palavra = input("escreva seu nome: ")
count = palavra.lower().count('a')
print(f"seu nome tem {count} 'A's")
_________________________________________________________________________________
# tarefa 5

numero = input("digite um numero inteiro: ")
nums_sep = [int(num) for num in numero]
sum=0
for num_sep in nums_sep:
       sum += num_sep
       if num_sep <= 0:
        break
    
print(sum)

ou

conv = []
while True:
    sum = 0
    numero = input("numero inteiro (digite 0 para parar): ")
    if numero <= "0":
        break
    conv.append(int(numero))
    
    for num in conv:
        sum += num
    print(f"a soma dos numeros digitados ate agora é {sum}")
_________________________________________________________________________________
#tarefa 6
palavra = str(input("frase: "))
conv = palavra.replace(" ", "")
print (conv)
_________________________________________________________________________________
#tarefa 7

palavra = input("Frase : ")
sum = 0
for letra in palavra:
    if letra.lower() in 'aeiou':
        sum += 1

print(f'a frase que voce escreveu tem {sum} vogais.')
_________________________________________________________________________________
#tarefa 8
palavra = input("Frase : ")
sum = 0
for letra in palavra:
    if letra.lower() not in 'aeiou':
        sum += 1

print(f'a frase que voce escreveu tem {sum} consoantes.')


_________________________________________________________________________________
#tarefa 9 
nom = input("Nome completo: ")
nom_1 = nom.split(" ")
print(f'Seu primeiro nome é {nom_1[0]}')

_________________________________________________________________________________
#tarefa 10 :

letra = "mamão"
parte = ""
i = -1
while True:
    inv = letra[i]
    parte += inv
    if len(parte) == len(letra):
        break
    i-=1
print(parte)
