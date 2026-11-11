from datetime import datetime
from gestion import (lista_paciente, lista_medico, buscar_codigo, registrar_paciente, registrar_medico,
                       validar_fecha, programar_cita, filtrar_especialidad, enmascarar)

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

    print("\nMédicos disponibles:")
    for m in filtrar_especialidad(""):
        print("  ", m.resumen())

    codigo_medico = input("Código del médico (ejemplo M001): ")
    while buscar_codigo(lista_medico, codigo_medico) == False:
        codigo_medico = input("Error: el código no existe. Escriba otro código de médico: ")

    hoy = datetime.now().strftime("%d/%m/%Y")
    fecha = input(f"Fecha de la cita dd/mm/aaaa (desde hoy {hoy} hasta 31/12/2026): ")
    while validar_fecha(fecha) == False:
        fecha = input("Error: fecha no válida. Escriba otra fecha (dd/mm/aaaa): ")
    cita = programar_cita(codigo_paciente, codigo_medico, fecha)
    print(f"Cita programada -> {cita.codigo}: {enmascarar(nombre)} con Dr. {cita.medico.nombre} - {cita.fecha}")

    seguir = input("\n¿Atender a otro paciente? (s/n): ").strip().lower()

print("Fin del programa.")