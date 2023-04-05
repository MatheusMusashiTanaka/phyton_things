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
    
    #tarefa 6
    
    N = 3
    M = 5
    if N-M >0:
        M = M - N
    else:
        N= M-N
     print(N,M)
__________________________________________________
#tarefa 7

N = 4
if N %2 ==0:
    M = N * 2
else :
    N = N + 1
    M = M * 2
print (N,M)
___________________________________________________
#tarefa 8
Nota_1= float(input("nota 1: "))
Nota_2= float(input("nota 2: "))

Media = Nota_1/Nota_2

if Media >= 7:
    print("Aprovado")
elif Media > 10 or Media < 0
    print("notas invalidase")
else:
    print("reprovado")
____________________________________________
#tarefa 9

nota_1 = float(input("Nota 1 : "))
nota_2 = float(input("Nota 2 : "))
teste = float(input("teste : "))

media_pon = ((nota_1 * 0.3) + (nota_2*0.3) + (teste*0.4))


if media_pon > 10 or media_pon < 0 :
    print("notas erradas")
elif media_pon >= 7:
    print("aprovado")
else:
    print("reprovado")
___________________________________________
#tarefa 10
tempo = int(input("minutos estacionados: "))

if tempo <= 15:
    print("gratis")
elif tempo < 60:
    print("R$ 3,00")
elif tempo >= 60:
    print("R$ 6,00")
 ____________________________________
#tarefa 11

dist = int(input("distancia em km: "))

if dist <= 200:
    custo = dist * 0.5
    print(f'você pagara R${custo}')
elif dist <= 400:
    custo = dist * 0.45
    print(f'você pagara R${custo}')
elif dist > 400:
    custo = dist * 0.4
    print(f'você pagara R${custo}')

          



