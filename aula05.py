import os 
os.system("cls")
#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#replace("valor1", "valor2") -> Substitui o valor 1 pelo valor2
#:.f -> formata para 2 casas decimais apenas no f{}

# nota1= float(input("digite a primeira nota:")).replace(",",".")
# nota2= float(input("digite a segunda nota:")).replace(",",".")
# media= (nota1+nota2)/2

# if media < 5:
#     print("Reprovado :(")
# elif media <= 7:
#     print("Em Recuperação :/")
# else:
#     print("Aprovado :)")


# peso= float(input("digite seu peso:").replace(",","."))
# altura= float(input("digite sua altura:").replace(",","."))

# imc= round(peso/(altura*altura),2)
# if imc < 17:
#     print("Muito abaixo do peso!")
# elif imc >= 17 and imc <= 18.49:
#     print("Abaixo do peso!")
# elif imc >= 18.5 and imc <= 24.99:
#     print("Peso normal!")
# elif imc >= 25 and imc <= 29.99:
#     print("Acima do peso!")
# elif imc >= 30 and imc <= 34.99:
#     print("Obesidade I!")
# elif imc >= 35 and imc <= 39.99:
#     print("Obesidade II!")
# else:
#     print("Obesidade III (MÓRBIDA)!!!")



print("="*10, "concessionária", "="*10)
print(r"""


    // | |     //   / /  /__  ___/     //   ) )     //   ) )     // | |     //   ) )
   //__| |    //   / /     / /        //   / /     //           //__| |    //___/ /
  / ___  |   //   / /     / /        //   / /     //           / ___  |   / ___ (
 //    | |  //   / /     / /        //   / /     //           //    | |  //   | |
//     | | ((___/ /     / /        ((___/ /     ((____/ /    //     | | //    | |


""")
salario= float(input("Digite o seu salário:"))
aumA= round(salario*0.20,2)
aumB= round(salario*0.15,2)
aumC= round(salario*0.10,2)
aumD= round(salario*0.05,2)

if salario <= 2799.99:
    print(f"Salário antes do reajuste: {salario}")
    print(f"O percentual de aumento aplicado: 20%")
    print(f"O valor do aumento: {aumA}")
    print(f"Salário após aumento: {aumA+salario}")
elif salario >= 2800 and salario <=6999.99:
    print(f"Salário antes do reajuste: {salario}")
    print(f"O percentual de aumento aplicado: 15%")
    print(f"O valor do aumento: {aumB}")
    print(f"Salário após aumento: {aumB+salario}")
elif salario >= 7000 and salario <=14999.99:
    print(f"Salário antes do reajuste: {salario}")
    print(f"O percentual de aumento aplicado: 10%")
    print(f"O valor do aumento: {aumC}")
    print(f"Salário após aumento: {aumC+salario}")
else:
    print(f"Salário antes do reajuste: {salario}")
    print(f"O percentual de aumento aplicado: 5%")
    print(f"O valor do aumento: {aumD}")
    print(f"Salário após aumento: {aumD+salario}")



























