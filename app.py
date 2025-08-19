from classes import*
from func import*

menu()
resp1 = int(input("--> "))

while resp1 != 0:
    if resp1 == 1:
        limpar_e_pausar()
        menu_cadastro()
        tipo = int(input("--> "))

        print("Preencha as informações do animal:")
        nome = input("Nome: ")
        peso = input("Peso: ")
        idade = input("Idade: ")
        raca = input("Raça ou especie:")
        cor = input("Cor: ")
        dono = input("Nome do dono:")

        cadastro(tipo, nome, peso, idade, raca, cor, dono)
        print("Cadastro realizado com sucesso!")
    
    else:
        print(" ")
