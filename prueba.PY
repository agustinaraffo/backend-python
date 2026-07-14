 
class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre 
        self.apellido = apellido 
        self.dni = dni 

class Perro:
    def __init__(self, nombre, edad, id):
        self.nombre = nombre 
        self.edad = edad 
        self.id = id 

class Gato:
    def __init__(self, nombre, edad, id):
        self.nombre = nombre 
        self.edad = edad 
        self.id = id 


persona1 = Persona ("Agustina", "Raffo", 40811481)
perro1 = Perro ("Olivia", 10, 1)
gato1 = Gato ("Cuba", 10, 2)

print (f"""
       Los datos de {persona1.nombre} son:  
       Nombre: {persona1.nombre}  
       Apellido: {persona1.apellido}  
       DNI: {persona1.dni}
       """)

print (f"""
       Los datos de {perro1.nombre} son:  
       Nombre: {perro1.nombre}  
       Edad: {perro1.edad}  
       id: {perro1.id}
       """)

print (f"""
       Los datos de {gato1.nombre} son:  
       Nombre: {gato1.nombre}  
       Edad: {gato1.edad}  
       id: {gato1.id}
       """)