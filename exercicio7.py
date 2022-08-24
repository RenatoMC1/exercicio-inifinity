peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))
IMC = peso / pow(altura, 2)

if IMC <= 18.5:
    print(f"Você está abaixo do peso, pois seu IMC é {round(IMC,2)}")
elif 18.5 < IMC < 24.9:
    print(f"Você está com peso normal,pois seu IMC é {round(IMC,2)}")
elif 25 < IMC < 29.9:
    print(f"Você está sobrepeso, pois seu IMC é {round(IMC,2)}")
elif 30 < IMC < 39.9:
    print(f"Você está Obeso Tipo I, pois seu IMC é {round(IMC,2)}")

else:
    print(f"Alerta: Obesidade móbida, pois seu IMC é {round(IMC,2)}")
