# Defino la clase empleado

class Empleado:
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContrato):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioIngreso = anioIngreso
        self.tipoContrato = tipoContrato

    def calcularSalarioTotal(self):
        pass

#Defino clase Empleado a comisión

class EmpComision(Empleado):
    
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContrato, salarioMinimo, numClientesCaptados, montoPorCliente):
        super().__init__(dni, nombre, apellido, anioIngreso, tipoContrato)
        self.salarioMinimo = salarioMinimo
        self.numClientesCaptados = numClientesCaptados
        self.montoPorCliente = montoPorCliente

    def calcularSalarioTotal(self):
        salarioComision = self.numClientesCaptados * self.montoPorCliente
        return max(salarioComision, self.salarioMinimo)
        
  
        
# Defino empleado asalariado

class EmpSalario(Empleado):
    
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContrato, salarioFijo):
        super().__init__(dni, nombre, apellido, anioIngreso, tipoContrato)
        self.salarioFijo = salarioFijo

    def calcularSalarioTotal(self):
        antiguedad = 2024 - self.anioIngreso
        salario = self.salarioFijo
        if(antiguedad > 5):
            return salario * 1.1
        elif (antiguedad > 1):
            return salario * 1.05
        else: return salario

# Metodo para mostrar los empleados y sus salarios

def mostrarSalario(empleados):
        for empleado in empleados:
            salario = empleado.calcularSalarioTotal()
            print (f'\nEmpleado: {empleado.nombre} {empleado.apellido}')
            print (f'Tipo de contrato: {empleado.tipoContrato}')
            print (f'Salario: ${empleado.calcularSalarioTotal():,.2f}')


empleados = [

    # Empleados a comisión

    EmpComision(26898079, "Francisco", "Sandine", 2018, "Comisión", 350000, 18, 25000),
    EmpComision(35698079, "Daniela", "Andrada", 2005, "Comisión", 350000, 25, 25000),
    EmpComision(28098089, "Julian", "Decine", 2023, "Comisión", 350000, 9, 25000),
    EmpComision(19998035, "Martina", "Salvia", 2012, "Comisión", 350000, 3, 25000),
    EmpComision(35899546, "Andrea", "D'AGostino", 2016, "Comisión", 350000, 11, 25000),
    
    #Empleados salario fijo
    
    EmpSalario(32156998, "Estefanía", "Deharbe", 2018, "Salario Fijo", 385000),
    EmpSalario(19659665, "Alejandra", "Salerno", 2012, "Salario Fijo", 590000),
    EmpSalario(23658887, "Marcos", "Denis", 2010, "Salario Fijo", 359000),
    EmpSalario(26889659, "Helena", "Marquin", 2004, "Salario Fijo", 688000),
    EmpSalario(23332150, "Santiago", "Azcuenaga", 2005, "Salario Fijo", 665000)

]

mostrarSalario(empleados)


#Calculo el dato de quien tuvo más clientes captados en el período liquidado

def empleadoConMasClientes(empleados):
    maxClientes = 0
    empleadoMaxClientes = None
    for empleado in empleados:
        if isinstance(empleado, EmpComision):
            if empleado.numClientesCaptados > maxClientes:
                maxClientes = empleado.numClientesCaptados
                empleadoMaxClientes = empleado
    return empleadoMaxClientes

empleado = empleadoConMasClientes(empleados)
print('\n_________________________')
print ('\nDato destacado del mes:')
print(f"{empleado.nombre} {empleado.apellido} captó el máximo de {empleado.numClientesCaptados} clientes en el período liquidado")
print('_________________________')