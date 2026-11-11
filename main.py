from gestion import lista_paciente, registrar_paciente, registrar_medico, enmascarar

print("=== SISTEMA KAWSAY (prototipo con datos ficticios) ===")
print("Use un nombre inventado para el paciente. No escriba DNI, teléfono ni datos médicos reales.")

base = [["M001", "Luis Ramos", "Medicina general"], ["M002", "Rosa Vega", "Pediatría"],
        ["M003", "Carlos Mena", "Cardiología"], ["M004", "Elena Rojas", "Dermatología"]]
for m in base:
    registrar_medico(m[0], m[1], m[2])

seguir = "s"
while seguir == "s":
    print()
    nombre = input("Nombre del paciente (ficticio): ")
    edad = ""
    while edad == "":
        try:
            edad = int(input("Edad del paciente: "))
        except ValueError:
            print("Error: escriba solo números enteros.")
    codigo_paciente = f"P{len(lista_paciente) + 1:03d}"
    if registrar_paciente(codigo_paciente, nombre, edad) == False:
        print("Error: nombre vacío o edad fuera del rango 0 a 120.")
        continue
    print("Registrado:", enmascarar(nombre), "- código", codigo_paciente)

    seguir = input("\n¿Atender a otro paciente? (s/n): ").strip().lower()

print("Fin del programa.")