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
