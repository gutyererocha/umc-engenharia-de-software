print("Jogo de advinhação de um número entre 1 e 10")

numTentatitas = 1
numPremiado = int(input("Jogador 1, digite o número premiado de 1 a 10: "))

while(numPremiado < 1 or numPremiado > 10):
    numPremiado = int(input("Número inválido! Digite um número entre 1 e 10: "))

numEscolhido = int(input("Jogador 2, tente acertar o número premiado entre 1 e 10: "))

while(numEscolhido != numPremiado):
    numEscolhido = int(input("Você errou! tente de novo: "))

    numTentatitas += 1

print("Você acertou em", numTentatitas, "tentativas")