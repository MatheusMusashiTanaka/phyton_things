#tarefa 6

lista = []
while True:
    num = int(input("Digite um numero: "))
    if num < 0:
        break
    if num not in lista:
        lista.append(num)

print(f'seus numeros digitados (sem repetição) foram: {lista}')


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#tarefa 7

lista = []

for i in range(5):
    alt = float(input("altura em cm: "))
    pes = float(input("peso em kg: "))
    lista += [(alt, pes)]

iguais = ""

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] == lista[j]:
            iguais += (f' voce repetiu : {lista[i]} duas vezes')
    
print(iguais)
- - - - - - - - - - - - - - -- 
# tarefa 8
lista = []

while True:
    nom = str(input("Nome(digite um nome vazio para parar): "))
    if nom == "":
        break
    ida = int(input("idade em anos: "))
    lista += [(nom, ida)]

veio = lista[0]

for i in range(1, len(lista)):
    if lista[i][1] > veio[1]:
        veio = lista[i]
    

print(f'o mais velho é {veio[0]} com {veio[1]} anos')
_______________________________________
#tarefa 9

lista = [2, 4 ,1 ,11 ,111, 5, 8 ,9 ,4]
new_lista =[]

for x in lista:
    if x in [2,5,8,9,4}
             new_lista.append(x)
             
print(new_lista)
             
-------------------------------------------------------
#tarefa 10

lista = [22,15,68,99,63]
soma = 0
new_lista = []
for i in lista:
    if i % 2 == 0:
        soma +=1
        new_lista.append(i)
print(f'existe {soma} numeros pares ( {new_lista})')
________________________________________________________________
 #tarefa 11

nome = input("seu nome: ")
soma = 0
vogais = 'aeiou'

for letra in nome.lower():
    if letra in vogais:
        soma+=1
print(f' existe {soma} vogais')
 ______________________________________
#tarefa 12

for i in range(0,101):
    if i%2==0:
        print(i , end= " ")
 _______________________________________
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
