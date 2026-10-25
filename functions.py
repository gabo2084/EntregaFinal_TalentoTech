
stock = [
    {
        "Id": 1,
        "Nombre": "Notebook Lenovo IdeaPad 3",
        "Descripcion": "Notebook con procesador Intel Core i5, 8GB RAM y SSD de 512GB.",
        "Cantidad": 12,
        "Precio": 850000,
        "Categoria": "Notebooks"
    },
    {
        "Id": 2,
        "Nombre": "Mouse Logitech G203",
        "Descripcion": "Mouse gamer óptico RGB de 8000 DPI.",
        "Cantidad": 35,
        "Precio": 28000,
        "Categoria": "Periféricos"
    },
    {
        "Id": 3,
        "Nombre": "Teclado Redragon Kumara",
        "Descripcion": "Teclado mecánico con switches Outemu Blue.",
        "Cantidad": 20,
        "Precio": 55000,
        "Categoria": "Periféricos"
    },
    {
        "Id": 4,
        "Nombre": "Monitor Samsung 24 pulgadas",
        "Descripcion": "Monitor Full HD de 75Hz con panel IPS.",
        "Cantidad": 8,
        "Precio": 210000,
        "Categoria": "Monitores"
    },
    {
        "Id": 5,
        "Nombre": "Disco SSD Kingston 480GB",
        "Descripcion": "Unidad de estado sólido SATA III de 480GB.",
        "Cantidad": 25,
        "Precio": 45000,
        "Categoria": "Almacenamiento"
    },
    {
        "Id": 6,
        "Nombre": "Memoria RAM Corsair 16GB DDR4",
        "Descripcion": "Módulo de memoria de 3200MHz.",
        "Cantidad": 18,
        "Precio": 70000,
        "Categoria": "Componentes"
    },
    {
        "Id": 7,
        "Nombre": "Placa de Video RTX 4060",
        "Descripcion": "Tarjeta gráfica NVIDIA de 8GB GDDR6.",
        "Cantidad": 5,
        "Precio": 650000,
        "Categoria": "Componentes"
    },
    {
        "Id": 8,
        "Nombre": "Impresora HP DeskJet 2775",
        "Descripcion": "Impresora multifunción con conectividad WiFi.",
        "Cantidad": 10,
        "Precio": 120000,
        "Categoria": "Impresoras"
    },
    {
        "Id": 9,
        "Nombre": "Router TP-Link Archer C6",
        "Descripcion": "Router WiFi de doble banda AC1200.",
        "Cantidad": 15,
        "Precio": 75000,
        "Categoria": "Redes"
    },
    {
        "Id": 10,
        "Nombre": "Auriculares HyperX Cloud Stinger",
        "Descripcion": "Auriculares gamer con micrófono integrado.",
        "Cantidad": 14,
        "Precio": 65000,
        "Categoria": "Audio"
    },
    {
        "Id": 11,
        "Nombre": "Webcam Logitech C920",
        "Descripcion": "Webcam Full HD 1080p para videoconferencias.",
        "Cantidad": 7,
        "Precio": 98000,
        "Categoria": "Periféricos"
    },
    {
        "Id": 12,
        "Nombre": "Disco Externo Seagate 1TB",
        "Descripcion": "Disco rígido portátil USB 3.0.",
        "Cantidad": 11,
        "Precio": 89000,
        "Categoria": "Almacenamiento"
    },
    {
        "Id": 13,
        "Nombre": "Fuente Corsair 650W",
        "Descripcion": "Fuente de alimentación certificada 80 Plus Bronze.",
        "Cantidad": 9,
        "Precio": 105000,
        "Categoria": "Componentes"
    },
    {
        "Id": 14,
        "Nombre": "Gabinete Aerocool Bolt",
        "Descripcion": "Gabinete ATX con panel lateral transparente.",
        "Cantidad": 6,
        "Precio": 82000,
        "Categoria": "Componentes"
    },
    {
        "Id": 15,
        "Nombre": "Switch TP-Link 8 Puertos",
        "Descripcion": "Switch de red Gigabit Ethernet.",
        "Cantidad": 13,
        "Precio": 42000,
        "Categoria": "Redes"
    },
    {
        "Id": 16,
        "Nombre": "Notebook HP 250 G9",
        "Descripcion": "Notebook con Intel Core i3, 8GB RAM y SSD de 256GB.",
        "Cantidad": 10,
        "Precio": 720000,
        "Categoria": "Notebooks"
    },
    {
        "Id": 17,
        "Nombre": "Pendrive SanDisk 64GB",
        "Descripcion": "Memoria USB 3.0 de alta velocidad.",
        "Cantidad": 40,
        "Precio": 12000,
        "Categoria": "Almacenamiento"
    },
    {
        "Id": 18,
        "Nombre": "UPS APC 1200VA",
        "Descripcion": "Sistema de alimentación ininterrumpida para PC.",
        "Cantidad": 4,
        "Precio": 190000,
        "Categoria": "Energía"
    }
]

producto = {}

def cabecera(titulo, simbolo):

    longitud_titulo = len(titulo)
    
    if longitud_titulo % 2 == 0:

        lineas_extremas = simbolo * 100
        linea_titulo = f'{simbolo * ((99 - longitud_titulo)//2)} {titulo} {simbolo * ((99 - longitud_titulo)//2)}'
        lineas_extremas

    else:

        lineas_extremas = simbolo * 101
        linea_titulo = f'{simbolo * ((100 - longitud_titulo)//2)} {titulo} {simbolo * ((100 - longitud_titulo)//2)}'
        lineas_extremas

    print(f'\n{lineas_extremas}')
    print(linea_titulo)
    print(f'{lineas_extremas}\n')


