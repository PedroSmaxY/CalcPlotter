# Importa as bibliotecas necessárias
from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Usa a interface gráfica Tkinter para a criação da figura
matplotlib.use('TkAgg')


def funcao_exponencial():
    limpar_console()
    
    # Define a variável simbólica x
    x = symbols('x')

    # Loop para garantir que o usuário insira uma função exponencial válida
    while True:
        print("Digite uma função em termos de 'x' (por exemplo, x**2)")
        try:
            # Tenta converter a entrada do usuário em uma expressão simbólica
            funcao = sympify(input("\ny="))
            break
        except:
            limpar_console()
            # Se ocorrer um erro, exibe uma mensagem e continua o loop
            print("Erro: Função exponencial inválida. Certifique-se de usar a sintaxe correta.")
            continue

    # Calcula a derivada e a integral da função
    derivada = diff(funcao, x)
    integral = integrate(funcao, x)

    # Exibe as informações da derivada e integral
    print(f"\nDerivada da função: {derivada}\n")
    print(f"Integral da função: {integral}\n")
    

    # Converte a função simbólica para uma função que pode ser avaliada numericamente
    f = lambdify(x, funcao, "numpy")

    # Gera valores de x para o gráfico
    x_vals = np.linspace(-100, 100, 10000)

    # Avalia a expressão para obter os valores de y correspondentes
    y_vals = f(x_vals)

    # Define o tamanho da figura
    plt.figure(figsize=(10, 5))

    # Define a função do gráfico
    plt.plot(x_vals, y_vals, label="Função")
    # Define a função da derivada d(x)
    plt.plot(x_vals, [eval(str(derivada))for x in x_vals], label="Derivada")

    # Define a largura e espessura dos eixos x e y
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)

    # Define um titulo para a figura
    plt.title("Gráfico da Função Exponencial")
    # Define os nomes dos eixos x e y
    plt.xlabel("x")  
    plt.ylabel("y")  

    # Define a escala de visão do gráfico
    plt.xlim(-10, 10)  
    plt.ylim(-5, 15)  

    # Adiciona os índices de cada função
    plt.legend()  
    # Mostra a grade na figura
    plt.grid(True)  
    
    # Cria a figura
    plt.show()  


# Executa a função principal se o script for executado como um programa independente
if __name__ == "__main__":
    from limpar_console import limpar_console
    funcao_exponencial()
else:
    from .limpar_console import limpar_console
