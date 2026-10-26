def calcular_promedio(lista_notas):
    return sum(lista_notas) / len(lista_notas)

def clasificar_estudiante(promedio):
    if promedio >= 4.0:
        return "Alto"
    elif promedio >= 3.0:
        return "Medio"
    return "Bajo"

def obtener_promedio(pareja):
    return pareja[1]

def generar_cuadro_honor(diccionario_estudiantes):
    cuadro = []
    for nombre, notas in diccionario_estudiantes.items():
        cuadro.append((nombre, calcular_promedio(notas)))
    cuadro.sort(key=obtener_promedio, reverse=True)
    return cuadro

estudiantes = {}
opcion = ""

while opcion != "3":
    print("\n--------Menu--------")
    print("1. Ingresar estudiante")
    print("2. Mostrar cuadro de honor")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
        elif nombre in estudiantes:
            print("Error: ese estudiante ya existe.")
        else:
            notas = []
            while len(notas) < 2:
                try:
                    nota = float(input("Ingrese la nota " + str(len(notas) + 1) + ": "))
                    if nota < 0:
                        print("Error: la nota no puede ser negativa.")
                    elif nota > 5:
                        print("Error: la nota no puede ser mayor a 5.")
                    else:
                        notas.append(nota)
                except ValueError:
                    print("Error: debe ingresar un número, no letras.")
            estudiantes[nombre] = notas
            print("Estudiante agregado.")

    elif opcion == "2":
        print("\nCUADRO DE HONOR")
        puesto = 1
        for nombre, promedio in generar_cuadro_honor(estudiantes):
            print(puesto, ".", nombre, "/", round(promedio, 2), "/", clasificar_estudiante(promedio))
            puesto = puesto + 1

    elif opcion == "3":
        print("Programa finalizado.")

    else:
        print("Error: opción no válida.")