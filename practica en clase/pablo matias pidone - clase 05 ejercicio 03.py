"""
3. A partir del siguiente enunciado, crear las clases necesarias (con
sus respectivos atributos y métodos) para poder representarlos.
↪ “Juan Lopez tiene 25 años y es de profesión Abogado. Por la
tarde, después de trabajar, sale a caminar. También tiene una
bicicleta amarilla marca “Massino” y a veces sale a dar
vueltas en ella”.
● Guardarlo en un archivo llamado ejercicio3.py
"""

import random

class Persona:
    def __init__(self, nombre, apellido, edad, profesion, bicicleta):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.profesion = profesion
        self.Bicicleta = bicicleta
    
    def actividad(self):
        if (random.randint(0, 1) == 0):
            return 'sale a caminar'
        else:
            return 'anda en su bicicleta'
    
    def mostrar(self):
        act = pers01.actividad()
        print("----------------------------------------------------------------------")
        print(f"{self.nombre} {self.apellido} tiene {self.edad} años es de profesion {self.profesion}.")
        if(act == "sale a caminar"):
            print(f"Por la tarde {act}")
        else:
            print(f"Por la tarde {act}, de color {self.Bicicleta.color} y marca {self.Bicicleta.marca}")
        print("----------------------------------------------------------------------")

class Bicicleta:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca


miBici = Bicicleta("amarilla", "Massino")

pers01 = Persona("Juan", "Lopez", 25, "Abogado", miBici)

pers01.mostrar()