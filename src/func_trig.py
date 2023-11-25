# Importa as bibliotecas necessárias
from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Utiliza a interface gráfica Tkinter para a criação da figura
matplotlib.use('TkAgg') 

def funcao_trigonometrica():
    # Define a variável simbólica x
    x = symbols('x')

    # Loop para garantir que o usuário insira uma função trigonométrica válida
    while True:
        funcao_trig = input("Digite a função trigonométrica em termos de 'x' (por exemplo, sin(x)): y=")
        try:
            # Tenta converter a entrada do usuário em uma expressão simbólica
            expr = sympify(funcao_trig)
            break
        except:
            # Se ocorrer um erro, exibe uma mensagem e continua o loop
            print("Erro: Função trigonométrica inválida. Certifique-se de usar a sintaxe correta.")
            continue

    # Gera valores de x para o gráfico
    x_vals = np.linspace(-100, 100, 10000)

    # Avalia a expressão para obter os valores de y correspondentes
    y_vals_trig = [expr.subs(x, val) for val in x_vals]

    # Calcula a derivada e a integral da função
    derivada = diff(expr, x)
    integral = integrate(expr, x)

    # Converte a expressão da derivada em uma função numérica
    derivada_func = lambdify(x, derivada, 'numpy')

    # Exibe as informações da derivada e integral
    print(f"\nDerivada da função: {derivada}\n")
    print(f"Integral da função: {integral}\n")

    # Avalia a função derivada nos valores de x para o gráfico
    derivada_vals = derivada_func(x_vals)

    # Configurações do gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals_trig, label="Função Trigonométrica")
    plt.plot(x_vals, derivada_vals, label="Derivada")
    plt.title("Gráfico da Função Trigonométrica")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(-10, 10)
    plt.ylim(-5, 10)
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.legend()
    plt.grid(True)
    plt.show()

# Executa a função principal se o script for executado como um programa independente
if __name__ == "__main__":
    funcao_trigonometrica()
