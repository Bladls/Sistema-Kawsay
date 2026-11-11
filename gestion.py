from paciente import Paciente
from medico import Medico

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
