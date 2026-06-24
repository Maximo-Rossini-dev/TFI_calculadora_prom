print("Bienvenidos a la calculadora de promedios UTN!")

materias = [
    {"nombre": "Programacion", "examenes": 3},
    {"nombre": "Matematica", "examenes": 2},
    {"nombre": "AYSO", "examenes": 3},
    {"nombre": "OE", "examenes": 3},
]


def pedir_nota(nombre_materia, numero_examen):

    # Solicita una nota al usuario y valida que sea un número entre 1 y 100.
    # Si el dato ingresado no es válido, vuelve a pedirlo.

    while True:
        try:
            nota = float(
                input(f"Ingrese su nota en el examen {numero_examen} de {nombre_materia}: ")
            )

            if nota < 1 or nota > 100:
                print("Error: la nota debe estar entre 1 y 100. Intente nuevamente.")
            else:
                return nota

        except ValueError:
            print("Error: debe ingresar un número válido. Intente nuevamente.")


for materia in materias:
    total_materia = 0

    print(f"\nMateria: {materia['nombre']}")

    for i in range(materia["examenes"]):
        nota = pedir_nota(materia["nombre"], i + 1)
        total_materia += nota

    promedio = total_materia / materia["examenes"]

    print(
        f"El promedio total de la materia {materia['nombre']} es de {promedio:.2f}"
    )
