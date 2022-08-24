#Questão 03 - Faça um programa que peça o raio de um círculo, calcule e mostre a sua área usando a biblioteca MATH.

import math

raio = int(input("Digite o valor do raio do círculo: "))

print(f"A área do círculo é:  {pow(raio,2)* math.pi}")