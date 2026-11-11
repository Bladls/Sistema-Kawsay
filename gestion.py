from datetime import datetime
from paciente import Paciente
from medico import Medico
from cita import Cita

lista_paciente = []
lista_medico = []
lista_cita = []
historial = []

def crear_persona(tipo, codigo, nombre, dato):
    if tipo == "paciente":
        return Paciente(codigo, nombre, dato)
    elif tipo == "medico":
        return Medico(codigo, nombre, dato)
    else:
        return False

def buscar_codigo(lista, codigo):
    for elemento in lista:
        if elemento.codigo == codigo.strip().upper():
            return elemento
    return False

def registrar_paciente(codigo, nombre, edad):
    if buscar_codigo(lista_paciente, codigo) != False or nombre.strip() == "" or edad < 0 or edad > 120:
        return False
    lista_paciente.append(crear_persona("paciente", codigo, nombre.strip(), edad))
    return True

def registrar_medico(codigo, nombre, especialidad):
    if buscar_codigo(lista_medico, codigo) != False or nombre.strip() == "" or especialidad.strip() == "":
        return False
    lista_medico.append(crear_persona("medico", codigo, nombre.strip(), especialidad.strip()))
    return True

def validar_fecha(fecha):
    try:
        dia = datetime.strptime(fecha.strip(), "%d/%m/%Y")
    except ValueError:
        return False
    return dia.date() >= datetime.now().date() and dia <= datetime(2026, 12, 31)

def programar_cita(codigo_paciente, codigo_medico, fecha):
    paciente = buscar_codigo(lista_paciente, codigo_paciente)
    medico = buscar_codigo(lista_medico, codigo_medico)
    if paciente == False or medico == False:
        return False
    cita = Cita(f"C{len(lista_cita) + 1:03d}", paciente, medico, fecha.strip())
    lista_cita.append(cita)
    return cita

def registrar_atencion(codigo, codigo_paciente, codigo_medico, motivo):
    repetido = list(filter(lambda a: a["codigo"] == codigo, historial))
    paciente = buscar_codigo(lista_paciente, codigo_paciente)
    medico = buscar_codigo(lista_medico, codigo_medico)
    if len(repetido) > 0 or paciente == False or medico == False:
        return False
    historial.append({"codigo": codigo, "paciente": codigo_paciente, "medico": codigo_medico, "motivo": motivo.strip()})
    return True
