""" Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que el libro se elimine. class Libro(): """


class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")

# Crear una instancia de la clase Libro
libro = Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", cantidad_paginas=500)

# Eliminar la instancia de la clase Libro
del libro
