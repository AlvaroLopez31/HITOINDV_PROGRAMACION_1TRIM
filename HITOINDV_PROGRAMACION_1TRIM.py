# APLICACION DE GESTION DE PEDIDOS
# Puntos a hacer:
#   1.Registar Cliente: Pedir datos personales y de facturacion (Pueden ser españoles o extranjeros)
#       -> Datos Personales: DNI, Nombre y Apellidos, Direccion, Pais, Telefono, Mail.
#       -> Datos de Facturacion: DNI, Nombre y Apellidos, Direccion, Pais, Telefono, Mail.
#       -> Pueden ser iguales.
#
#   2.Visualizar clientes registrados
#   3.Realizar busquedas de clientes
#   4.Realizar una compra (Asociada a un cliente y con uno o varios productos)
#   5.Seguimiento de una compra: SMS al movil y mensaje al correo con datos del pedido y codigo de
#       seguimiento


import random

# -------------Estructuras-------------
# Clientes
lista_clientes = []
lista_clientes.append(dict(datos_personales = dict(dni = "09034244T", nombre = "Pepito", apellidos = "Diaz Vivar",
                                                    direccion = "Calle Mayor, 1 - 28000 Madrid", pais = "Españita",
                                                    telefono = "+34 623 23 13 31", mail = "aaa@aaa.es"),
                            datos_fiscales = dict(nif = "09034244T", nombre_fiscal = "Pepito Diaz Vivar",
                                                     direccion_fiscal = "Calle Mayor, 1 - 28000 Madrid",
                                                     pais_fiscal = "Españita", telefono_fiscal = "+34 623 23 13 31",
                                                     mail_fiscal = "aaa@aaa.es")))
lista_clientes.append(dict(datos_personales = dict(dni = "09434345C", nombre = "Juanito", apellidos = "Jimenez Lopez",
                                                    direccion = "Avenida de los Campos Eliseos, 1 - 65273 Paris", pais = "Francia",
                                                    telefono = "+34 623 54 65 63", mail = "bbb@bbb.fr"),
                            datos_fiscales = dict(nif = "09434345C", nombre_fiscal = "Juanito Jimenez Lopez",
                                                     direccion_fiscal = "Avenida de los Campos Eliseos, 1 - 65273 Paris",
                                                     pais_fiscal = "Francia", telefono_fiscal = "+34 623 54 65 63",
                                                      mail_fiscal = "bbb@bbb.fr")))

# Productos
lista_productos = []
lista_productos.append(dict(nombre = "Air Force One", precio = 150.00))
lista_productos.append(dict(nombre = "Jordan 1", precio = 120.00))
lista_productos.append(dict(nombre = "Nike Tn", precio = 110.00))
lista_productos.append(dict(nombre = "New Balance Classics", precio = 100.00))
lista_productos.append(dict(nombre = "Adidas Gazelle", precio = 79.99))

# Compras
lista_pedidos = []
lista_pedidos.append(dict(cliente = lista_clientes[0], carrito = lista_productos, numero_seguimiento ="123"))
lista_pedidos.append(dict(cliente = lista_clientes[1], carrito = lista_productos, numero_seguimiento ="546"))



# Registro de cliente
def registro_cliente(lista_clientes):
    print("--Registro de Cliente--", "\tDatos Personales: ", sep="\n")
    dni_cliente = input("\t\tIntroduce el DNI del nuevo cliente: ")
    nombre_cliente = input("\t\tIntroduce el nombre del nuevo cliente: ")
    apellidos_cliente = input("\t\tIntroduce los apellidos del nuevo cliente: ")
    direccion_cliente = input("\t\tIntroduce la direccion del nuevo cliente: ")
    pais_cliente = input("\t\tIntroduce el pais del nuevo cliente: ")
    telefono_cliente = input("\t\tIntroduce el telefono del nuevo cliente: ")
    mail_cliente = input("\t\tIntroduce el mail del nuevo cliente: ")
    nif = ""
    nombre_fiscal = ""
    direccion_fiscal = ""
    pais_fiscal = ""
    telefono_fiscal = ""
    mail_fiscal = ""

    while True:
        facturacion_igual = input("\t\t¿Los datos de facturacion son iguales a los personales? (S/N): ")
        if  (facturacion_igual == "S" or facturacion_igual == "s"):
            nif = dni_cliente
            nombre_fiscal = nombre_cliente + apellidos_cliente
            direccion_fiscal = direccion_cliente
            pais_fiscal = pais_cliente
            telefono_fiscal = telefono_cliente
            mail_fiscal = mail_cliente
            break

        elif (facturacion_igual == "N" or facturacion_igual == "n"):
            print("\tDatos Fiscales: ")
            nif = input("\t\tIntroduce el NIF de la factura: ")
            nombre_fiscal = input("\t\tIntroduce el nombre de la factura: ")
            direccion_fiscal = input("\t\tIntroduce la direccion de la factura: ")
            pais_fiscal = input("\t\tIntroduce el pais de la factura: ")
            telefono_fiscal = input("\t\tIntroduce el telefono de la factura: ")
            mail_fiscal = input("\t\tIntroduce el mail de la factura: ")
            break
        else:
            print("Introduce una opcion correcta.")



    datos_personales = dict(dni = dni_cliente, nombre = nombre_cliente, apellidos = apellidos_cliente,
                         direccion = direccion_cliente, pais = pais_cliente, telefono = telefono_cliente,
                          mail = mail_cliente)

    datos_fiscales = dict(nif = nif, nombre_fiscal = nombre_fiscal, direccion_fiscal = direccion_fiscal,
                            pais_fiscal = pais_fiscal, telefono_fiscal = telefono_fiscal, mail_fiscal = mail_fiscal)

    nuevo_cliente = dict(datos_personales = datos_personales, datos_fiscales = datos_fiscales)

    lista_clientes.append(nuevo_cliente)
    print("\tLos datos del cliente creado son: ")
    imprimir_cliente(nuevo_cliente)

