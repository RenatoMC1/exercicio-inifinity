peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))
IMC = peso / pow(altura,2)

if IMC <= 18.5:
    print("Você está abaixo do peso")
elif 18.5 < IMC < 24.9:
    print("Você está com peso normal")
elif 25 < IMC < 29.9:
    print("Você está sobrepeso")
elif 30 < IMC < 39.9:
    print("Você está Obeso Tipo I")

else:
    print("Alerta: Obesidade móbida")