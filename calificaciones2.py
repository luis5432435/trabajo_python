# Diccionario vacío para almacenar estudiantes y calificaciones
estudiantes = {}

while True:
    # Solicitar nombre del estudiante
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    
    # Opción para salir del bucle
    if nombre.lower() == "salir":
        break
    
    # Solicitar calificación del estudiante y convertirla a tipo float
    try:
        calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    except ValueError:
        print("Por favor, ingrese una calificación válida.")
        continue
    
    # Actualizar calificación si el estudiante ya existe, o agregarlo si no existe
    if nombre in estudiantes:
        print(f"Actualizando la calificación de {nombre} a {calificacion}.")
    else:
        print(f"Agregando el estudiante {nombre} con calificación {calificacion}.")
    
    estudiantes[nombre] = calificacion

# Mostrar todos los estudiantes y sus calificaciones
print("\nLista de estudiantes y sus calificaciones:")
for estudiante, calificacion in estudiantes.items():
    print(f"{estudiante}: {calificacion}")
