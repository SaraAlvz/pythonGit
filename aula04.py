#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

# idade= int(input("digite sua idade:")) 
# if idade >= 18:
#     if idade > 120:
#         print("idade invalida")
#     else:
#         print("maior de idade")
# else:
#     if idade < 0:
#         print("idade invalida")
#     else:
#         print("menor de idade")

#     idade= 18
# if int(input("digite sua idade:"))>= idade:
#     print("maior de idade")
# else:
#     print("menor de idade")

# email= (input ("digite seu email:"))
# senha= (input("digite sua senha:"))
# if email == "python@senai.com" and senha == "12345678":
#     print("USUÁRIO ENCONTRADO")
# else:
#     print("USUÁRIO OU SENHA INVÁLIDOS")

# print("="*15, "SUPERMARKET", "="*15)
# print("R$: 0.30 -> MENOS QUE UMA DUZIA")
# print("R$: 0.25 -> PELO MENOS DOZE")
# quantidade= int(input("Digite a quantidade de maçazinhas:"))
# if quantidade < 12:
#     print(f"{quantidade} maças: R$ 0.30 unidade, TOTAL -> {quantidade*0.30}" )
# else:
#     print(f"{quantidade} maças: R$0.25 unidade, TOTAL -> {quantidade*0.25}")

# letra= input("digite uma letra:").lower()
# if letra == "a" or letra == "e" or letra== "i" or letra =="o" or letra=="u": 
#     print("Você digitou uma vogal!")
# else:
#     print("Você digitou uma consoante!")

#reescrevendo de outra maneira
#upper() -> CONVERTER TUDO PARA MAIUSCULO
#lower() -> CONVERTER TUDO PARA MINUSCULO

num1= float(input("Digite um número:"))
num2= float(input("Digite outro número:"))
if num1 > num2:
    print(f"Número maior: {num1}")
    print(f"Número menor: {num2}")
else:
    print(f"Número maior: {num2}")
    print(f"Número menor: {num1}")