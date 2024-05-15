class Persona:

    def __init__(self, nombre, apellido, edad,dni,email, telefono:None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.email = email
        self.telefono = telefono
        
    def saluda(self):
        return f"Hola, buen día {self.nombre} {self.apellido}"
    
    def __str__(self):
        return f"Es una persona llamado:{self.nombre} {self.apellido}"