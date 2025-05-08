import os
os.system
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
# SWITCH CASE -> (match case) escolha caso (a partir da versão 3.10)
#match valor:
# case valor:

# linguagem = 100

# match linguagem:
#     case "python":
#         print("é facil")
#     case "java" :
#         print("muito codigo, python faz com linhas menores")
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")
#     case "html":
#         print("kauã não dorme")
#     case 10:
#         print("entrou aqui!")
#     case _:
#         print("outro caso")


# semana= input("Digite o numero da semana 1 a 7:")

# match semana:
#     case "1":
#         print("segunda")
#     case "2":
#         print("terça")
#     case "3":
#         print("quarta")
#     case "4":
#         print("quinta")
#     case "5":
#         print("sextouu")
#     case "6":
#         print("sabadouu")
#     case "7":
#         print("domingouuu")
#     case _:
#         print("larga de ser burro(a) pq eu pedi até 7!!")

# print(""" MUNDO DO CELULAR
# 1- IPHONE 15 - R$: 5000,00
# 2- XIOMI REDMI 13 PRO PLUS 512GB - R$ 2500,00
# 3- SAMSUNG S25 265GB - R$ 6999,99
#     FRETE: SP -> 10,00
#            MG -> 15,00
#            RS -> 20,00
# """)

# produto= input("Digite o número do produto:")
# estado= input("Digite a sigla do estado:").upper()
# print("*"*20)
# preco= 0
# frete= 0

# match estado:
#     case "SP":
#       frete= 10
#     case "MG":
#       frete= 15
#     case "RS":
#       frete= 20

# match produto:
#     case "1":
#       preco= 5000
#     case "2":
#       preco= 2500
#     case "3":
#       preco= 6999.99



# print(f"PREÇO R$: {preco}")
# print(f"FRETE R$: {frete}")
# print(f"TOTAL R$: {preco+frete}")

import random
robo = random.randint(1,3) #gera de 1 ate 99 aleatoriamente

print("="*10,"JOGO PEDRA PAPEL TESOURA","="*10)

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

jogador= input("Digite pedra/papel/tesoura:").lower()

match robo:
    case 1:
        robo = papel
    case 2:
        robo = pedra
    case 3:
        robo = tesoura

match jogador:
    case "pedra":
        jogador = pedra
    case "papel":
        jogador = papel
    case "tesoura":
        jogador = tesoura

print(f"ROBO: {robo}")
print(f"JOGADOR: {jogador}")


match jogador:
    case _ if jogador == pedra and robo == pedra:
        print("EMPATOU!!")
    case _ if jogador == pedra and robo == papel:
        print("ROBO VENCEU!")
    case _ if jogador == pedra and robo == tesoura:
        print("JOGADOR VENCEU!")
    case _ if jogador == papel and robo == papel:
        print("EMPATOU!!")
    case _ if jogador == papel and robo == tesoura:
        print("ROBO VENCEU!")
    case _ if jogador == papel and robo == pedra:
        print("ROBO VENCEU!")
    case _ if jogador == tesoura and robo == tesoura:
        print("EMPATOU!")
    case _ if jogador == tesoura and robo == papel:
        print("JOGADOR VENCEU!")
    case _ if jogador == tesoura and robo == pedra:
        print("ROBO VENCEU!")



