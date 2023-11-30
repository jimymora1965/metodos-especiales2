
import os
class Libro:
    def __init__(self,titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __len__(self):
        return int(self.paginas)
    
def limpiar_consola():
    os.system("cls")

limpiar_consola()

libro = Libro(titulo = "Cien años de soledad", autor= "Gabriel Garcia Marquez", paginas= 400)
longitud_libro = len(libro)
print(f"El libro tiene {longitud_libro} páginas ")
