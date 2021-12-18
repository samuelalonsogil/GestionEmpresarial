class Articulo:
    MAX_ESTRELLAS_PERMITIDAS = 10000

    def __init__(self, nombre, id, estrellas_asignadas):
        self.nombre = nombre
        self.id = id
        self.estrellas_asignadas = estrellas_asignadas

    def __str__(self):
        return self.nombre + " " + self.id + " " + str(self.estrellas_asignadas)

    def suma_total_estrellas(self):
        return self.estrellas_asignadas.sum()

    def media_total_estrellas(self):
        return self.estrellas_asignadas.sum() / len(self.estrellas_asignadas)

    def validar_estrellas(self):
        if self.estrellas_asignadas <= Articulo.MAX_ESTRELLAS_PERMITIDAS:
            return True
        elif self.estrellas_asignadas < 0:
            return False

        elif self.estrellas_asignadas == list(filter(lambda l: l[2] < 0, list)
                                              or self.estrellas_asignadas == list(filter(lambda l: l[2] > 5, list))
                                              or self.estrellas_asignadas == list(
            filter(lambda l: isinstance(l[2], int) != True, list))):
            return False

        else:
            return False


articulo = Articulo("samu", "2", [1, 2, 3])
print(articulo.validar_estrellas())
