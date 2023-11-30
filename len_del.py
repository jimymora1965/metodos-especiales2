class Alumno:
    def __init__(self, nombre, apellido, numero_alumno):
        self.nombre = nombre
        self.apellido = apellido
        self.n_a = numero_alumno

    def __str__(self):
        return f"El alumno se llama {self.nombre}, apellido {self.apellido} y hay {self.n_a} alumnos en total."
    
    def __len__(self):
        return int(self.n_a)
    
    def __del__(self):
        print("Alumno eliminado")

# Crear una instancia de la clase Alumno
alumno1 = Alumno(nombre="Jimy", apellido="Mora", numero_alumno="45")

# Utilizar el método __str__
print(alumno1)

# Utilizar el método __len__
cantidad_alumnos= len(alumno1)
print(f"El número del alumno en la lista es el: {cantidad_alumnos}")

# Utilizar el método __del__ (eliminar la instancia)
del alumno1
