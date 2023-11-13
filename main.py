import numpy as np
import matplotlib.pyplot as plt


def calcular_movimento_foguete(altura_inicial: float, aceleracao_gravidade: float, tempo_total: float, resistencia_ar: float):
    # Calcula o tempo de voo usando a fórmula t = (2h/g) + (v0/g)
    tempo_voo = (2 * altura_inicial / aceleracao_gravidade) + (velocidade_inicial / aceleracao_gravidade)

    # Se o tempo total fornecido for maior que o tempo de voo, use o tempo de voo
    tempo_total = min(tempo_total, tempo_voo)

    # Cria um array de tempos para o gráfico
    tempos = np.linspace(0, tempo_total, 100)

    # Calcula a altitude e a velocidade para cada ponto no tempo
    altitudes = (aceleracao_gravidade * tempos ** 2) / 2
    velocidades = aceleracao_gravidade * tempos - resistencia_ar * tempos ** 2

    # Exibe o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(tempos, altitudes, label='Altitude', color='blue')
    plt.plot(tempos, velocidades, label='Velocidade', color='red')

    plt.title('Movimento do Foguete')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Altitude (m) / Velocidade (m/s)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return altitudes[-1], tempo_voo


def formatar_tempo(tempo: float) -> str:
    horas = tempo // 60
    minutos = tempo % 60

    return f"{horas:.0f} horas e {minutos:.0f} minutos" 


if __name__ == "__main__":
    altura_inicial = float(input("Insira a altura final do foguete em metros (Ou aperte enter para considerar 1000 metros): ") or 1000)
    aceleracao_gravidade = float(input("Insira a aceleração devido à gravidade em m/s² (Ou aperte enter para considerar 9,8m/s²): ") or 9.8)
    tempo_total = float(input("Insira o tempo total a ser exibido no gráfico em segundos (Ou aperte enter para considerar 60s): ") or 60)
    resistencia_ar = float(input("Insira o valor da resistência do ar em N/m² (Ou aperte enter para considerar 0 de resistência): ") or 0)
    velocidade_inicial = float(input("Insira a velocidade inicial do foguete em m/s (Ou aperte enter para considerar Vo = 0): ") or 0)

    altura_final, tempo_voo = calcular_movimento_foguete(altura_inicial, aceleracao_gravidade, tempo_total, resistencia_ar)

    print(f"Tempo para atingir a altura final: {formatar_tempo(tempo_voo)}")
    print(f"Altura final: {altura_final:.2f} metros")
