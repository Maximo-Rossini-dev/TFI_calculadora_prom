# Calculadora de Promedios UTN

## Link al Video

https://www.youtube.com/watch?v=1RO7SFPq7Xw

## Descripción

Este programa desarrollado en Python permite calcular el promedio de distintas materias a partir de las notas ingresadas por el usuario.

La aplicación solicita las calificaciones obtenidas en los exámenes de cada materia definida previamente y calcula el promedio correspondiente.

Se trata de un ejercicio introductorio orientado al aprendizaje de:

- Variables
- Listas
- Diccionarios
- Bucles `for`
- Entrada de datos mediante `input()`
- Operaciones aritméticas
- Formateo de cadenas con `f-strings`

---

# Objetivo

Permitir al usuario ingresar las notas de los exámenes de varias materias y obtener el promedio de cada una.

---

# Tecnologías Utilizadas

- Python 3

No requiere librerías externas.

---

# Estructura del Programa

## Definición de materias

El programa comienza definiendo una lista de diccionarios denominada `materias`.

```python
materias = [
    {"nombre": "Programacion", "examenes": 3},
    {"nombre": "Matematica", "examenes": 2},
]
```

Cada materia contiene:

| Campo    | Descripción                   |
| -------- | ----------------------------- |
| nombre   | Nombre de la materia          |
| examenes | Cantidad de exámenes a rendir |

---

## Variable acumuladora

```python
totalMateria = 0
```

Esta variable almacena la suma de todas las notas ingresadas.

---

## Recorrido de materias

```python
for m in materias:
```

El programa recorre cada materia de la lista.

En cada iteración:

- Obtiene el nombre de la materia.
- Obtiene la cantidad de exámenes.
- Solicita las notas correspondientes.

---

## Recorrido de exámenes

```python
for i in range(m["examenes"]):
```

Se ejecuta tantas veces como exámenes tenga la materia.

Ejemplo:

Para Programación:

```python
range(3)
```

Genera:

```text
0
1
2
```

Y permite solicitar las tres notas.

---

## Solicitud de notas

```python
print(f"Ingrese su nota en el {i + 1} examen de {m['nombre']}")
nota = int(input())
```

El usuario ingresa una nota numérica.

La función:

```python
int()
```

convierte el dato ingresado desde texto a número entero.

---

## Acumulación de notas

```python
totalMateria += nota
```

Equivale a:

```python
totalMateria = totalMateria + nota
```

Permite ir sumando todas las notas ingresadas.

---

## Cálculo del promedio

```python
totalMateria // m["examenes"]
```

Se utiliza división entera (`//`).

Ejemplo:

```python
17 // 3
```

Resultado:

```text
5
```

La parte decimal se descarta.

---

## Impresión del resultado

```python
print(
    f"El promedio total de la materia {m['nombre']} es de {totalMateria // m['examenes']}"
)
```

Muestra el promedio calculado para la materia actual.

---

# Ejemplo de Ejecución

```text
Bienvenidos a la calculadora de promedios UTN!

Ingrese su nota en el 1 examen de Programacion
8

Ingrese su nota en el 2 examen de Programacion
7

Ingrese su nota en el 3 examen de Programacion
9

El promedio total de la materia Programacion es de 8

Ingrese su nota en el 1 examen de Matematica
6

Ingrese su nota en el 2 examen de Matematica
7

El promedio total de la materia Matematica es de 15


---

## Persistencia de datos

Guardar las notas en:

- CSV
- JSON
- Base de datos

---

# Complejidad

## Temporal

O(n)

donde:

- n = cantidad total de exámenes ingresados.

## Espacial

O(1)

ya que utiliza una cantidad constante de memoria adicional.

---

# Conclusión

La Calculadora de Promedios UTN es un programa simple orientado al aprendizaje de estructuras básicas de Python. Permite practicar el uso de listas, diccionarios, ciclos y entrada de datos por consola.
```
