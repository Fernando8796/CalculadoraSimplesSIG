'''
Calculadora:
    Etapas:
        1° Usuário escolher o Operador matemático (+, -, *, /, **, %);
        2° Pegar o Operador matemático e chamar a função dele;
        3° Usuário escolher o primeiro número;
        4° Transformar o primeiro número do usuário em float;
        5° Usuário escolher o segundo número;
        6° Transformar o segundo número do usuário em float;
        7° Jogar os dois números float na função;
        8° Dar o resultado
'''



def soma(numb1, numb2):
    resultado = numb1 + numb2
    return resultado

def sub(numb1, numb2):
    resultado = numb1 - numb2
    return resultado

def mult(numb1, numb2):
    resultado = numb1 * numb2
    return resultado

def div(numb1, numb2):
    resultado = numb1 / numb2 
    return resultado

def poten(numb1, numb2):
    resultado = numb1 ** numb2
    return resultado

def porc(numb1, numb2):
    numb3 = numb2/100
    resultado = numb1 * numb3
    return resultado

mensagem = '''
Escolha o Operador Aritimético
[1] Somar +
[2] Subtrair -
[3] Multiplicar *
[4] Dividir /
[5] Potenciação **
[6] Porcentagem %"
'''
num1 = ("Qual o primeiro número para ")
num2 = ("Qual o segundo número?\n")

while True:
    escolha = input(mensagem)

    if escolha == "1":

        n1 = input(num1 + "somar?\n")
        numb1 = int(n1)

        n2 = input(num2)
        numb2 = int(n2)

        result = soma(numb1, numb2)
        resultades = f"O resultado é {result}"
        print(resultades)

    elif escolha == "2":
        n1 = input(num1 + "subtrair?\n")
        numb1 = int(n1)

        n2 = input(num2)
        numb2 = int(n2)

        result = sub(numb1, numb2)
        resultades = f"O resultado é {result}"
        print(resultades)

    elif escolha == "3":
        n1 = input(num1 + "multiplicar?\n")
        numb1 = int(n1)

        n2 = input(num2)
        numb2 = int(n2)

        result = mult(numb1, numb2)
        resultades = f"O resultado é {result}"
        print(resultades)

    elif escolha == "4":
        n1 = input(num1 + "dividir?\n")
        numb1 = int(n1)

        n2 = input(num2)
        numb2 = int(n2)

        result = div(numb1, numb2)
        resultades = f"O resultado é {result}"
        print(resultades)

    elif escolha == "5":
        n1 = input("Qual é a base?\n")
        numb1 = int(n1)

        n2 = input("Qual é o expoente?\n")
        numb2 = int(n2)

        result = poten(numb1, numb2)
        resultades = f"O resultado é {result}"
        print(resultades)

    elif escolha == "6":
        n1 = input("Quantos porcentos?\n")
        numb1 = int(n1)

        n2 = input("De quanto?\n")
        numb2 = int(n2)

        result = porc(numb1, numb2)
        resultades = f"O resultado é {result}"
        print(resultades)

    else:
        print("Escolha inválida")

    #Chamando input para aguardar próxima operacão
    input()
