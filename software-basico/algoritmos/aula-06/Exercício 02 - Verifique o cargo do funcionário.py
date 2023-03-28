print("Verifique o cargo do funcionário digitando o código correspondente")

codigo = int (input("Digite o código do cargo: "))

if codigo == 1:
    print("Escrituário")
elif codigo == 2:
    print("Secretária")
elif codigo == 3:
    print("Caixa")
elif codigo == 4:
    print("Gerente")
elif codigo == 5:
    print("Diretor")
else:
    print("Código inválido")
