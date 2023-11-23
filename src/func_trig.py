from sympy import symbols, diff, integrate, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


def funcao_trigonometrica():
    x = symbols('x')

    while (True):
        funcao_trig = input(
            "Digite a função trigonométrica em termos de 'x' (por exemplo, sin(x)): y=")
        try:
            expr = sympify(funcao_trig)
            break
        except:
            print(
                "Erro: Função trigonométrica inválida. Certifique-se de usar a sintaxe correta.")
            continue

    x_vals = np.linspace(-100, 100, 10000)
    y_vals_trig = [expr.subs(x, val) for val in x_vals]

    derivada = diff(expr, x)
    integral = integrate(expr, x)

    derivada_func = lambdify(x, derivada, 'numpy')

    print(f"\nDerivada da função: {derivada}\n")
    print(f"Integral da função: {integral}\n")

    derivada_vals = derivada_func(x_vals)

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


if __name__ == "__main__":
    funcao_trigonometrica()
