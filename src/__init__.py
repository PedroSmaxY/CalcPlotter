# This is the __init__.py file of the 'src' package
import sys
import subprocess
from time import sleep
from .clear_console import clear_console


def install_dependencies(libraries):
    print("Installing dependencies...")
    sleep(1)
    clear_console()

    for library in libraries:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])
            print(f"\n{library} installed successfully!")
            sleep(1)
        except subprocess.CalledProcessError as error:
            if "No module named pip" in str(error):
                print("\npip is not installed on your system.")

            else:
                print(f"\nError installing {library}!")

            sleep(2.5)
            sys.exit(1)
        sleep(1)
        clear_console()

    print("Dependencies installed successfully!")
    sleep(1)
    clear_console()


clear_console()
print("Checking dependencies...")
sleep(1)
try:
    import tkinter
except ImportError:
    print("Could not find the tkinter dependency!")
    sleep(2.5)
    sys.exit(1)
try:
    import matplotlib
    import numpy
    import sympy
    print("Dependencies checked successfully!")
    sleep(1)
    clear_console()
except ImportError:
    libraries = ["matplotlib", "numpy", "sympy"]
    install_dependencies(libraries)
