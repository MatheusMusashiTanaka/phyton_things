num = -5

if num == 0:
    print("o numero é zero")
else:
    if num > 0:
        print("o numero é positivo")
    else:
        print("o numero é negativo")


numero = 7

if numero % 2 == 0:
    print("par")
else:
    print("impar")


x=8

if x == 0:
    print("o numero é zero")
else:
    if x > 0 and x % 2 == 0:
        print("o numero é positivo e par")
    elif x>0 and x % 2 != 0:
        print("o numero é positivo e impar")
    if x < 0 and (x * -1) % 2 == 0:
        print("o numero é negativo e par")
    elif x < 0 and (x*-1) % 2 != 0:
        print("o numero é negativo e impar")