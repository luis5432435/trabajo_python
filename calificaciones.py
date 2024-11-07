# Crear un diccionario vacío para almacenar las calificaciones
calificaciones = {}

# Pedir los nombres de los estudiantes y sus calificaciones
for i in range(3):
    nombre = input("Ingresa el nombre del estudiante: ")
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    calificaciones[nombre] = calificacion

# Encontrar el nombre del estudiante con la calificación más alta
nombre_max = max(calificaciones, key=calificaciones.get)

# Imprimir el resultado
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación de {calificaciones[nombre_max]}.")
