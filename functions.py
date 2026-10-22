
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


def menu_opciones():

    print('''
        1. Agregar producto
        2. Mostrar productos
        3. Actualizar producto
        4. Eliminar producto
        5. Buscar producto
        6. Reporte de productos
        0. Salir
    ''')

def menu_busqueda():

    print('''
        1. Nombre
        2. Descripcion
        3. Cantidad
        4. Precio
        5. Categoria
        0. Terminar
    ''')


def pantalla_principal(titulo, simbolo):
    cabecera(titulo, simbolo)
    menu_opciones()


def ingresar_dato(dato_clave):

    dato_verificado = False

    while dato_verificado == False:

        if dato_clave.lower() in ('id', 'cantidad', 'precio'):

            dato_valor = input(f'\nIngresar {dato_clave.upper()} del producto: ').strip()
            
            if not dato_valor or not dato_valor.isnumeric() or int(dato_valor) <= 0:

                print(f'\n{dato_valor} no puede estar vacio. Debe ser un numero y mayor a cero.')
                continue
    
            dato_verificado = True
    
            return dato_valor
        
        elif dato_clave.lower() in ('nombre', 'categoria', 'descripcion'):

            dato_valor = input(f'\nIngresar {dato_clave.upper()} del producto: ').strip().title()

            if not dato_valor or dato_valor.isnumeric():

                print(f'\n{dato_valor} no debe estar vacio o no ser un numero.')
                continue

            dato_verificado = True

            return dato_valor


def vista_producto(producto):
    
    for clave, valor in producto.items():

        if clave == 'Precio':
            print(f'\n{clave}: $ {valor}')
        else:
            print(f'\n{clave}: {valor}')

    print(f'{'_' * 100}')


def solicitar_clave_valor():

    criterio = input('Buscar por (id/nombre/categoria): ')

    match criterio:
        case 'id':
            valor = input('Ingrese el ID: ')
        case 'nombre':
            valor = input('Ingrese el nombre del producto: ')
        case 'categoria':
            valor = input('Ingrese la categoria del producto')



def buscar_producto(clave, valor):

    for producto in stock:

        if producto.get(clave) == valor:
            return producto

    return None


def agregar_producto():

    cabecera('Agregar Producto', '+')

    producto = {
        'Id': ingresar_dato('id'),
        'Nombre': ingresar_dato('nombre'),
        'Descripcion': ingresar_dato('descripcion').capitalize(),
        'Cantidad': ingresar_dato('cantidad'),
        'Precio': ingresar_dato('precio'),
        'Categoria': ingresar_dato('categoria')
        }

    stock.append(producto)

    cabecera('Producto Agregado', '+')

    vista_producto(producto)


def mostrar_productos():

    cabecera('Mostrar Productos', '+')

    if not stock:
        print('No existen productos cargados en el sistema.')
    else:
        for producto in stock:
            vista_producto(producto)


def actualizar_producto():

    cabecera('Actualizar Producto', '+')

    menu_busqueda()




    




