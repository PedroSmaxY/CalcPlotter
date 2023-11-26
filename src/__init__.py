# Este é o arquivo __init__.py do pacote 'src'
import sys
import subprocess
from time import sleep
from .limpar_console import limpar_console


def instalar_dependencias(bibliotecas):
    print("Instalando dependências...")

    for biblioteca in bibliotecas:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])
            print(f"{biblioteca} instalada com sucesso!")
        except subprocess.CalledProcessError as erro:
            if "No module named pip" in str(erro):
                print("O pip não está instalado no seu sistema.")
            else:
                print(f"Erro ao instalar {biblioteca}!")
            sys.exit(1)
        sleep(1)
        limpar_console()

    print("Dependências instaladas com sucesso!")
    sleep(1)
    limpar_console()


    print("Verificando dependências...")
    try:
        import tkinter
    except ImportError:
        print("Não foi possível encontrar a dependência tkinter!")
        sys.exit(1)
try:
    import matplotlib
    import numpy
    import sympy
    print("Dependências verificadas com sucesso!")
    sleep(1)
    limpar_console()
except ImportError:
    print("Não foi possível encontrar as dependências.")
    bibliotecas = ["matplotlib", "numpy", "sympy"]
    instalar_dependencias(bibliotecas)

