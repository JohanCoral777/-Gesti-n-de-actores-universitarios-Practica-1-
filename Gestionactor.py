class Actor:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return f"Actor: {self.nombre}, Tipo: {self.tipo}"

class Estudiante(Actor):
    def __init__(self, nombre, tipo, carrera):
        super().__init__(nombre, tipo)
        self.carrera = carrera

    def __str__(self):
        return f"{super().__str__()}, Carrera: {self.carrera}"

class Profesor(Actor):
    def __init__(self, nombre, tipo, materia):
        super().__init__(nombre, tipo)
        self.materia = materia

    def __str__(self):
        return f"{super().__str__()}, Materia: {self.materia}"