#tarefa 1
i = 1

while i<11:
    print(i)
    i+=1
__________________________________________________________
#tarefa 2

i = 2
while i <= 100:
    print(i)
    i= i + 2
__________________________________________________________  
#tarefa 3
n=10
while n >=0:
  print(n)
  n+=1
___________________________________________________________
#tarefa 4
n = int(input("numero: "))
x=1
while<=10:
  result = x*n
  print(result)
  x+=1
 _________________________________________________________
#tarefa 5
n=int(input("num: "))
x = n
while n!= 0:
  print(x)
  n=int(input("num: "))
 _______________________________________ 
#tarefa 6
num = int(input("numero: "))

while num != 0:
    if (num % 2) == 0:
        print("par")
    elif (num % 2) != 0:
        print("impar")
    
    num = int(input("numero (digite 0 para sair): "))
________________________________________
#tarefa 7
i = 1

while i <= 5:
    numero = int(input("numero: "))
    if numero < 0:
        print("numero é negativo")
    elif numero > 0:
        print("numero é positivo")
    i+=1
 _______________________________________
#tarefa 10
i = 1
soma=0
while i <= 100:
    soma += i
    i+=1
print (soma)
    
________________________________________
#tarefa 11
i=1
soma=0
while i <= 10:
    numero=int(input("digite numero: "))
    soma+=numero
    i+=1
print (f"soma :{soma}")
________________________________________
#tarefa 12
 i=0
soma=0
while i < 1000:
    soma+=i
    i+=5
print(soma)
________________________________________
#tarefa 13
soma = 0
while True:
    if soma >=1000:
        break
    numero = int(input("digite: "))
    soma += numero
print(soma)
________________________________________
#tarefa 14
div = 0
sum = 0
Med = 0
while True:
    num = int(input("Numero: "))
    sum+=num
    div+=1
    Med = (sum)/div
    print(f'Media: {Med}')
________________________________________
#tarefa 15

soma = 0
while True:
    numero = int(input("numero: "))
    if numero < 0:
        break
    soma += numero
print(soma)
_________________________________________
#tarefa 16
num = 0
sum = 0
while num >= 0:
    num = int(input("Numero(digite numero negativo para parar): "))
    
    if (num%2) == 0:
        sum+=num
    
print(sum)
______________________________________________
 #tarefa 17
  soma = 0
i=1

while i<=10:
    numero = int(input("numero: "))
    if numero < 0:
        soma+=1
    i+=1
print (f"foram digitados :{soma} numeros negativos")
print (soma)
________________________________________
#tarefa 18
numero = int(input("Numero: "))
divisores = 0
i = numero
while i > 0:
    if (numero % i) == 0:
        divisores+=1
    i-=1
print (divisores)
_______________________________________
#19

num = 0
sum = 0
while num >= 0:
    num = int(input("Numero(digite numero negativo para parar): "))
    
    if (num%2) == 0:
        sum+=1
    
print(f'foram digitados: {sum}')
_____________________________________________________________________
#tarefa 20
num = 0
par = 0
total = 0
while num >= 0:
    num = int(input("Numero(digite numero negativo para parar): "))
    
    if (num%2) == 0:
        par+=1
    if num >= 0:
        total+=1
print(f'A quantidade de pares foi de {(par/total)*100}%')
_________________________________________________
    #tarefa 21
    num = 0
par = 0
total = 0
while num >= 0:
    num = int(input("Numero(digite numero negativo para parar): "))
    
    if (num%2) == 0:
        par+=1
    if num >= 0:
        total+=1
print(f'A quantidade de pares foi de {(par/total)*100}%')
_________________________________________________________
#22

max = float('-inf')
i=1
while i<=5:
    num = int(input(f'numero {i}: '))
    if num>max:
        max = num
    i+=1
print(f'o maior valor foi : {max}') 


_________________________________________________________
#23
max = float('-inf')
i=1
while i<=5:
    num = int(input(f'nota {i}: '))
    if num < 0 or num > 10:
        raise ValueError("Nota deve ser entre 10 e 0")
    if num>max:
        max = num
    i+=1

print(f'o maior valor foi : {max}') 
_______________________________________________________
#24

num = 0

i=1

while i<=7:
    num = int(input("Digite temperatura ºC: "))
    if i == 1:
        menor = num
    if num<menor:
        menor = num
    i+=1
print(f'A menor temperatura da semana foi {menor}ºC')

ou

num = 0
menor = float('inf')
i=1

while i<=7:
    num = int(input("Digite temperatura ºC: "))
    if num<menor:
        menor = num
    i+=1
print(f'A menor temperatura da semana foi {menor}ºC')
_________________________________________________________
#25
_________________________________________________________
#26
_________________________________________________________
#27
i=1
for i in range (1,11):
    for mult in range (1,11):
        print(f'{i} x {mult} = {i*mult}')
____________________________________________________________
#28
i = 1
while True:
    num = int(input(f"Numero {i}: "))
    i += 1
    div = num
    while div > 0:
        if num % div == 0:
            print(f"o {num} é divisivel por {div}")
        div -= 1
    if num<0:
        break
    


