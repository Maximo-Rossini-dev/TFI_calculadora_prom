# Calculadora de Promedios UTN

## Link al Video

https://www.youtube.com/watch?v=1RO7SFPq7Xw

## Descripción

Este programa desarrollado en Python permite calcular el promedio de distintas materias a partir de las notas ingresadas por el usuario.

La aplicación solicita las calificaciones obtenidas en los exámenes de cada materia definida previamente y calcula el promedio correspondiente.

En esta versión se incorporó una mejora en la validación de datos mediante el uso de `try/except`, permitiendo controlar que el usuario ingrese valores numéricos válidos y que las notas se encuentren dentro del rango permitido.

Se trata de un ejercicio introductorio orientado al aprendizaje de:

* Variables
* Listas
* Diccionarios
* Funciones
* Bucles `for`
* Bucles `while`
* Entrada de datos mediante `input()`
* Manejo de errores con `try/except`
* Validación de datos ingresados por el usuario
* Operaciones aritméticas
* Formateo de cadenas con `f-strings`

---

# Objetivo

Permitir al usuario ingresar las notas de los exámenes de varias materias y obtener el promedio de cada una.

Además, se busca que el programa sea más robusto, evitando que finalice inesperadamente si el usuario ingresa un dato incorrecto.

---

# Tecnologías Utilizadas

* Python 3

No requiere librerías externas.

---

# Estructura del Programa

## Mensaje de bienvenida

El programa comienza mostrando un mensaje inicial al usuario:

```python
print("Bienvenidos a la calculadora de promedios UTN!")
```

Este mensaje permite identificar el inicio de la ejecución del programa.

---

## Definición de materias

El programa define una lista de diccionarios denominada `materias`.

```python
materias = [
    {"nombre": "Programacion", "examenes": 3},
    {"nombre": "Matematica", "examenes": 2},
    {"nombre": "AYSO", "examenes": 3},
    {"nombre": "OE", "examenes": 3},
]
```

Cada materia contiene:

| Campo    | Descripción                   |
| -------- | ----------------------------- |
| nombre   | Nombre de la materia          |
| examenes | Cantidad de exámenes a cargar |

De esta manera, el programa puede recorrer automáticamente cada materia y solicitar la cantidad de notas correspondiente.

---

## Función `pedir_nota`

La función `pedir_nota` se encarga de solicitar una nota al usuario y validar que el dato ingresado sea correcto.

```python
def pedir_nota(nombre_materia, numero_examen):
```

Esta función recibe dos parámetros:

| Parámetro      | Descripción                                 |
| -------------- | ------------------------------------------- |
| nombre_materia | Nombre de la materia que se está procesando |
| numero_examen  | Número de examen que se está solicitando    |

---

## Validación de datos

Dentro de la función se utiliza un bucle `while True`, que permite repetir la solicitud hasta que el usuario ingrese una nota válida.

```python
while True:
```

Esto evita que el programa continúe con datos incorrectos.

---

## Manejo de errores con `try/except`

El programa utiliza una estructura `try/except` para controlar errores al momento de ingresar datos.

```python
try:
    nota = float(
        input(f"Ingrese su nota en el examen {numero_examen} de {nombre_materia}: ")
    )
```

La función `input()` recibe el dato ingresado por el usuario como texto.

Luego, la función `float()` intenta convertir ese dato a un número decimal.

Esto permite ingresar notas enteras o con decimales, por ejemplo:

```text
80
75.5
92.25
```

Si el usuario ingresa un texto, una letra o un valor no numérico, se ejecuta el bloque `except`.

```python
except ValueError:
    print("Error: debe ingresar un número válido. Intente nuevamente.")
```

De esta forma, el programa no se detiene, sino que muestra un mensaje de error y vuelve a solicitar la nota.

---

## Control del rango de notas

Además de validar que el dato sea numérico, el programa controla que la nota esté dentro del rango permitido.

```python
if nota < 1 or nota > 100:
    print("Error: la nota debe estar entre 1 y 100. Intente nuevamente.")
else:
    return nota
```

El rango válido definido es de 1 a 100.

Si el usuario ingresa un número menor a 1 o mayor a 100, el programa informa el error y vuelve a pedir la nota.

Ejemplos de valores inválidos:

```text
0
-5
150
```

Ejemplos de valores válidos:

```text
60
75
88.5
100
```

---

## Recorrido de materias

El programa recorre cada materia de la lista utilizando un bucle `for`.

```python
for materia in materias:
```

En cada iteración:

* Se inicializa el total de la materia en cero.
* Se muestra el nombre de la materia.
* Se solicitan las notas correspondientes.
* Se calcula el promedio.
* Se imprime el resultado final.

---

## Variable acumuladora

Dentro del recorrido de cada materia, se utiliza la variable `total_materia`.

```python
total_materia = 0
```

Esta variable almacena la suma de todas las notas ingresadas para la materia actual.

