class Cita:
    def __init__(self, codigo, paciente, medico, fecha):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha

    @property
    def codigo(self):
        return self._codigo

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    @property
    def fecha(self):
        return self._fecha

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @paciente.setter
    def paciente(self, value):
        self._paciente = value

    @medico.setter
    def medico(self, value):
        self._medico = value

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    def resumen(self):
        return f"{self._codigo}: {self._paciente.nombre} con Dr. {self._medico.nombre} - {self._fecha}"
