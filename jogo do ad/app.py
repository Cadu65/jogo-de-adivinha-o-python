import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de Adivinhação!")
    print("Eu estou pensando em um número entre 1 e 100.")

    while True:
        tentativa = int(input("Faça sua tentativa: "))
        tentativa += 1

        if tentativa < numero_secreto:
            print("É maior! Tente novamente.")
        elif tentativa > numero_secreto:
            print("É menor! Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_adivinhacao()
