from gestion import registrar_medico

print("=== SISTEMA KAWSAY (prototipo con datos ficticios) ===")
print("Use un nombre inventado para el paciente. No escriba DNI, teléfono ni datos médicos reales.")

base = [["M001", "Luis Ramos", "Medicina general"], ["M002", "Rosa Vega", "Pediatría"],
        ["M003", "Carlos Mena", "Cardiología"], ["M004", "Elena Rojas", "Dermatología"]]
for m in base:
    registrar_medico(m[0], m[1], m[2])
