num1 = int(input("Digite um número inteiro e positivo: "))
num2 = int(input("Digite outro número inteiro e positivo: "))
pergunta = input("Qual operação que você deseja (+ - * /)? ")

soma = num1+num2
subtracao = num1-num2
multiplicacao = num1*num2
divisao = num1/num2

if pergunta == "soma":
    print(f"A soma é {soma}")
elif pergunta == "subtracao":
    print(f"A subtração é {subtracao}")
elif pergunta == "multiplicacao":
    print(f"A multiplicacao é {multiplicacao}")
elif pergunta == "divisao":
    print(f"A divisão é {divisao}")
else:
    print("Você não digitou uma operação válida")



