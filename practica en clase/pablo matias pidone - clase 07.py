from enum import Enum

class TipoInstrumento(Enum):
    PERCUSION = "Percusión"
    VIENTO = "Viento"
    CUERDA = "Cuerda"

class Instrumento:
    def __init__(self, id, nombreInstrumento, precio, tipo):
        self.id = id
        self.nombreInstrumento = nombreInstrumento
        self.precio = precio
        self.tipo = tipo

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def listarInstrumentos(self):
        for instrumento in self.instrumentos:
            print("ID:", instrumento.id)
            print("Nombre:", instrumento.nombreInstrumento)
            print("Precio: $", instrumento.precio)
            print("Tipo:", instrumento.tipo.value)
            print("----------------------------------")

    def tipoInstrumentos(self, tipo):
        return [instrumento for instrumento in self.instrumentos if instrumento.tipo == tipo]

    def borrarInstrumento(self, id):
        self.instrumentos = [instrumento for instrumento in self.instrumentos if instrumento.id != id]

    def porcTipoInstrumentos(self):
        tipos = {tipo: 0 for tipo in TipoInstrumento}
        total = len(self.instrumentos)
        for instrumento in self.instrumentos:
            tipos[instrumento.tipo] += 1
        porcentajes = {tipo: (count / total) * 100 for tipo, count in tipos.items()}
        return porcentajes

class Fabrica:
    def __init__(self):
        self.listaSucursales = []

    def agregarSucursal(self, sucursal):
        self.listaSucursales.append(sucursal)

    def listarInstrumentos(self):
        for sucursal in self.listaSucursales:
            print(f"SUCURSAL:\n{sucursal.nombre}")
            print("----------------------------------")
            sucursal.listarInstrumentos()

    def tipoInstrumentos(self, tipo):
        instrumentos = []
        for sucursal in self.listaSucursales:
            instrumentos.extend(sucursal.tipoInstrumentos(tipo))
        return instrumentos

    def borrarInstrumento(self, id):
        for sucursal in self.listaSucursales:
            sucursal.borrarInstrumento(id)

    def porcTipoInstrumentos(self, nombre_sucursal):
        for sucursal in self.listaSucursales:
            if sucursal.nombre == nombre_sucursal:
                return sucursal.porcTipoInstrumentos()
        return None

# Ejemplo de uso
if __name__ == "__main__":
    fabrica = Fabrica()

    # Crear sucursales
    sucursal1 = Sucursal("Escuela de Musica")
    sucursal1.instrumentos.append(Instrumento("A001", "Bombo Legüero", 6100, TipoInstrumento.PERCUSION))
    sucursal1.instrumentos.append(Instrumento("A002", "Flauta Dulce", 2150, TipoInstrumento.VIENTO))
    sucursal1.instrumentos.append(Instrumento("A003", "Bajo acustico", 2500, TipoInstrumento.CUERDA))
    sucursal1.instrumentos.append(Instrumento("A004", "Violonchelo", 6200, TipoInstrumento.CUERDA))
    sucursal1.instrumentos.append(Instrumento("A005", "Violin", 8200, TipoInstrumento.CUERDA))

    sucursal2 = Sucursal("Peatonal")
    sucursal2.instrumentos.append(Instrumento("B001", "Tambor redoblante", 1240, TipoInstrumento.PERCUSION))
    sucursal2.instrumentos.append(Instrumento("B002", "Arpa", 1580, TipoInstrumento.CUERDA))
    sucursal2.instrumentos.append(Instrumento("B003", "Bajo", 1250, TipoInstrumento.CUERDA))
    sucursal2.instrumentos.append(Instrumento("B004", "Tambor redoblante", 1240, TipoInstrumento.PERCUSION))
    sucursal2.instrumentos.append(Instrumento("B005", "Platillos", 5240, TipoInstrumento.PERCUSION))


    # Agregar sucursales a la fábrica
    
    fabrica.agregarSucursal(sucursal1)
    fabrica.agregarSucursal(sucursal2)

    # A) Listar instrumentos de todas las sucursales
    
    print("\nListar Instrumentos de todas las sucursales:")
    print("----------------------------------")
    fabrica.listarInstrumentos()

    # B) Buscar instrumentos por tipo
    
    tipo_buscar = TipoInstrumento.PERCUSION
    print(f"\nInstrumentos de tipo '{tipo_buscar.value}':")
    instrumentos_tipo = fabrica.tipoInstrumentos(tipo_buscar)
    for instrumento in instrumentos_tipo:
        print("ID:", instrumento.id)
        print("Nombre:", instrumento.nombreInstrumento)
        print("Precio: $", instrumento.precio)
        print()

    tipo_buscar = TipoInstrumento.CUERDA
    print(f"\nInstrumentos de tipo '{tipo_buscar.value}':")
    instrumentos_tipo = fabrica.tipoInstrumentos(tipo_buscar)
    for instrumento in instrumentos_tipo:
        print("ID:", instrumento.id)
        print("Nombre:", instrumento.nombreInstrumento)
        print("Precio: $", instrumento.precio)
        print()

    # C) Borrar un instrumento por ID
        
    id_borrar = 'B003'
    fabrica.borrarInstrumento(id_borrar)
    print(f"Instrumento con ID {id_borrar} eliminado de todas las sucursales.")

    # D) Porcentaje de instrumentos por tipo en una sucursal
    
    sucursal_nombre = 'Peatonal'
    print(f"\nPorcentaje de instrumentos por tipo en {sucursal_nombre}:")
    print("-------------------------------------")
    porcentajes = fabrica.porcTipoInstrumentos(sucursal_nombre)
    if porcentajes:
        for tipo, porcentaje in porcentajes.items():
            print(f"{tipo.value}: {porcentaje:.2f}%")
    else:
        print("Sucursal no encontrada.")