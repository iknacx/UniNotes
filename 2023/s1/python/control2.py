#| Crear una clase de nombre Estudiante, con los atributos:
#| * Nombres
#| * Apellidos
#| * Carrera
#| * Calificación promedio.
#| Cree un metodo de construccion (__init__), para inicializar los valores de los atributos
#| Ademas cree un objeto de tipo Estudiante y asigne valores a sus atributos
#| Finalmente visualice los valores de los objetos de tipo Estudiante creado

class Estudiante:
    # Atributos de la clase Estudiante
    nombres = ""
    apellidos = ""
    carrera = ""
    promedio = 0.0

    # Constructor de la clase
    def __init__(self, nombres, apellidos, carrera, promedio):
        self.nombres = nombres
        self.apellidos = apellidos
        self.carrera = carrera
        self.promedio = promedio

    # Metodo de la clase para poder usar la clase en print()
    def __str__(self):
        return f"Estudiante\n\tNombres: {self.nombres}\n\tApellidos: {self.apellidos}\n\tCarrera: {self.carrera}\n\tCalificación promedio: {self.promedio}"

# Pedir los atributos al usuario
nombres = input("Ingrese los dos nombres: ")
apellidos = input("Ingrese los dos apellidos: ")
carrera = input("Ingrese la carrera del estudiante: ")
promedio = float(input("Ingrese la calificación promedio: "))

# Inicializar la clase Estudiante con los atributos pedidos
estudiante = Estudiante(nombres, apellidos, carrera, promedio)

# Mostrar la variable de acuerdo al metodo __str__
print(estudiante)
