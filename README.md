# Sistema Kawsay

Prototipo de un sistema para registrar pacientes, médicos, citas y atenciones, hecho con datos ficticios.

**Curso:** Lenguajes de Programación  
**Docente:** Dr. Jhonatan Isaac Vargas Huaman  
**Grupo 3**  
**Lenguaje:** Python 3

## Descripción

Kawsay es un prototipo para organizar el trabajo de un pequeño centro de atención. Con él se puede registrar pacientes y médicos, programar citas y guardar las atenciones en un historial.

El sistema usa solo datos ficticios. No se piden DNI, teléfono, dirección ni datos médicos reales, y los nombres de los pacientes se muestran ocultos (por ejemplo, `A*** P***`).

## Tecnologías

- Python 3
- Git y GitHub
- VS Code

## Requerimientos

| ID | Requerimiento | Funciones |
|---|---|---|
| RF01 | Registrar paciente | `registrar_paciente` |
| RF02 | Registrar médico | `registrar_medico` |
| RF03 | Buscar por código | `buscar_codigo` |
| RF04 | Programar cita | `validar_fecha`, `programar_cita` |
| RF05 | Registrar atención (historial) | `registrar_atencion`, `filtrar_atencion` |

Otras funciones: `crear_persona` (crea un paciente o un médico), `filtrar_especialidad` (lista los médicos por especialidad) y `enmascarar` (oculta los nombres).

## Paradigmas usados

- **Estructurado:** funciones, listas, `while`, `for` y validaciones.
- **Orientado a objetos:** las clases `Paciente`, `Medico` y `Cita`, con atributos protegidos, propiedades y `setters`.
- **Funcional:** `filter()` para buscar sin modificar las listas.

## Estructura del proyecto

```
Sistema-Kawsay/
├── main.py        # Programa principal
├── gestion.py     # Listas y funciones del sistema
├── paciente.py    # Clase Paciente
├── medico.py      # Clase Medico
├── cita.py        # Clase Cita
├── README.md
└── .gitignore
```

## Cómo ejecutarlo

1. Instalar Python 3.
2. Descargar o clonar el repositorio.
3. Abrir una terminal en la carpeta del proyecto y ejecutar:

```
python main.py
```

El programa pide el nombre (ficticio) y la edad del paciente, el código del médico (de `M001` a `M004`), la fecha de la cita (desde hoy hasta el 31/12/2026) y el motivo de la consulta.

## Integrantes

- ADRIHAN SMITH GONZALES LLONTOP
- ALEJANDRO MIGUEL TEQUEN ANGELATS
- JILMAR ALDAIR ALFONSO GARCIA PEDREGAL
- JOSUE EMANUEL CAYAO VILLAFRANCA
- JUAN DAVID ZELADA GRAU

## Repositorio

https://github.com/Bladls/Sistema-Kawsay
