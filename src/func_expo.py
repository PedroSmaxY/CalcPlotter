from sympy import symbols, diff, integrate
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

def funcao_exponencial():
    x = symbols('x')
    funcao = input("Digite uma função em termos de 'x' (por exemplo, x**2): y=")

    # Calcula a derivada
    derivada = diff(funcao, x)
    # Calcula a integral
    integral = integrate(funcao, x)


    print(f"\nDerivada da função: {derivada}\n")
    print(f"Integral da função: {integral}\n")

    x_vals = np.linspace(-100, 100, 10000)
    y_vals = [eval(funcao) for x in x_vals]

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label="Função")
    plt.plot(x_vals, [eval(str(derivada))
    for x in x_vals], label="Derivada")
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.title("Gráfico da Função e sua Derivada")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(-10, 10)
    plt.ylim(-5, 15)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    funcao_exponencial()