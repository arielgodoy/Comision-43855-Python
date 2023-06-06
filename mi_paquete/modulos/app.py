from modulos.classes import *
def ingresacompra(bd):
    nomcliente = input("Ingrese Nombre CLiente: ")
    rutcliente = input("Ingrese rut CLiente: ")
    dircliente = input("Ingrese direccion CLiente: ")
    feccliente = "1999-01-01"
    clientecompra=Cliente(nomcliente,rutcliente,dircliente,feccliente)
    articulo = input("articulo: ")
    valor = int(input("Valor: "))

    bd.update({
        nomcliente: {
            'cliente': clientecompra,
            'articulo': articulo,
            'valor': valor,
        }
    })
    print("compra Ingresada Exitosamente")
    return bd

def listacompras(bd):
    for compras, datos in bd.items():
        print(f"Cliente: { datos['cliente'].nombre} Rut { datos['cliente'].rut} , Articulo: {datos['articulo']}, Valor: {datos['valor']}")    
    return bd


def totalcompras(bd):
    total = 0
    for compras, datos in bd.items():
        total = total + datos['valor']    
    print(f"Total compras {total}")
    return bd
