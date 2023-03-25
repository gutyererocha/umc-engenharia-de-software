print("Verifique se você foi aprovado, reprovado ou está em exame")

media = int (input("Digite a média da sua nota: "))

if media >= 5:
    print("Aprovado")
elif media >= 3:
    print("Exame")
else:
    print("Reprovado")