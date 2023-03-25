print("MENU DE OPÇÕES:\n\n1- Somar dois números\n2- Multiplicar dois números\n3- Subtrair dois números\n4- Dividir dois números")

codigo = int (input("Digite o número da opção desejada: "))

if codigo == 1:
    num1 = float (input("Você escolheu a opção: Somar dois números\n\nDigite o primeiro número a ser somado: "))
    num2 = float (input("Digite o segundo número a ser somado: "))

    codigo = num1 + num2

    print("Resultado da soma: ", codigo)

elif codigo == 2:
    num1 = float (input("Você escolheu a opção: Multiplicar dois números\n\nDigite o primeiro número a ser multiplicado: "))
    num2 = float (input("Digite o segundo número a ser multiplicado: "))

    codigo = num1 * num2

    print("Resultado da multiplicação: ", codigo)

elif codigo == 3:
    num1 = float (input("Você escolheu a opção: Subtrair dois números\n\nDigite o primeiro número a ser subtraido: "))
    num2 = float (input("Digite o segundo número a ser subtraido: "))

    codigo = num1 - num2

    print("Resultado da subtração: ", codigo)

elif codigo == 4:
    num1 = float (input("Você escolheu a opção: Dividir dois números\n\nDigite o primeiro número a ser dividido: "))
    num2 = float (input("Digite o segundo número a ser dividido: "))

    codigo = num1 / num2

    print(f"Resultado da divisão: {round(codigo, 2)}")

else:
    print("Valor inválido")