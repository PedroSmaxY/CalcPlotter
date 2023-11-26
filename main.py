from src.func_expo import funcao_exponencial
from src.func_trig import funcao_trigonometrica
from src.limpar_console import limpar_console

def calculadora():
    while True:
        limpar_console()
        print("\nBem-vindo à Calculadora com Gráfico!\n")
        print("\nEscolha uma operação:")
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
            funcao_exponencial()

        elif escolha == '6':
            funcao_trigonometrica()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    calculadora()
