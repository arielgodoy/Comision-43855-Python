from modulos import app
from modulos.classes import *

##### ingreso compras de prueba en la BD #####
cliente1=Cliente("cliente uno","11.111.111-1","Avda. Los unos #1","1111-11-11")
cliente2=Cliente("cliente dos","22.222.222-2","Avda. Los dos #22","2222-22-22")
cliente3=Cliente("cliente tres","33.333.333-3","Avda. Los tres #333","3333-33-33")
bd = {
    'compra1': {
        'cliente': cliente1,
        'articulo': 'articulo 1',
        'valor': 1000

    },
    'compra2': {
        'cliente': cliente2,
        'articulo': 'articulo 2',
        'valor': 1000

    },
    'compra3': {
        'cliente': cliente3,
        'articulo': 'articulo 3',
        'valor': 1000

    },   
}



while True:
    print("1.- Ingresar compra")    
    print("2.- Lista compras")
    print("3.- Total Compras")
    print("4.- Salir")

    opcion = input('Ingrese Opción: ')
    try:
        opcion = int(opcion)
    except ValueError:
        print('Opción inválida. Reintente.')
        continue

    if 0 < opcion <= 4:
        if opcion == 1:
            app.ingresacompra(bd)        
        elif opcion == 2:
            app.listacompras(bd)  
        elif opcion == 3:
            app.totalcompras(bd)  
        elif opcion == 4:
            break
    else:
        print('Opción inválida. Reintente')
