num2 = 5

while True:
    num1 = int(input("Digite um número entre 1 e 10: "))
    if num1 > num2:
        print("Seu número foi maior que o palpite")
        continue
    elif num1 < num2:
        print("Seu número foi menor que o palpite")
        continue
    else:
        print("você acertou")
        break

