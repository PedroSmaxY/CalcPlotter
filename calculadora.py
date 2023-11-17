from sympy import symbols, diff
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

def calculadora():
    x = symbols('x')

    print("Bem-vindo à Calculadora com Gráfico!")
    while True:
        print("\nEscolha uma operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Gráfico da Função e Derivada")
        print("0 - Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '0':
            print("Saindo da calculadora. Até logo!")
            break
        elif escolha in ['1', '2', '3', '4']:
            operacao = int(escolha)
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == 1:
                resultado = num1 + num2
                print(f"Resultado: {resultado:.2f}")
            elif operacao == 2:
                resultado = num1 - num2
                print(f"Resultado: {resultado:.2f}")
            elif operacao == 3:
                resultado = num1 * num2
                print(f"resultado: {resultado:.2f}")
            elif operacao == 4:
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {resultado:.2f}")
                else:
                    print("Erro: Divisão por zero!")
        elif escolha == '5':
            funcao = input("Digite uma função em termos de 'x' (por exemplo, x**2): ")

            # Calcula a derivada
            derivada = diff(funcao, x)

            print(f"Derivada da função: {derivada}")

            x_vals = np.linspace(-50, 50, 100)
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
            plt.ylim(-20, 20)
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    calculadora()
