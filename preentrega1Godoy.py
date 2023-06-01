
def ingresausuario(bd):
    nombre = input("Ingrese Nombre: ")
    password = input("Ingrese Password: ")
    bd.update({
        nombre: {
            'usuario': nombre,
            'password': password
        }
    })
    print("Usuario Ingresado Exitosamente")
    return bd

def modificausuario(bd):
    nombre = input("Ingrese Nombre usuario a Editar: ")
    if nombre in bd:
        password = input("Ingrese Nuevo Password: ")
        bd[nombre]['password'] = password
        print("Password actualizado")
    else:
        print("Usuario no existe")
    return bd

def eliminaausuario(bd):
    nombre = input("Ingrese Nombre usuario a Eliminar: ")
    if nombre in bd:
        del bd[nombre]
        print("Elemento eliminado.")
    else:
        print("Usuario no existe")
    return bd

def listausuario(bd):
    for nombre, datos in bd.items():
        print(f"Usuario: {nombre}, Contraseña: {datos['password']}")
    return bd

def datosdeprueba(bd):
    for i in range(20):
        nombre = 'usuario' + str(i)
        password = 'password' + str(i)
        bd[nombre] = {
            'usuario': nombre,
            'password': password
        }
    print("Datos de prueba ingresados a la BD")
    return bd

def loginusuario(bd):
    nombre = input("Ingrese usuario: ")
    if nombre in bd:
        password = input("Ingrese contraseña: ")
        if validar_contrasena(nombre, password, bd):
            print(f"Contraseña válida. ############## USUARIO LOGUEADO {nombre} ##############")
        else:
            print(f"Contraseña incorrecta. ############## ACCESO DENEGADO {nombre} ##############")
    else:
        print("Usuario no existe")
    return bd

def validar_contrasena(nombre, password, bd):
    if nombre in bd:
        if bd[nombre]['password'] == password:
            return True
    return False


bd = {
    'usuario1': {
        'usuario': 'usuario1',
        'password': '123456'
    },
    'usuario2': {
        'usuario': 'usuario2',
        'password': 'password123'
    },
    'usuario3': {
        'usuario': 'usuario3',
        'password': 'qwerty'
    }
}

while True:
    print("1.- Ingresar Usuario")
    print("2.- Editar Usuario")
    print("3.- Lista usuarios")
    print("4.- Eliminar usuario")
    print("5.- Asignar Datos de prueba")
    print("6.- LOGIN DE USUARIO")
    print("7.- Salir")

    opcion = input('Ingrese Opción: ')

    try:
        opcion = int(opcion)
    except ValueError:
        print('Opción inválida. Reintente.')
        continue

    if 0 < opcion <= 7:
        if opcion == 1:
            ingresausuario(bd)
        elif opcion == 2:
            modificausuario(bd)
        elif opcion == 3:
            listausuario(bd)
        elif opcion == 4:
            eliminaausuario(bd)
        elif opcion == 5:
            datosdeprueba(bd)
        elif opcion == 6:
            loginusuario(bd)
        elif opcion == 7:
            break
    else:
        print('Opción inválida. Reintente')







        