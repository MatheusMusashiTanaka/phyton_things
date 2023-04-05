chuva = int(input("chuva? (1=y/0=n): "))

saia = "Saia de casa"
if chuva == 1:
    umbrela = int(input("voce tem um guarda chuva? (1=y/0=n): "))
    if umbrela==1:
        print(saia)
    else:
        print("espere um pouco")
        while chuva == 1:
            chuva = int(input("ainda esta chovendo? (1=y/0=n): "))
            if chuva == 0:
                print(saia)
            else:
                print("espere mais")
else:
    print(saia)
-----------------------------------------
import random

vitorias = 0
derrotas = 0
empates = 0

def cancelar(player):
    if player == "0":
        return True
    else:
        return False

while True:
    player = input("(p)edra, (pa)pel, (t)esoura, or (0) to cancel: ")
    
    if cancelar(player):
        break
    
    numero = random.randint(1, 3)

    if numero == 1:
        escolha = "pedra"
    elif numero == 2:
        escolha = "papel"
    else:
        escolha = "tesoura"
        
    if player == "p":
        if escolha == "pedra":
            print("Empate")
            empates += 1
        elif escolha == "papel":
            print('Derrota')
            derrotas += 1
        else:
            print('Vitoria')
            vitorias += 1
            
    elif player == "pa":
        if escolha == "pedra":
            print("Vitoria")
            vitorias += 1
        elif escolha == "papel":
            print('Empate')
            empates += 1
        else:
            print('Derrota')
            derrotas += 1
            
    elif player == "t":
        if escolha == "pedra":
            print("Derrota")
            derrotas += 1
        elif escolha == "papel":
            print("Vitoria")
            vitorias += 1
        else:
            print("Empate")
            empates += 1
    
    resultado = f"{vitorias},{derrotas},{empates}"
    print(resultado)
