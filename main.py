from src import func_expo
from src import func_trig


def calculadora():
    print("\nBem-vindo à Calculadora com Gráfico!")
    while True:
        print("\nEscolha uma operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Gráfico da Função e Derivada/Integral")
        print("6 - Gráfico da Função Trigonométrica e Derivada/Integral")
        print("0 - Sair\n")

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
            func_expo.funcao_exponencial()

        elif escolha == '6':
            func_trig.funcao_trigonometrica()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    calculadora()
