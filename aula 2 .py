numero = float(input("numero: "))


if numero < 0:
    numero = -numero
    float(print(numero))
elif numero == 0:
    float(print(numero))
else:
    float(print(numero))
_______________________________________________________
#tarefa 2 limites de intervalo

a = int(input("a: "))
b = int(input("b: "))

if b>a:
    temp_a = a
    a = b
    b = temp_a
print(f"intervalo:[{a},{b}]")
______________________________________________________

#tarefa 3

print( "Formula da equação: aX^2+bX+c=0 ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print(f"soma = {-b/c}")
print(f"produto = {c/a}")
______________________________________________
#tarefa 4

vel = float(input("velocidade: "))

if vel > 80:
    multa = (vel - 80.0) * 5
    print(f"multado por R${multa}")
    ______________________________________________
 #tarefa 5
num = int(input("Numero : "))

if num % 2 == 0:
    print("par")
else:
    print("impar")
__________________________________________________
#tarefa 7

N = 4
if N %2 ==0:
    M = N * 2
else :
    N = N + 1
    M = M * 2
print (N,M)
