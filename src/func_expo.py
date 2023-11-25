# Importa as bibliotecas necessárias
from sympy import symbols, diff, integrate
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Usa a interface gráfica Tkinter para a criação da figura
matplotlib.use('TkAgg')


def funcao_exponencial():
    # Define a variável simbólica x
    x = symbols('x')

    # Loop para garantir que o usuário insira uma função exponencial válida
    while (True):
        try:
            # Tenta converter a entrada do usuário em uma expressão simbólica
            funcao = input("Digite uma função em termos de 'x' (por exemplo, x**2): y=")
        except:
            # Se ocorrer um erro, exibe uma mensagem e continua o loop
            print("Erro: Função exponencial inválida. Certifique-se de usar a sintaxe correta.")

    # Calcula a derivada e a integral
    derivada = diff(funcao, x)
    integral = integrate(funcao, x)

    # Mostra na tela os valores da derivada e integral
    print(f"\nDerivada da função: {derivada}\n")
    print(f"Integral da função: {integral}\n")

    # Gera valores de x para o gráfico
    x_vals = np.linspace(-100, 100, 10000)

    # Define os valores de y para cada valor de x
    y_vals = [eval(funcao) for x in x_vals]

    # Define o tamanho da figura
    plt.figure(figsize=(10, 5))

    # Define a função do gráfico
    plt.plot(x_vals, y_vals, label="Função")
    # Define a função da derivada i(x)
    plt.plot(x_vals, [eval(str(derivada))for x in x_vals], label="Derivada")

    # Define a largura e espessura do eixo x
    plt.axhline(0, color='black', linewidth=1.5)
    # Define a largura e espessura do eixo y
    plt.axvline(0, color='black', linewidth=1.5)

    # Define um titulo para a figura
    plt.title("Gráfico da Função e sua Derivada")
    plt.xlabel("x")  # Define um nome ao eixo x
    plt.ylabel("y")  # Define um nome ao eixo y

    plt.xlim(-10, 10)  # Define uma escala de visão no eixo x
    plt.ylim(-5, 15)  # Define uma escala de visão no eixo y

    plt.legend()  # Adiciona um índice para cada função
    plt.grid(True)  # Mostra a grade na figura
    plt.show()  # Cria a figura


# Executa a função principal se o script for executado como um programa independente
if __name__ == "__main__":
    funcao_exponencial()
