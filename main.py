# Simulador de puertas lógicas

# Mensaje inicial
print("\nBienvenido al simulador de puertas lógicas")
print("Podrá simular las diferentes puertas lógicas, dando valores de entrada y eligiendo la puerta lógica que desea simular.")

while True:
    # Solicitar al usuario el operador lógico
    operador = input("Seleccione un operador lógico (AND, OR, NOT, NAND, NOR, XOR) o 'salir' para terminar: ").upper()
    while operador not in ["AND", "OR", "NOT", "NAND", "NOR", "XOR", "SALIR"]:
        print("Operador no válido. Vuelva a intentarlo.")
        operador = input("Seleccione un operador lógico (AND, OR, NOT, NAND, NOR, XOR) o 'salir' para terminar: ").upper() # No me agrada repetir otra vez esta línea del input pero de momento no se me ocurre otra forma

    # Salir del simulador
    if operador == "SALIR":
        print("Saliendo del simulador...")
        break

    # Solicitar valores de entrada según el operador
    print("Ingrese los valores de las variables A, B y C (0 o 1)") # Acá tendríamos que validar que si o si agreguen 1 o 0, y no otro valor
    A = int(input("A: "))
    B = int(input("B: "))
    C = int(input("C: "))

    # Resultados de las puertas lógicas
    AND = A and B and C
    OR = A or B or C
    NOT = not A
    NAND = not (A and B and C) # Si quieren que sea un poco más complejo, le agregamos los otros operadores je
    NOR = not (A or B or C)
    XOR = (A and not B and not C) or (not A and B and not C) or (not A and not B and C) or (A and B and C)

    # Salidas
    match operador:
        case "AND":
            print(f"El resultado de A({A}) AND B({B}) AND C({C}) es: {bool(AND)}")
        case "OR":
            print(f"El resultado de A({A}) OR B({B}) OR C({C}) es: {bool(OR)}")
        case "NOT":
            print(f"El resultado de NOT A({A}) es: {bool(NOT)}")
        case "NAND":
            print(f"El resultado de A({A}) NAND B({B}) NAND C({C}) es: {bool(NAND)}")
        case "NOR":
            print(f"El resultado de A({A}) NOR B({B}) NOR C({C}) es: {bool(NOR)}")
        case "XOR":
            print(f"El resultado de A({A}) XOR B({B}) XOR C({C}) es: {bool(XOR)}")

# Mensaje final
print("Gracias por usar el simulador de puertas lógicas.")
