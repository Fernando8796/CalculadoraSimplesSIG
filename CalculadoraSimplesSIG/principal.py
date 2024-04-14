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


mensagem = '''
Escolha o Operador Aritimético
[1] Somar +
[2] Subtrair -
[3] Multiplicar *
[4] Dividir /
[5] Potenciação **
[6] Porcentagem %"
'''

while True:
    escolha = input(mensagem)

    if escolha == "1":
        num1 = int(input("Qual o primeiro número para somar? "))

        num2 = int(input("Qual o segundo número? "))

        result = num1 + num2
        print(f"O resultado é {result}")

    elif escolha == "2":
        num1 = int(input("Qual o primeiro número para subtrair? "))

        num2 = int(input("Qual o segundo número? "))

        result = num1 - num2
        print(f"O resultado é {result}")

    elif escolha == "3":
        num1 = int(input("Qual o primeiro número para multiplicar? "))

        num2 = int(input("Qual o segundo número? "))

        result = num1 * num2
        print(f"O resultado é {result}")

    elif escolha == "4":
        num1 = int(input("Qual o primeiro número para dividir? "))

        num2 = int(input("Qual o segundo número? "))

        result = num1 / num2
        print(f"O resultado é {result}")

    elif escolha == "5":
        num1 = int(input("Qual é a base? "))

        num2 = int(input("Qual é o expoente? "))

        result = num1 ** num2
        print(f"O resultado é {result}")

    elif escolha == "6":
        num1 = int(input("Quantos porcentos? "))

        num2 = int(input("De quanto? "))

        result = num1/100 * num2
        print(f"O resultado é {result}")

    else:
        print("Escolha inválida")

    #Chamando input para aguardar próxima operacão
    input()