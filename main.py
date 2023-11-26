from src.func_expo import funcao_exponencial
from src.func_trig import funcao_trigonometrica
from src.limpar_console import limpar_console


def calculadora():
    while True:
        print("Bem-vindo à Calculadora com Gráfico!")
        print("\nEscolha uma operação:\n")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Gráfico da Função Exponencial e Derivada/Integral")
        print("6 - Gráfico da Função Trigonométrica e Derivada/Integral")
        print("0 - Sair\n")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '0':
            limpar_console()
            print("Saindo da calculadora. Até logo!")
            break
        elif escolha in ['1', '2', '3', '4']:
            limpar_console()
            operacao = int(escolha)
            while True:
                try:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    break
                except ValueError:
                    print("Erro: Entrada inválida!")
                    input("Pressione ENTER para continuar...")
                    limpar_console()
                    continue

            if operacao == 1:
                resultado = num1 + num2
                print(f"\nResultado: {num1:.0f} + {num2:.0f} = {resultado:.0f}")
                input("\nPressione ENTER para continuar...")
                
            elif operacao == 2:
                resultado = num1 - num2
                print(f"\nResultado: {num1:.0f} - {num2:.0f} = {resultado:.0f}")
                input("\nPressione ENTER para continuar...")

            elif operacao == 3:
                resultado = num1 * num2
                print(f"\nResultado: {num1:.0f} x {num2:.0f} = {resultado:.0f}")
                input("\nPressione ENTER para continuar...")

            elif operacao == 4:
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"\nResultado: {num1} / {num2} = {resultado:.2f}")
                    input("\nPressione ENTER para continuar...")
                else:
                    print("\nErro: Divisão por zero!")
                    input("\nPressione ENTER para continuar...")

        elif escolha == '5':
            funcao_exponencial()

        elif escolha == '6':
            funcao_trigonometrica()
        else:
            limpar_console()
            print("Opção inválida. Tente novamente.")
            continue

        limpar_console()


if __name__ == "__main__":
    calculadora()
