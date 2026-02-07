import random

def jogo_jokenpo():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_computador = random.choice(opcoes)
    return escolha_computador

if __name__ == "__main__":
    resultado = jogo_jokenpo()
    print(f"O computador escolheu: {resultado}")