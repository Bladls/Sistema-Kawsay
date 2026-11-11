class Paciente:
    def __init__(self, codigo, nombre, edad):
        self._codigo = codigo
        self._nombre = nombre
        self._edad = edad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @edad.setter
    def edad(self, value):
        self._edad = value

    def resumen(self):
        return f"{self._codigo} - {self._nombre} - {self._edad} años"
