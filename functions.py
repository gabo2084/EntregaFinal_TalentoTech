
stock = []
producto = {}

def cabecera(titulo, simbolo):
    longitud_titulo = len(titulo)
    if longitud_titulo % 2 == 0:
        lineas_extremas = simbolo * 100
        linea_titulo = f'{simbolo * ((99 - longitud_titulo)//2)} {titulo} {simbolo * ((99 - longitud_titulo)//2)}'
        lineas_extremas = simbolo * 100
    else:
        lineas_extremas = simbolo * 101
        linea_titulo = f'{simbolo * ((100 - longitud_titulo)//2)} {titulo} {simbolo * ((100 - longitud_titulo)//2)}'
        lineas_extremas = simbolo * 101

    print(f'\n{lineas_extremas}')
    print(linea_titulo)
    print(f'{lineas_extremas}\n')

def menu_opciones():
    print('1. Agregar producto')
    print('2. Mostrar productos')
    print('3. Actualizar producto')
    print('4. Eliminar producto')
    print('5. Buscar producto')
    print('6. Reporte de productos')
    print('0. Salir')


def pantalla_principal(titulo, simbolo):
    cabecera(titulo, simbolo)
    menu_opciones()


def ingresar_id():
    
    id_verificado = False

    while id_verificado == False:
    
        verificar_id = input('\nIngrese el ID del producto: ').strip()

        if not verificar_id or not verificar_id.isnumeric() or int(verificar_id) <= 0:
            print('\nEl Id no puede estar vacio. Debe ser un numero y mayor a cero.')
            continue

        id_verificado = True

        return verificar_id


def ingresar_nombre():

    nombre_verificado = False

    while nombre_verificado == False:

        verificar_nombre = input('\nIngrese el nombre del producto: ').strip().title()

        if not verificar_nombre or verificar_nombre.isnumeric():
            print('\nEl nombre no debe estar vacio o no ser un numero.')
            continue

        nombre_verificado = True

        return verificar_nombre


def ingresar_descripcion():

    descripcion_verificada = False

    while descripcion_verificada == False:

        verificar_descripcion = input('\nIngrese la descripcion del producto: ').strip().capitalize()

        if not verificar_descripcion or verificar_descripcion.isnumeric():
            print('\nLa descripcion no debe estar vacia o ser un numero.')
            continue

        descripcion_verificada = True

        return verificar_descripcion


def ingresar_cantidad():

    cantidad_verificada = False

    while cantidad_verificada == False:

        verificar_cantidad = input('\nIngrese la cantidad del producto: ').strip()

        if not verificar_cantidad or not verificar_cantidad.isnumeric() or int(verificar_cantidad) <= 0:
            print('\nLa cantidad no tiene que estar vacia. Debe ser un numero y mayor a cero.')
            continue

        cantidad_verificada = True

        return int(verificar_cantidad)


def ingresar_precio():

    precio_verificado = False

    while precio_verificado == False:

        verificar_precio = input('\nIngrese el precio del producto: ').strip()

        if not verificar_precio or not verificar_precio.isnumeric() or int(verificar_precio) <= 0:
            print('\nEl precio no tiene que estar vacio. Debe ser un numero y mayor a cero.')
            continue

        precio_verificado = True

        return float(verificar_precio)


def ingresar_categoria():

    categoria_verificada = False

    while categoria_verificada == False:

        verificar_categoria = input('\nIngrese la categoria del producto: ').strip().title()

        if not verificar_categoria or verificar_categoria.isnumeric():
            print('\nLa categoria no debe estar vacia o no ser un numero.')
            continue

        categoria_verificada = True

        return verificar_categoria


def agregar_producto(titulo, simbolo):

    cabecera(titulo, simbolo)

    producto = {
        'Id': ingresar_id(),
        'Nombre': ingresar_nombre(),
        'Descripcion': ingresar_descripcion(),
        'Cantidad': ingresar_cantidad(),
        'Precio': ingresar_precio(),
        'Categoria': ingresar_categoria()
        }

    print(producto)

    stock.append(producto)


def mostrar_productos(titulo, simbolo):

    cabecera(titulo, simbolo)

    for producto in stock:
        for clave, valor in producto.items():
            print(f'{clave}: {valor}')





