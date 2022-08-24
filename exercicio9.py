time_1 = input("Digite o 1º time: ")
Qtde_gols_time_1 = int(input("Digite a quantidade de gols do 1º time: "))
time_2 = input("Digite o 2º time: ")
Qtde_gols_time_2 = int(input("Digite a quantidade de gols do 2º time: "))

if Qtde_gols_time_1 > Qtde_gols_time_2:
    print(f"O time que ganhou foi {time_1} por {Qtde_gols_time_1} x {Qtde_gols_time_2}!")

elif Qtde_gols_time_1 < Qtde_gols_time_2:
    print(f"O time que ganhou foi {time_2} por {Qtde_gols_time_2} x {Qtde_gols_time_1}!")

else:
    print(f"Ninguém ganhou, foi empate de {Qtde_gols_time_2} x {Qtde_gols_time_1}!")