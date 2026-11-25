from datetime import datetime
from gestion import (lista_paciente, lista_medico, lista_cita, historial, buscar_codigo, registrar_paciente,
                       registrar_medico, validar_fecha, programar_cita, registrar_atencion,
                       filtrar_especialidad, filtrar_atencion, enmascarar)

print("=== SISTEMA KAWSAY (prototipo con datos ficticios) ===")
print("Use nombres inventados. No escriba DNI, teléfono ni datos médicos reales.")

salir = False
while salir == False:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Buscar paciente por código")
    print("4. Buscar médico por código")
    print("5. Buscar médicos por especialidad")
    print("6. Programar cita")
    print("7. Registrar atención")
    print("8. Ver historial de un paciente")
    print("9. Ver listados (pacientes, médicos y citas)")
    print("0. Salir")
    opcion = input("Elija una opción: ").strip()

    match opcion:
        case "1":
            print("\n--- Registrar paciente ---")
            nombre = input("Apellido y nombre del paciente (ficticio): ")
            while nombre.strip() == "":
                nombre = input("Error: el nombre no puede estar vacío. Escriba el nombre: ")
            edad = ""
            while edad == "":
                try:
                    edad = int(input("Edad del paciente (0 a 120): "))
                    if edad < 0 or edad > 120:
                        print("Error: la edad debe estar entre 0 y 120.")
                        edad = ""
                except ValueError:
                    print("Error: escriba solo números enteros.")
            codigo_paciente = f"P{len(lista_paciente) + 1:03d}"
            if registrar_paciente(codigo_paciente, nombre, edad) == False:
                print("Error: no se pudo registrar al paciente.")
            else:
                print("Paciente registrado:", enmascarar(nombre), "- código", codigo_paciente)

        case "2":
            print("\n--- Registrar médico ---")
            nombre = input("Apellido y nombre del médico (ficticio): ")
            while nombre.strip() == "":
                nombre = input("Error: el nombre no puede estar vacío. Escriba el nombre: ")
            especialidad = ""
            while especialidad == "":
                print("\nEspecialidades disponibles:")
                print("   1. Medicina general")
                print("   2. Pediatría")
                print("   3. Cardiología")
                print("   4. Dermatología")
                print("   5. Ginecología")
                print("   6. Traumatología")
                print("   7. Neurología")
                print("   8. Oftalmología")
                print("   9. Psiquiatría")
                print("   10. Odontología")
                numero = input("Escriba el número de la especialidad: ").strip()
                match numero:
                    case "1":
                        especialidad = "Medicina general"
                    case "2":
                        especialidad = "Pediatría"
                    case "3":
                        especialidad = "Cardiología"
                    case "4":
                        especialidad = "Dermatología"
                    case "5":
                        especialidad = "Ginecología"
                    case "6":
                        especialidad = "Traumatología"
                    case "7":
                        especialidad = "Neurología"
                    case "8":
                        especialidad = "Oftalmología"
                    case "9":
                        especialidad = "Psiquiatría"
                    case "10":
                        especialidad = "Odontología"
                    case _:
                        print("Error: elija un número del 1 al 10.")
            codigo_medico = f"M{len(lista_medico) + 1:03d}"
            if registrar_medico(codigo_medico, nombre, especialidad) == False:
                print("Error: no se pudo registrar al médico.")
            else:
                print("Médico registrado:", nombre.strip(), "-", especialidad.strip(), "- código", codigo_medico)

        case "3":
            print("\n--- Buscar paciente por código ---")
            if len(lista_paciente) == 0:
                print("Aún no hay pacientes registrados. Use la opción 1.")
            else:
                codigo = input("Código del paciente (ejemplo P001; presione Enter para ver la lista): ")
                while codigo.strip() == "":
                    print("\nPacientes registrados:")
                    for p in lista_paciente:
                        print(f"   {p.codigo} - {enmascarar(p.nombre)} - {p.edad} años")
                    codigo = input("\nCódigo del paciente (ejemplo P001): ")
                paciente = buscar_codigo(lista_paciente, codigo)
                if paciente == False:
                    print("No existe un paciente con ese código.")
                else:
                    print(f"Encontrado: {paciente.codigo} - {enmascarar(paciente.nombre)} - {paciente.edad} años")
                    print("Atenciones registradas:", len(filtrar_atencion(paciente.codigo)))

        case "4":
            print("\n--- Buscar médico por código ---")
            if len(lista_medico) == 0:
                print("Aún no hay médicos registrados. Use la opción 2.")
            else:
                codigo = input("Código del médico (ejemplo M001; presione Enter para ver la lista): ")
                while codigo.strip() == "":
                    print("\nMédicos registrados:")
                    for m in lista_medico:
                        print("  ", m.resumen())
                    codigo = input("\nCódigo del médico (ejemplo M001): ")
                medico = buscar_codigo(lista_medico, codigo)
                if medico == False:
                    print("No existe un médico con ese código.")
                else:
                    print("Encontrado:", medico.resumen())

        case "5":
            print("\n--- Buscar médicos por especialidad ---")
            if len(lista_medico) == 0:
                print("Aún no hay médicos registrados. Use la opción 2.")
            else:
                especialidad = input("Especialidad a buscar (ejemplo: pedi; deje vacío para ver todos): ")
                encontrados = filtrar_especialidad(especialidad)
                if len(encontrados) == 0:
                    print("No hay médicos con esa especialidad.")
                for m in encontrados:
                    print("  ", m.resumen())

        case "6":
            print("\n--- Programar cita ---")
            if len(lista_paciente) == 0 or len(lista_medico) == 0:
                print("Primero debe registrar al menos un paciente y un médico.")
            else:
                codigo_paciente = input("Código del paciente (ejemplo P001; presione Enter para ver la lista): ")
                while buscar_codigo(lista_paciente, codigo_paciente) == False:
                    if codigo_paciente.strip() == "":
                        print("\nPacientes registrados:")
                        for p in lista_paciente:
                            print(f"   {p.codigo} - {enmascarar(p.nombre)} - {p.edad} años")
                        codigo_paciente = input("\nCódigo del paciente (ejemplo P001): ")
                    else:
                        codigo_paciente = input("Error: el código no existe. Escriba otro código de paciente: ")

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
                print(f"Cita programada -> {cita.codigo}: {enmascarar(cita.paciente.nombre)} con Dr. {cita.medico.nombre} - {cita.fecha}")

        case "7":
            print("\n--- Registrar atención ---")
            if len(lista_paciente) == 0 or len(lista_medico) == 0:
                print("Primero debe registrar al menos un paciente y un médico.")
            else:
                codigo_paciente = input("Código del paciente (ejemplo P001; presione Enter para ver la lista): ")
                while buscar_codigo(lista_paciente, codigo_paciente) == False:
                    if codigo_paciente.strip() == "":
                        print("\nPacientes registrados:")
                        for p in lista_paciente:
                            print(f"   {p.codigo} - {enmascarar(p.nombre)} - {p.edad} años")
                        codigo_paciente = input("\nCódigo del paciente (ejemplo P001): ")
                    else:
                        codigo_paciente = input("Error: el código no existe. Escriba otro código de paciente: ")
                codigo_medico = input("Código del médico (ejemplo M001; presione Enter para ver la lista): ")
                while buscar_codigo(lista_medico, codigo_medico) == False:
                    if codigo_medico.strip() == "":
                        print("\nMédicos registrados:")
                        for m in lista_medico:
                            print("  ", m.resumen())
                        codigo_medico = input("\nCódigo del médico (ejemplo M001): ")
                    else:
                        codigo_medico = input("Error: el código no existe. Escriba otro código de médico: ")
                motivo = input("Motivo de la consulta (ejemplo: control general): ")
                while motivo.strip() == "":
                    motivo = input("Error: el motivo no puede estar vacío. Escriba el motivo: ")
                # buscar_codigo normaliza el código; se usa el código real del objeto
                codigo_paciente = buscar_codigo(lista_paciente, codigo_paciente).codigo
                codigo_medico = buscar_codigo(lista_medico, codigo_medico).codigo
                registrar_atencion(f"A{len(historial) + 1:03d}", codigo_paciente, codigo_medico, motivo)
                print("Atención registrada.")

        case "8":
            print("\n--- Historial de un paciente ---")
            if len(lista_paciente) == 0:
                print("Aún no hay pacientes registrados. Use la opción 1.")
            else:
                codigo = input("Código del paciente (ejemplo P001; presione Enter para ver la lista): ")
                while codigo.strip() == "":
                    print("\nPacientes registrados:")
                    for p in lista_paciente:
                        print(f"   {p.codigo} - {enmascarar(p.nombre)} - {p.edad} años")
                    codigo = input("\nCódigo del paciente (ejemplo P001): ")
                paciente = buscar_codigo(lista_paciente, codigo)
                if paciente == False:
                    print("No existe un paciente con ese código.")
                else:
                    propia = filtrar_atencion(paciente.codigo)
                    print(f"Historial de {paciente.codigo} - {enmascarar(paciente.nombre)} ({len(propia)} atenciones):")
                    if len(propia) == 0:
                        print("   Sin atenciones registradas.")
                    for a in propia:
                        print(f"   {a['codigo']} | médico Dr. {buscar_codigo(lista_medico, a['medico']).nombre} | motivo: {a['motivo']}")

        case "9":
            print("\n--- Pacientes registrados ---")
            if len(lista_paciente) == 0:
                print("   Ninguno.")
            for p in lista_paciente:
                print(f"   {p.codigo} - {enmascarar(p.nombre)} - {p.edad} años")
            print("\n--- Médicos registrados ---")
            if len(lista_medico) == 0:
                print("   Ninguno.")
            for m in lista_medico:
                print("  ", m.resumen())
            print("\n--- Citas programadas ---")
            if len(lista_cita) == 0:
                print("   Ninguna.")
            for c in lista_cita:
                print(f"   {c.codigo}: {enmascarar(c.paciente.nombre)} con Dr. {c.medico.nombre} - {c.fecha}")

        case "0":
            salir = True

        case _:
            print("Opción no válida. Elija un número del 0 al 9.")

print("\nTotal de pacientes:", len(lista_paciente), "| médicos:", len(lista_medico), "| citas:", len(lista_cita), "| atenciones:", len(historial))
print("Fin del programa.")
