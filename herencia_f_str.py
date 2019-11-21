class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"Hola soy {self.nombre} {self.apellido} y tengo {self.edad} años"

nuevo_estudiente = Estudiante('Yohan','Garcia',24)
print(nuevo_estudiente)