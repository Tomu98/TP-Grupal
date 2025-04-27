# Simulador de puertas lógicas

# Función para mostrar la tabla de verdad
def mostrar_tabla(operador):
    print(f"\nTabla de verdad de {operador}:")

    # Tabla de verdad de NOT
    if operador == "NOT":
        print("A | Resultado")
        for a in [0, 1]:
            r = not a
            print(f"{a} | {int(r)}")
        return

    # Tabla de verdad de los otros operadores
    print("A B C | Resultado")
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                if operador == "AND":
                    r = a and b and c
                elif operador == "OR":
                    r = a or b or c
                elif operador == "NAND":
                    r = not (a and b and c)
                elif operador == "NOR":
                    r = not (a or b or c)
                elif operador == "XOR":
                    r = (a + b + c) % 2
                print(f"{a} {b} {c} | {int(r)}")


# Función para obtener un valor binario válido (0 o 1)
def obtener_valor_binario(nombre_variable):
    while True:
        valor = input(f"{nombre_variable}: ")
        if valor == "0" or valor == "1":
            return int(valor)
        else:
            print("Valor no válido. Ingresa solo 1 o 0.")


# Función para obtener respuesta válida de s/n 
def obtener_respuesta_si_no(pregunta):
    while True:
        respuesta = input(pregunta).lower()
        if respuesta in ["s", "si", "n", "no"]:
            return respuesta == "s" or respuesta == "si"
        else:
            print("Respuesta no válida. Por favor, ingrese 's/si' o 'n/no'.")


# Mensaje inicial
print("\nBienvenido al simulador de puertas lógicas.")
print("Este programa te permite:")
print("- Elegir entre diferentes puertas lógicas")
print("- Ingresar valores binarios como entrada")
print("- Ver el resultado lógico de la operación")
print("- Opcionalmente, consultar la tabla de verdad del operador seleccionado")

continuar = True
while continuar:
    print("\nSeleccione un operador lógico")
    operador = input("(AND, OR, NOT, NAND, NOR, XOR): ").upper()
    while operador not in ["AND", "OR", "NOT", "NAND", "NOR", "XOR"]:
        print("Operador no válido. Vuelva a intentarlo.")
        operador = input("\n(AND, OR, NOT, NAND, NOR, XOR): ").upper()

    if operador == "NOT":
        print("\nIngrese el valor de la variable A (0 o 1)")
        A = obtener_valor_binario("A")
        B = C = None
    else:
        print("\nIngrese los valores de las variables A, B y C (0 o 1)")
        A = obtener_valor_binario("A")
        B = obtener_valor_binario("B")
        C = obtener_valor_binario("C")

    # Resultados y salidas
    match operador:
        case "AND":
            resultado = A and B and C
            print(f"\nOperación: AND (Conjunción)")
            print(f"Entradas: A={A} B={B} C={C}")
            print(f"Resultado: {A} * {B} * {C} = {int(resultado)} ({bool(resultado)})")
        case "OR":
            resultado = A or B or C
            print(f"\nOperación: OR (Disyunción)")
            print(f"Entradas: A={A} B={B} C={C}")
            print(f"Resultado: {A} + {B} + {C} = {int(resultado)} ({bool(resultado)})")
        case "NOT":
            resultado = not A
            print(f"\nOperación: NOT (Negación)")
            print(f"Entrada: A={A}")
            print(f"Resultado: ¬{A} = {int(resultado)} ({bool(resultado)})")
        case "NAND":
            resultado = not (A and B and C)
            print(f"\nOperación: NAND (Negación de la conjunción)")
            print(f"Entradas: A={A} B={B} C={C}")
            print(f"Resultado: ¬({A} * {B} * {C}) = {int(resultado)} ({bool(resultado)})")
        case "NOR":
            resultado = not (A or B or C)
            print(f"\nOperación: NOR (Negación de la disyunción)")
            print(f"Entradas: A={A} B={B} C={C}")
            print(f"Resultado: ¬({A} + {B} + {C}) = {int(resultado)} ({bool(resultado)})")
        case "XOR":
            resultado = (A + B + C) % 2
            print(f"\nOperación: XOR (Disyunción exclusiva)")
            print(f"Entradas: A={A} B={B} C={C}")
            print(f"Resultado: ({A} + {B} + {C}) % 2 = {int(resultado)} ({bool(resultado)})")

    # Mostrar tabla de verdad si se desea
    if obtener_respuesta_si_no("\n¿Desea ver la tabla de verdad para esta puerta lógica? (s/n): "):
        mostrar_tabla(operador)

    continuar = obtener_respuesta_si_no("\n¿Quieres volver a intentar? (s/n): ")

print("\nSaliendo del simulador...")
print("¡Gracias por usar el simulador de puertas lógicas!\n")
