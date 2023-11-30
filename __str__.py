""" #Con string

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad}"

# Crear una instancia de la clase Persona
persona1 = Persona(nombre="Juan", edad=30)

# Imprimir la instancia utilizando el método __str__
print(persona1)
 """



#SIN __str__ metodo

""" Si la clase Persona no tuviera el método __str__, la impresión del objeto podría verse diferente. Sin el método __str__, Python utilizará una representación predeterminada que puede no ser tan informativa y posiblemente mostrará solo la dirección de memoria del objeto """

class PersonaNoStr:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear una instancia de la clase PersonaNoStr
persona2 = PersonaNoStr(nombre="Ana", edad=25)

# Imprimir la instancia sin el método __str__
print(persona2)
