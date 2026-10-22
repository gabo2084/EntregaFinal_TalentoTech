
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
    print(f'{'_' * 100}')

    if not stock:
        print('No existen productos cargados en el sistema.')
    else:
        for producto in stock:
            for clave, valor in producto.items():
                print(f'{clave}: {valor}')
            print(f'{'_' * 100}')







