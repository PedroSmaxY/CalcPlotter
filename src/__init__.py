# Este é o arquivo __init__.py do pacote 'src'
import sys
import subprocess
from time import sleep
from .limpar_console import limpar_console


def instalar_dependencias(bibliotecas):
    print("Instalando dependências...")
    sleep(1)

    for biblioteca in bibliotecas:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])
            print(f"\n{biblioteca} instalada com sucesso!")
            sleep(1)
        except subprocess.CalledProcessError as erro:
            if "No module named pip" in str(erro):
                print("\nO pip não está instalado no seu sistema.")

            else:
                print(f"\nErro ao instalar {biblioteca}!")

            sleep(2.5)
            sys.exit(1)
        sleep(1)
        limpar_console()

    print("Dependências instaladas com sucesso!")
    sleep(1)
    limpar_console()


limpar_console()
print("Verificando dependências...")
sleep(1)
try:
    import tkinter
except ImportError:
    print("Não foi possível encontrar a dependência tkinter!")
    sleep(2.5)
    sys.exit(1)
try:
    import matplotlib
    import numpy
    import sympy
    print("Dependências verificadas com sucesso!")
    sleep(1)
    limpar_console()
except ImportError:
    bibliotecas = ["matplotlib", "numpy", "sympy"]
    instalar_dependencias(bibliotecas)
