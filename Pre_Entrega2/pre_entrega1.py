BD_usuarios = { "jorge"   : "123",
                "ana"     : "abc1",
                "julia"   : "abc2",
                "fernando": "abc3",
                "roberto" : "abc4"
                }

def registroUsuarios():
    nombre =    input("Ingresa un nombre de usuario: ")
    contrasena= input("Ingrese una contraseña de usuario: ")

    while nombre in BD_usuarios:
        nombre = input("Usuario ya existente, por favor ingresa otro: ")
        contrasena= input("Ingrese una contraseña de usuario: ")

    registro= BD_usuarios.update({nombre:contrasena}) 
    return print(f"{nombre} ha sido registrado con exito!!!: ")


def leerDatos():
    mostrarDatos= print(BD_usuarios)
    return mostrarDatos

def login():
    acceso=False
    while acceso == False:
        nombre = input("Ingrese un nombre de usuario: ")
        if nombre in (BD_usuarios):
            passwordCorrecto = False
            while passwordCorrecto == False:
                password = input("ingrese una contraseña: ")
                if password == BD_usuarios[nombre]:
                    passwordCorrecto = True
                    acceso = True
                else: 
                    print("Credenciales Inválidas")
        else:
            print("No es un usuario valido")
                
    return print("Acceso concedido!!")


registroUsuarios()
leerDatos()
login()