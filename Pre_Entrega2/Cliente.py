from Persona import Persona
    
class Cliente(Persona) :
    def __init__ (self,nombre, apellido, edad,dni,email, telefono ,numCuenta, razon_social:None):
        super().__init__(nombre, apellido, edad,dni,email, telefono)
        self.numCuenta = numCuenta
        self.razon_social = razon_social
        self.articulos = []                
        return print(f"El cliente tiene estos datos:\n Nombre completo: {self.nombre} {self.apellido}, Edad:{self.edad}, DNI: {self.dni}, Email: {self.email}, Telefono: {self.telefono}, Número de cuenta: {self.numCuenta}, Razón social: {self.razon_social}")
    
    def agregar_articulos(self, articulos, cantidad):
        self.articulos.append(articulos)
        self.articulos.append(cantidad)
        return #f"Articulos agregados a la lista"
    
    def listar_articulos (self):
        nombre= self.nombre
        articulos = self.articulos
        return print (f"{nombre} tiene agregados estos artículos para compra: {articulos}")
    
    def valida_dni(self ):
        dni__ = (input(str(f"Ingresa el dni dado por {self.nombre} {self.apellido} : ")))
        if dni__ == self.dni:
            return print(f"El DNI proporcionado por {self.nombre} {self.apellido} es correcto.")
        else:
            return print(f"El DNI no concuerda con el ingresado por {self.nombre}, debe ser actualizado.")
    
    def obtener_email(self):
        return print(f"El correo electrónico del cliente es: {self.email}")

    def __str__(self):
        return f"Es un cliente llamado:{self.nombre} {self.apellido}"

