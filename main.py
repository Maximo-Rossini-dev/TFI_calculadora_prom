print("Bienvenidos a la calculadora de promedios UTN!")
materias = [
    {"nombre": "Programacion", "examenes": 3},
    {"nombre": "Matematica", "examenes": 2},
    {"nombre": "AYSO", "examenes": 3},
    {"nombre": "OE", "examenes": 2},
]
totalMateria = 0

for m in materias:
    for i in range(m["examenes"]):
        print(f"Ingrese su nota en el {i + 1} examen de {m["nombre"]} ")
        nota = int(input())
        totalMateria += nota
    print(
        f"El promedio total de la materia {m["nombre"]} es de {totalMateria // m["examenes"]}"
    )
    totalMateria = 0