def imprimir_cliente(cliente):
    print("\tDNI: ", cliente["datos_personales"]["dni"], ", Nombre: ", cliente["datos_personales"]["nombre"], ", Apellidos: ", cliente["datos_personales"]["apellidos"],
          ", Telefono: ", cliente["datos_personales"]["telefono"], ", Pais: ", cliente["datos_personales"]["pais"], sep="")


def visualizar_clientes(lista_clientes):
    print("Lista de Clientes:")
    for cliente in lista_clientes:
        imprimir_cliente(cliente)


def buscar_cliente(dni_buscar,lista_clientes):
    for cliente in lista_clientes:
        if dni_buscar == cliente["datos_personales"]["dni"]:
            return cliente
    return False


def buscar_producto(producto_buscar, lista_productos):
    for producto in lista_productos:
        if producto_buscar == producto["nombre"]:
            return producto
    return False


def imprimir_producto(producto):
    print("\tNombre: ", producto["nombre"], ", Precio: ", producto["precio"], "€", sep="")


def visualizar_productos(lista_productos):
    print("Lista de Productos:")
    for producto in lista_productos:
        imprimir_producto(producto)


def realizar_compra(lista_clientes, lista_productos,lista_pedidos):
    carrito = []
    print("--Realizar Compra--")
    dni_compra = input("Introduce el DNI del cliente que realiza la compra: ")
    cliente_compra = buscar_cliente(dni_compra, lista_clientes)
    if cliente_compra != False:
        print("¿Que productos quieres comprar?")
        visualizar_productos(lista_productos)
        while True:
            producto_buscar = input("Introduce el nombre para añadirlo a la lista (Para salir, escribe \"salir\"): ")
            producto_encontrado = buscar_producto(producto_buscar, lista_productos)
            if producto_encontrado != False:
                carrito.append(producto_encontrado)
            elif producto_buscar == "salir":
                break
            else:
                print("El producto introducido no existe, intentalo de nuevo.")

        numero_seguimiento = random.randint(0, 1000)
        pedido = dict(cliente = cliente_compra, carrito = carrito, numero_seguimiento = numero_seguimiento)
        lista_pedidos.append(pedido)
        print("Se ha realizado la compra.")
        imprimir_datos_pedido(pedido)


    else:
        print("No existe ningun usuario con ese DNI.")


def imprimir_datos_pedido(pedido):
    print("Cliente: ", pedido["cliente"]["datos_personales"]["dni"], ", Numero de productos: ", len(pedido["carrito"]),
          ", Numero de seguimiento: ", pedido["numero_seguimiento"])


def visualizar_pedidos(lista_pedidos):
    print("Lista de Pedidos:")
    for pedido in lista_pedidos:
        imprimir_datos_pedido(pedido)


def buscar_pedido(pedido_buscar, lista_pedidos):
    for pedido in lista_pedidos:
        if pedido_buscar == pedido["numero_seguimiento"]:
            return pedido
    return False

# Menu
print("\n--BIENVENIDO AL SISTEMA DE GESTION--")
while True:
    print("--------------------------------------------")
    print("Menus:\n\t1.Registrar Cliente\n\t2.Visualizar Clientes\n\t3.Buscar Cliente\n\t4.Realizar un"
          ," Pedido\n\t5.Mandar seguimiento de un pedido\n\t6.Salir del programa", sep="")
    print("--------------------------------------------")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        registro_cliente(lista_clientes)
    elif opcion == "2":
        visualizar_clientes(lista_clientes)
    elif opcion == "3":
        dni_buscar = input("Introduce el DNI del cliente a buscar: ")
        cliente_buscado = buscar_cliente(dni_buscar,lista_clientes)
        if cliente_buscado != False:
            print("Los datos del usuario son:")
            imprimir_cliente(cliente_buscado)
        else:
            print("No existe ningun usuario con ese DNI.")

    elif opcion == "4":
        realizar_compra(lista_clientes, lista_productos, lista_pedidos)
    elif opcion == "5":
        visualizar_pedidos(lista_pedidos)
        num_pedido = input("¿De que pedido quieres mandar los datos por SMS y por Mail?\nIntroduce su numero de seguimiento: ")
        pedido_buscado = buscar_pedido(num_pedido, lista_pedidos)
        if pedido_buscado != False:
            print("Se han enviado los datos al numero: ", pedido_buscado["cliente"]["datos_fiscales"]["telefono_fiscal"],
                   " y al mail: ", pedido_buscado["cliente"]["datos_fiscales"]["mail_fiscal"], sep="")
        else:
            print("No existe ningun pedido con ese numero de seguimiento.")
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Introduce una opcion valida.\n")




