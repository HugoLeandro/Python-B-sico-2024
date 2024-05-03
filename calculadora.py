

def subtracao(nu1,nu2):
    return nu1 - nu2

def multiplicacao(nu1,nu2):
    return nu1 * nu2

def divisao(nu1,nu2):
    if nu2 == 0:
        print("Operação Inválida. Divisão por Zero")
    else:
        return nu1 / nu2

def soma(nu1, nu2):
    return nu1 + nu2

def calculadora():
    try:
        nu1 = int(input("Qual o primeiro número?" ))
    except ValueError:
        print("Operação Inválida!. Digite um número.")
    try:
        nu2 = int(input("Qual o segundo número? "))
    except ValueError:
        print("Operação Inválida!. Digite um número.")


    operacao = input("Qual a operação? [ : x - + ] ")
    if operacao == "+":
        resultado = soma(nu1,nu2)
    elif operacao == ":":
        resultado = divisao(nu1,nu2)
    elif operacao == "-":
        resultado = subtracao(nu1,nu2)
    elif operacao == "x":
        resultado = multiplicacao(nu1,nu2)
    else:
         print("Operação Inválida") 
    return print(resultado)

calculadora()