Se reinicia en cero cada vez que comienza una nueva materia, para que los promedios no se mezclen entre sí.

---

## Recorrido de exámenes

Para cada materia, el programa solicita tantas notas como exámenes tenga definidos.

```python
for i in range(materia["examenes"]):
```

Por ejemplo, si la materia tiene 3 exámenes:

```python
range(3)
```

El programa solicitará tres notas.

---

## Solicitud de notas

La solicitud de notas se realiza llamando a la función `pedir_nota`.

```python
nota = pedir_nota(materia["nombre"], i + 1)
```

Esta función devuelve una nota válida, es decir, un número entre 1 y 100.

Luego, la nota se suma al total de la materia:

```python
total_materia += nota
```

Esto equivale a:

```python
total_materia = total_materia + nota
```

---

## Cálculo del promedio

Una vez ingresadas todas las notas de una materia, el programa calcula el promedio.

```python
promedio = total_materia / materia["examenes"]
```

Se utiliza división normal `/`, lo que permite obtener resultados con decimales.

Ejemplo:

```python
250 / 3
```

Resultado:

```text
83.3333333333
```

---

## Impresión del resultado

El promedio se muestra utilizando un `f-string`.

```python
print(
    f"El promedio total de la materia {materia['nombre']} es de {promedio:.2f}"
)
```

La expresión:

```python
{promedio:.2f}
```

permite mostrar el promedio con dos decimales.

Ejemplo:

```text
83.33
```

---

# Ejemplo de Ejecución

```text
Bienvenidos a la calculadora de promedios UTN!

Materia: Programacion
Ingrese su nota en el examen 1 de Programacion: 80
Ingrese su nota en el examen 2 de Programacion: 75
Ingrese su nota en el examen 3 de Programacion: 90
El promedio total de la materia Programacion es de 81.67

Materia: Matematica
Ingrese su nota en el examen 1 de Matematica: 70
Ingrese su nota en el examen 2 de Matematica: 85
El promedio total de la materia Matematica es de 77.50

Materia: AYSO
Ingrese su nota en el examen 1 de AYSO: 100
Ingrese su nota en el examen 2 de AYSO: 95
Ingrese su nota en el examen 3 de AYSO: 90
El promedio total de la materia AYSO es de 95.00

Materia: OE
Ingrese su nota en el examen 1 de OE: 60
Ingrese su nota en el examen 2 de OE: 75
Ingrese su nota en el examen 3 de OE: 80
El promedio total de la materia OE es de 71.67
```

---

# Ejemplo de Validación de Errores

Si el usuario ingresa un dato no numérico:

```text
Ingrese su nota en el examen 1 de Programacion: hola
Error: debe ingresar un número válido. Intente nuevamente.
Ingrese su nota en el examen 1 de Programacion:
```

Si el usuario ingresa una nota fuera del rango permitido:

```text
Ingrese su nota en el examen 1 de Programacion: 150
Error: la nota debe estar entre 1 y 100. Intente nuevamente.
Ingrese su nota en el examen 1 de Programacion:
```

Esto permite que el programa continúe funcionando sin cerrarse por errores de carga.

---

# Mejoras Incorporadas

En comparación con una versión básica de la calculadora, esta versión incorpora:

* Uso de una función para solicitar y validar notas.
* Manejo de errores mediante `try/except`.
* Validación del rango permitido entre 1 y 100.
* Repetición automática de la solicitud si el dato ingresado no es válido.
* Uso de números decimales mediante `float`.
* Cálculo del promedio con decimales.
* Presentación del resultado con dos cifras decimales.

Estas mejoras hacen que el programa sea más claro, ordenado y seguro frente a errores del usuario.

---

# Posibles Mejoras Futuras

A futuro, el programa podría ampliarse incorporando:

* Carga dinámica de materias.
* Carga dinámica de cantidad de exámenes.
* Guardado de resultados en archivos CSV.
* Guardado de resultados en archivos JSON.
* Registro histórico de promedios.
* Interfaz gráfica.
* Exportación de resultados.

---

# Complejidad

## Temporal

La complejidad temporal es:

```text
O(n)
```

donde:

* `n` representa la cantidad total de exámenes ingresados.

El programa debe recorrer cada examen una vez para solicitar la nota y calcular el promedio.

## Espacial

La complejidad espacial es:

```text
O(1)
```

ya que utiliza una cantidad constante de memoria adicional para almacenar variables como la nota, el total y el promedio.

---

# Conclusión

La Calculadora de Promedios UTN es un programa simple orientado al aprendizaje de estructuras básicas de Python.

Permite practicar el uso de listas, diccionarios, funciones, ciclos, entrada de datos por consola, validación de información y manejo de errores.

La incorporación de `try/except` mejora el funcionamiento del programa, ya que evita interrupciones ante datos incorrectos y permite que el usuario vuelva a ingresar la nota hasta que sea válida.

