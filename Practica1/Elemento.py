class Elemento:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.plataforma = None

    def obtenerCodigo(self):
        return self.codigo

    def obtenerNombre(self):
        return self.nombre

    def obtenerPlataformas(self):
        return self.plataforma

    def asignarPlataforma(self, plataforma):
        self.plataforma = plataforma