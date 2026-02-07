import random

def gerar_numeros_megasena():
    numeros = random.sample(range(1, 61), 6)
    numeros.sort()
    return numeros

if __name__ == "__main__":
    numeros_sorteio = gerar_numeros_megasena()
    print("Números da MegaSena:", numeros_sorteio)