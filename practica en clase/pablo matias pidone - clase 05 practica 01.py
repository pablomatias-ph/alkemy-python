# Definición de clase madre Producto

class Producto:
    def __init__(self, titulo, precio, stock, genero):
        self.titulo = titulo
        self.precio = precio
        self.stock = stock
        self.genero = genero
    def mostrarProducto(self):
        pass

#Definición de subclases con herencia

class Literatura(Producto):
    def __init__(self, titulo, precio, stock, genero, autor, editorial):
        super().__init__(titulo, precio, stock, genero)
        self.autor = autor
        self.editorial = editorial

    def mostrarProducto(self):
        print('\n---------------------')
        print('Sección Literatura')
        print('---------------------')
        print(f'• Título: {self.titulo}')
        print(f'• Autor: {self.autor}')
        print(f'• Género: {self.genero}')
        print(f'• Editorial: {self.editorial}')
        print(f'• Precio: $ {self.precio}')
        print(f'• Stock: {self.stock} unidades')
        print('---------------------')
        
class CineySeries(Producto):
    def __init__(self, titulo, precio, stock, genero, director, productora):
        super().__init__(titulo, precio, stock, genero)
        self.director = director
        self.productora = productora

    def mostrarProducto(self):
        print('\n---------------------')
        print('Sección Cine y Series')
        print('---------------------')
        print(f'• Título: {self.titulo}')
        print(f'• Director: {self.director}')
        print(f'• Género: {self.genero}')
        print(f'• Productora: {self.productora}')
        print(f'• Precio: $ {self.precio}')
        print(f'• Stock: {self.stock} unidades')
        print('---------------------')


class Musica(Producto):
    def __init__(self, titulo, precio, stock, genero, interprete, sello):
        super().__init__(titulo, precio, stock, genero)
        self.interprete = interprete
        self.sello = sello

    def mostrarProducto(self):
        print('\n---------------------')
        print('Sección Música')
        print('---------------------')
        print(f'• Título: {self.titulo}')
        print(f'• Intéprete: {self.interprete}')
        print(f'• Género: {self.genero}')
        print(f'• Sello: {self.sello}')
        print(f'• Precio: $ {self.precio}')
        print(f'• Stock: {self.stock} unidades')
        print('---------------------')


# Instancia de tres libros

libro = Literatura("El Eternauta", 18600, 5, "Novela fantástica", "Solano López ", "Planeta")
libro.mostrarProducto()

libro = Literatura("Introducción al arte contemporaneo", 14900, 4, "Hitoria del arte", "Anne Cauquelin ", "La Marca")
libro.mostrarProducto()

libro = Literatura("Diseño gráfico argentino en el siglo XX", 11800, 2, "Arquitectura y Diseño", "Carlos Mendez Mosquera ", "Ediciones Infinito")
libro.mostrarProducto()

# Instancia de tres peliculas o series

cineyseries = CineySeries("Showroom", 1872, 1, "Comedia dramática", "Fernando Molnar", "SBP")
cineyseries.mostrarProducto()

cineyseries = CineySeries("Annabelle / El Conjuro", 3536, 2, "Terror", "John R. Leonetti", "HBO")
cineyseries.mostrarProducto()

cineyseries = CineySeries("27, El club de los malditos", 1872, 8, "Acción", "Nicanor Loreti", "Miramax")
cineyseries.mostrarProducto()

#Instancia de tres discos

musica = Musica("Amor Amarillo", 9174, 3, "Rock / Pop en castellano", "Gustavo Ceratti", "Sony Music")
musica.mostrarProducto()

musica = Musica("Adriana Varela / Vivo", 6184, 4, "Tango", "Adriana Varell", "DBN")
musica.mostrarProducto()

musica = Musica("Montreux Jazz Festival", 7583, 1, "Jazz", "Elis Regina", "Warner")
musica.mostrarProducto()