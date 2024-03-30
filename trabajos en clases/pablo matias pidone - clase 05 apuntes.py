#Ejemplo POLIMORFISMO

# LIBRERÍA
# LIBROS
# MUSICA (CD, VINILOS)
# PELICULAS

# publicas - pueden ser leidos sin un getter - métodos
# _privadas - solo puedan ser leidos con un getter - atributos

class Producto:
    def __init__(self, _id, _titulo, _autor, _precio):
        self._id = _id
        self._titulo = _titulo
        self._autor = _autor
        self._precio = _precio

class Libro(Producto):
    def __init__(self, _id, _titulo,_autor,_precio, _editorial, _generoLiterario):
        super().__init__(self, _id, _titulo,_autor,_precio)
        self._editorial = _editorial
        self._generoLiterario = _generoLiterario

class Pelicula(Producto):
    def __init__(self, _id, _titulo,_autor,_precio, _duracion, _generoCine):
        super().__init__(self, _id, _titulo,_autor,_precio)
        self._duracion = _duracion
        self._generoCine = _generoCine

class Musica(Producto):
    def __init__(self, _id, _titulo,_autor,_precio, _duracion, _generoMusica):
        super().__init__(self, _id, _titulo,_autor,_precio)
        self._duracion = _duracion
        self._generoMusica = _generoMusica


""" class Auto():
    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo con 18 ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento() """



""" from enum import Enum

class EntidadFinanciera(Enum):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD" """