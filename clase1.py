carreras = ("Ingeniería de Software", "Contabilidad", "Derecho")

personas = [
    ("Juan", "Pérez", 38, 0),
    ("Carlos", "Santana", 29, 1),
    ("Raúl", "Sosa", 19, 2)
]

estudiantes = []

for _ in range(5):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))

    print("Carreras disponibles:")
    print("0 - Ingenieria de Software")
    print("1 - Contabilidad")
    print("2 - Derecho")

    carrera = int(input("Ingrese el número de la carrera: "))

    estudiantes.append((nombre, apellido, edad, carrera))

print("\nLista de estudiantes:")
for e in estudiantes:
    print(e)

for _ in range(5):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))

    print("Carreras disponibles:")
    print("0 - Ingenieria de Software")
    print("1 - Contabilidad")
    print("2 - Derecho")

    carrera = int(input("Ingrese el número de la carrera: "))

    persona = (nombre, apellido, edad, carrera)
    personas.append(persona)

    for p in personas:
        nombre = p[0]
        apellido = p[1]
        edad = p[2]
        indice_carrera = p[3]

    nombre_carrera = carreras[indice_carrera]

    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": nombre_carrera
    }

    estudiantes.append(estudiante)

print("\nRESULTADO FINAL")
print("----------------")

for e in estudiantes:
    print(
        e["nombre"],
        e["apellido"],
        "tiene",
        e["edad"],
        "años y estudia",
        e["carrera"]
    )