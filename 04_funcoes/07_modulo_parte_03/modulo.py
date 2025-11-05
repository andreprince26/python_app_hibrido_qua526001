# biblioteca
import os
import math
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# funçao do 1º grau: a*x+b = 0
def primeiro_grau(a, b):
    return -b/a if a != 0 else "nao existe raiz real."

# funçao do 2° grau: a*x² + b*x + c = 0
def segundo_grau(a, b, c):
    if a != 0:
        delta = (b**2)-(4*a*c)
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            yield x1
            yield x2
        elif delta == 0:
            yield -b/(2*a)
        else:
            yield "nao existem raizes reais."
    else:
        yield primeiro_grau(b, c)