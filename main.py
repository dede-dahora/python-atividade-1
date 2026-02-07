import calculadora

if __name__ == "__main__":
    # Usando as funções da calculadora
    resultado_soma = calculadora.soma(10, 5)
    resultado_subtracao = calculadora.subtracao(10, 5)
    
    print(f"Soma: 10 + 5 = {resultado_soma}")
    print(f"Subtração: 10 - 5 = {resultado_subtracao}")
    
    # Usando outras operações (opcional)
    resultado_multiplicacao = calculadora.multiplicacao(10, 5)
    resultado_divisao = calculadora.divisao(10, 5)
    
    print(f"Multiplicação: 10 × 5 = {resultado_multiplicacao}")
    print(f"Divisão: 10 ÷ 5 = {resultado_divisao}")