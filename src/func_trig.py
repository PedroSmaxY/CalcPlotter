# Importa as bibliotecas necessárias
from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Utiliza a interface gráfica Tkinter para a criação da figura
matplotlib.use('TkAgg') 

def funcao_trigonometrica():
    limpar_console()
    
    # Define a variável simbólica x
    x = symbols('x')

    # Loop para garantir que o usuário insira uma função trigonométrica válida
    while True:
        print("Digite a função trigonométrica em termos de 'x' (por exemplo, sin(x))")
        try:
            # Tenta converter a entrada do usuário em uma expressão simbólica
            expr = sympify(input("\ny="))
            break
        except:
            # Se ocorrer um erro, exibe uma mensagem e continua o loop
            limpar_console()
            print("Erro: Função trigonométrica inválida. Certifique-se de usar a sintaxe correta.")
            continue

    # Calcula a derivada e a integral da função
    derivada = diff(expr, x)
    integral = integrate(expr, x)

    # Exibe as informações da derivada e integral
    print(f"\nDerivada da função: {derivada}\n")
    print(f"Integral da função: {integral}\n")

    # Converte a expressão da derivada em uma função numérica
    derivada_func = lambdify(x, derivada, "numpy")

    # Gera valores de x para o gráfico
    x_vals = np.linspace(-100, 100, 10000)

    # Avalia a expressão para obter os valores de y correspondentes
    y_vals_trig = [expr.subs(x, val) for val in x_vals]

    # Avalia a função derivada nos valores de x para o gráfico
    derivada_vals = derivada_func(x_vals)

    # Define o tamanho da figura
    plt.figure(figsize=(10, 5))

    # Define a funcão do gráfico
    plt.plot(x_vals, y_vals_trig, label="Função Trigonométrica")
    # Define a função da derivada d(x)
    plt.plot(x_vals, derivada_vals, label="Derivada")

    # Define a Largura e espessura dos eixos x e y
    plt.axvline(0, color='black', linewidth=1.5)
    plt.axhline(0, color='black', linewidth=1.5)

    # Define o nome da figura
    plt.title("Gráfico da Função Trigonométrica")
    # Define os nomes dos eixos x e y
    plt.xlabel("x")
    plt.ylabel("y")

    # Define a escala de visão do gráfico
    plt.xlim(-10, 10)
    plt.ylim(-5, 10)

    # Adiciona os indices de cada função
    plt.legend()
    # Mostra a grade na figura
    plt.grid(True)
    
    # Cria a figura
    plt.show()

# Executa a função principal se o script for executado como um programa independente
if __name__ == "__main__":
    from limpar_console import limpar_console
    funcao_trigonometrica()
else:
    from .limpar_console import limpar_console