def pantalla_principal():

    cabecera('Sistema de Gestion de Productos', '+')

    print('''
        1. Agregar producto
        2. Mostrar productos
        3. Actualizar producto
        4. Eliminar producto
        5. Buscar producto
        6. Reporte de productos
        0. Salir
        ''')
    
    opcion = input('\nIngrese la opcion a ejecutar(1|2|3|4|5|6|0): ')

    return opcion


def pantalla_claves_producto(titulo, simbolo):

    cabecera(titulo, simbolo)

    print('''
        1. Nombre
        2. Descripcion
        3. Cantidad
        4. Precio
        5. Categoria
        0. Salir
    ''')

    opcion = input('\nIngrese su opcion(1|2|3|4|5|0): ')

    if opcion in ('1', '2', '3', '4', '5', '0'):

        return opcion
    
    else:

        print('\nOpcion no valida.')
        return '0'


def ingresar_dato(dato_clave):

    dato_verificado = False

    while dato_verificado == False:

        if dato_clave.lower() in ('id', 'cantidad', 'precio'):

            dato_valor = input(f'\nIngresar {dato_clave.upper()} del producto: ').strip()
            
            if not dato_valor or not dato_valor.isnumeric() or int(dato_valor) <= 0:

                print(f'\nEl campo no puede estar vacio, debe ser un numero y mayor a cero.')
                continue
    
            dato_verificado = True
    
            return dato_valor
        
        elif dato_clave.lower() in ('nombre', 'categoria', 'descripcion'):

            dato_valor = input(f'\nIngresar {dato_clave.upper()} del producto: ').strip()

            if not dato_valor or dato_valor.isnumeric():

                print(f'\nEl campo no debe estar vacio o no ser un numero.')
                continue

            dato_verificado = True

            return dato_valor


def solicitud_datos(titulo, simbolo):

    cabecera(titulo, simbolo)
    menu_claves_producto()
    opcion = input('\nIngrese su opcion(1|2|3|4|5|0): ')
    return opcion


def vista_producto(producto):
    
    for clave, valor in producto.items():

        if clave == 'Precio':
            print(f'\n{clave}: $ {valor}')
        else:
            print(f'\n{clave}: {valor}')

    print(f'{'_' * 100}')


def buscar_datos(clave, valor):

    resultados = []

    for producto in stock:

        if valor.lower() in producto[clave].lower():

            resultados.append(producto)

    return resultados


# Funciones que se usan en la pantalla principal

def agregar_producto():

    cabecera('Agregar Producto', '+')

    producto = {
        'Id': int(ingresar_dato('id')),
        'Nombre': ingresar_dato('nombre'),
        'Descripcion': ingresar_dato('descripcion'),
        'Cantidad': int(ingresar_dato('cantidad')),
        'Precio': float(ingresar_dato('precio')),
        'Categoria': ingresar_dato('categoria')
        }

    stock.append(producto)

    cabecera('Producto Agregado', '+')

    vista_producto(producto)


def mostrar_productos(listado_productos=stock):

    cabecera('Productos en Stock', '+')

    if not listado_productos:
        print('No existen productos cargados en el sistema.')
    else:
        for producto in listado_productos:
            vista_producto(producto)


def actualizar_producto():

    cabecera('Actualizar Producto', '+')

    id = input('\nIngrese el ID del producto a actualizar: ')

    if id.isnumeric():

        for producto in stock:

            if producto.get('Id') == int(id):

                print('\nProducto encontrado.')
                print(f'{'_' * 100}')
                vista_producto(producto)

                desea_salir = False

                while desea_salir == False:
                
                    opcion = pantalla_claves_producto(f'Actualizacion de Producto: {producto['Nombre']}', '+')
                    
                    if not opcion.isnumeric():
                        break

                    match opcion:
                        case '0':
                            print('\nVolviendo al menu principal ...')
                            break
                        case '1':
                            nombre = ingresar_dato('nombre')
                            producto['Nombre'] = nombre
                        case '2':
                            descripcion = ingresar_dato('descripcion')
                            producto['Descripcion'] = descripcion
                        case '3':
                            cantidad = ingresar_dato('cantidad')
                            producto['Cantidad'] = cantidad                
                        case '4':
                            precio = ingresar_dato('precio')
                            producto['Precio'] = precio
                        case '5':
                            categoria = ingresar_dato('categoria')
                            producto['Categoria'] = categoria
                        case _:
                            print('\nProducto no encontrado.')

                    print('\nProducto actualizado correctamente.')
                
                return True

            else:

                print('\nID no encontrado. Volviendo al menu principal...')
                return False
    
    else:

        print('\nEl valor ingresado no es numerico. Volviendo al menu principal...')
        return False


def eliminar_producto():

    cabecera('Eliminar Producto', '+')
    print('Pendiente de desarrollo...')


def buscar_productos():

    desea_salir = False
    
    while desea_salir == False:
    
        opcion = pantalla_claves_producto('Busqueda de Producto', '+')

        match opcion:
            case '0':
                print('\nVolviendo al menu principal ...')
                break
            case '1':
                clave = 'Nombre'
            case '2':
                clave = 'Descripcion'
            case '3':
                clave = 'Cantidad'                
            case '4':
                clave = 'Precio'
            case '5':
                clave = 'Categoria'

        valor = input(f'\nIngrese {clave.upper()} a buscar: ')

        productos_encontrados = buscar_datos(clave, valor)

        mostrar_productos(productos_encontrados)


def reporte_productos():

    cabecera('Reporte de Productos', '+')
    print('Pendiente de desarrollo...')











    




