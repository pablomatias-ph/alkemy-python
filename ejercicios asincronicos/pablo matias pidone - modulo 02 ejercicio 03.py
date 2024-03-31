import random

class Persona:
    def __init__(self, nombre, apellido, edad, profesion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.profesion = profesion
           
    def trabajar(self):
        return "estoy trabajando"
    
    def caminar(self):
        return "estoy paseando"

    def andarEnBici(self, bicicleta):
        return bicicleta.pedalear()
            
class Bicicleta:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def pedalear(self):
        return "estoy pedaleando"
    
persona = Persona("Juan", "Lopez", 25, "abogado")
vehiculo = Bicicleta("Massino", "Amarilla")

print ('\n------------------------------------------')
print (f'Soy {persona.nombre} {persona.apellido}')
print (f'Tengo {persona.edad} años')
print (f'Soy {persona.profesion}')
print (f'Ahora mismo {persona.trabajar()}')
print (f'Ahora {persona.caminar()}')
print ('------------------------------------------')
print (f'Ahora doy vueltas en bici: {persona.andarEnBici(vehiculo)}')
print ('------------------------------------------')