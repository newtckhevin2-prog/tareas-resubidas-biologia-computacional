# Tarea N°3 - Parte 2 - Calculadora y Conversión de Unidades
# Khevin Flores Olivares

# ------------------------------
# CALCULADORA usando sys.argv
# ------------------------------

import sys

def calculadora_argv():
    """
    Calculadora simple usando sys.argv
    Ejemplo de ejecución: python calculadora.py 3 2 -
    """
    # Simular argumentos para prueba
    sys.argv = ['calculadora.py', '3', '2', '-']

    if len(sys.argv) != 4:
        print("Uso: python calculadora.py <num1> <num2> <operador(+,-,*,%)>")
        return

    try:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        op = sys.argv[3]
    except ValueError:
        print("❌ Debes ingresar números válidos")
        return

    if op == '+':
        resultado = x + y
    elif op == '-':
        resultado = x - y
    elif op == '*':
        resultado = x * y
    elif op == '%':
        resultado = x % y
    else:
        print("❌ Operador inválido. Debe ser +, -, * o %")
        return

    print(f"El resultado es {x} {op} {y} = {resultado}")

# ------------------------------
# CALCULADORA usando argparse
# ------------------------------

import argparse

def calculadora_argparse():
    """
    Calculadora simple usando argparse
    Ejemplo de ejecución: python calculadoraArgparse.py --op * -x 3 -y 1.5
    """
    # Simular argumentos para prueba
    sys.argv = ['calculadoraArgparse.py', '--op', '*', '-x', '3', '-y', '1.5']

    parser = argparse.ArgumentParser(description="Calculadora simple")
    parser.add_argument('-x', type=float, required=True, help="Primer número")
    parser.add_argument('-y', type=float, required=True, help="Segundo número")
    parser.add_argument('--op', type=str, required=True, choices=['+', '-', '*', '%'], help="Operación")

    args = parser.parse_args()
    x = args.x
    y = args.y
    op = args.op

    if op == '+':
        resultado = x + y
    elif op == '-':
        resultado = x - y
    elif op == '*':
        resultado = x * y
    elif op == '%':
        resultado = x % y

    print(f"El resultado es {x} {op} {y} = {resultado}")

# ------------------------------
# CONVERSIÓN DE UNIDADES usando argparse
# ------------------------------

def convertir_unidades():
    """
    Conversión entre Pa y mmHg usando argparse
    Ejemplo de ejecución: python convertirUnidades.py --in 10 -u Pa --out mmHg
    """
    # Simular argumentos para prueba
    sys.argv = ['convertirUnidades.py', '--in', '10', '-u', 'Pa', '--out', 'mmHg']

    parser = argparse.ArgumentParser(description="Conversión de unidades")
    parser.add_argument('--in', dest='valor', type=float, required=True, help="Valor a convertir")
    parser.add_argument('-u', dest='unidad_in', type=str, required=True, help="Unidad de entrada")
    parser.add_argument('--out', dest='unidad_out', type=str, required=True, help="Unidad de salida")

    args = parser.parse_args()

    # Diccionario de factores de conversión
    factores = {('Pa','mmHg'): 1/133.322, ('mmHg','Pa'): 133.322}

    try:
        resultado = args.valor * factores[(args.unidad_in, args.unidad_out)]
        print(f"{args.valor} {args.unidad_in} = {resultado:.2f} {args.unidad_out}")
    except KeyError:
        print("❌ Conversión no implementada")

# ------------------------------
# EJECUCIÓN DE PRUEBA
# ------------------------------
if __name__ == "__main__":
    print("\n--- Calculadora usando sys.argv ---")
    calculadora_argv()

    print("\n--- Calculadora usando argparse ---")
    calculadora_argparse()

    print("\n--- Conversión de unidades ---")
    convertir_unidades()
