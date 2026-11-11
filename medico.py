class Medico:
    def __init__(self, codigo, nombre, especialidad):
        self._codigo = codigo
        self._nombre = nombre
        self._especialidad = especialidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def especialidad(self):
        return self._especialidad

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @especialidad.setter
    def especialidad(self, value):
        self._especialidad = value

    def resumen(self):
        return f"{self._codigo} - {self._nombre} - {self._especialidad}"
