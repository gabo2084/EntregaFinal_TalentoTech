from colorama import init, Fore, Back, Style
from tabulate import tabulate

init(autoreset=True)

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
    }
]

producto = {}

def cabecera(titulo, simbolo):

    longitud_titulo = len(titulo)
    
    if longitud_titulo % 2 == 0:

        lineas_extremas = simbolo * 150
        linea_titulo = f'{simbolo * ((149 - longitud_titulo)//2)} {titulo} {simbolo * ((149 - longitud_titulo)//2)}'
        lineas_extremas

    else:
        
        lineas_extremas = simbolo * 151
        linea_titulo = f'{simbolo * ((150 - longitud_titulo)//2)} {titulo} {simbolo * ((150 - longitud_titulo)//2)}'
        lineas_extremas

    print()
    print(Back.LIGHTBLUE_EX + Fore.WHITE + f'{lineas_extremas}')
    print(Back.LIGHTBLUE_EX + Fore.WHITE + linea_titulo)
    print(Back.LIGHTBLUE_EX + Fore.WHITE + f'{lineas_extremas}')


def pantalla_principal():

    cabecera('Sistema de Gestion de Productos', ' ')

    print(Fore.LIGHTYELLOW_EX + '''
        1. Agregar producto
        2. Mostrar productos
        3. Actualizar producto
        4. Eliminar producto
        5. Buscar producto
        6. Reporte de productos
        0. Salir
        ''')
    
    opcion = input(Fore.LIGHTGREEN_EX + 'Ingrese la opcion a ejecutar(1|2|3|4|5|6|0): ')

    return opcion


def pantalla_claves_producto(titulo, simbolo):

    cabecera(titulo, simbolo)

    opcion_valida = False

    while opcion_valida == False:
        print(Fore.LIGHTYELLOW_EX + ''''
        1. Id
        2. Nombre
        3. Descripcion
        4. Cantidad
        5. Precio
        6. Categoria
        0. Salir
        ''')
        
        opcion = input(Fore.LIGHTGREEN_EX + 'Ingrese la opcion a ejecutar(1|2|3|4|5|6|0): ')

        if opcion in ('1', '2', '3', '4', '5', '6', '0'):
            opcion_valida = True
            return opcion
    
        else:

            print(Fore.LIGHTRED_EX + '\nOpcion no valida.')
            continue


def solicitud_datos(titulo, simbolo):

    cabecera(titulo, simbolo)
    pantalla_claves_producto()
    opcion = input(Fore.LIGHTGREEN_EX + '\nIngrese su opcion(1|2|3|4|5|0): ')
    return opcion


def ingresar_dato(dato_clave):

    dato_verificado = False

    while dato_verificado == False:

        if dato_clave.lower() in ('id', 'cantidad', 'precio'):

            dato_valor = input(Fore.LIGHTGREEN_EX + f'\nIngresar {dato_clave.upper()} del producto: ').strip()
            
            if not dato_valor or not dato_valor.isnumeric() or int(dato_valor) <= 0:

                print(Fore.LIGHTRED_EX + f'\nEl campo no puede estar vacio, debe ser un numero y mayor a cero.')
                continue
    
            dato_verificado = True
    
            return dato_valor
        
        elif dato_clave.lower() in ('nombre', 'categoria', 'descripcion'):

            dato_valor = input(Fore.LIGHTGREEN_EX + f'\nIngresar {dato_clave.upper()} del producto: ').strip()

            if not dato_valor or dato_valor.isnumeric():

                print(Fore.LIGHTRED_EX + f'\nEl campo no debe estar vacio o no ser un numero.')
                continue

            dato_verificado = True

            return dato_valor
        

def buscar_producto_por_id():

    id = ingresar_dato('Id')

    for producto in stock:

        if producto.get('Id') == int(id):

            return producto


def buscar_datos(clave, valor):

    resultados = []

    for producto in stock:

        if str(valor).lower() in str(producto[clave]).lower():

            resultados.append(producto)

    return resultados


# Funciones que se usan en la pantalla principal

def agregar_producto():

    cabecera('Agregar Producto', ' ')

    producto = {
        'Id': int(ingresar_dato('id')),
        'Nombre': ingresar_dato('nombre'),
        'Descripcion': ingresar_dato('descripcion'),
        'Cantidad': int(ingresar_dato('cantidad')),
        'Precio': float(ingresar_dato('precio')),
        'Categoria': ingresar_dato('categoria')
        }

    stock.append(producto)

    cabecera('Producto Agregado', ' ')

    mostrar_productos([producto])


def mostrar_productos(lista_productos=stock):

    if not lista_productos:
        print(Fore.LIGHTRED_EX + f'\nNo existen productos cargados en el sistema.')
    else:
        print(tabulate(lista_productos, headers="keys", tablefmt="fancy_grid"))


def actualizar_producto():

    cabecera('Actualizar Producto', ' ')

    producto = buscar_producto_por_id()

    if not producto:
        
        print(Fore.LIGHTRED_EX + f'\nNo se encontro el producto con el ID ingresado. Volviendo al menu principal ...')
        return False
    
    else:

        print(Fore.LIGHTGREEN_EX + f'\nProducto Encontrado')
        mostrar_productos([producto])

        desea_salir = False

        while desea_salir == False:
        
            opcion = pantalla_claves_producto(f'Actualizacion de Producto: {producto['Nombre']}', ' ')
            
            if not opcion.isnumeric():
                break

            match opcion:
                case '0':
                    print(Fore.LIGHTRED_EX + f'\nVolviendo al menu principal ...')
                    break
                case '1':
                    id = ingresar_dato('id')
                    producto['Id'] = id
                case '2':
                    nombre = ingresar_dato('nombre')
                    producto['Nombre'] = nombre
                case '3':
                    descripcion = ingresar_dato('descripcion')
                    producto['Descripcion'] = descripcion
                case '4':
                    cantidad = ingresar_dato('cantidad')
                    producto['Cantidad'] = cantidad                
                case '5':
                    precio = ingresar_dato('precio')
                    producto['Precio'] = precio
                case '6':
                    categoria = ingresar_dato('categoria')
                    producto['Categoria'] = categoria

            print(Fore.LIGHTGREEN_EX + f'\nProducto actualizado correctamente.')
        
        return True


def eliminar_producto():

    cabecera('Eliminar Producto', ' ')

    producto = buscar_producto_por_id()

    if not producto:
        print(Fore.LIGHTRED_EX + f'\nNo se encontro el producto con el ID ingresado. Volviendo al menu principal ...')
        return False
    else:
        print(Fore.LIGHTGREEN_EX + '\nProducto encontrado.')
        mostrar_productos([producto])
        confirmacion = input(Fore.LIGHTRED_EX + '\nDesea eliminar este producto? (S/N): ').strip().lower()

        if confirmacion != 's':
            print(Fore.LIGHTRED_EX + '\nOperacion cancelada. Volviendo al menu principal ...')
            return False
        else:        
            stock.remove(producto)
            print(Fore.LIGHTGREEN_EX + f'\nProducto eliminado correctamente: {producto["Nombre"]}')
            return True


def buscar_productos():

    desea_salir = False
    
    while desea_salir == False:
    
        opcion = pantalla_claves_producto('Busqueda de Producto', ' ')

        match opcion:
            case '0':
                print(Fore.LIGHTRED_EX + f'\nVolviendo al menu principal ...')
                break
            case '1':
                clave = 'Id'
            case '2':
                clave = 'Nombre'
            case '3':
                clave = 'Descripcion'
            case '4':
                clave = 'Cantidad'                
            case '5':
                clave = 'Precio'
            case '6':
                clave = 'Categoria'

        valor = input(Fore.LIGHTGREEN_EX + f'\nIngrese {clave.upper()} a buscar: ')

        productos_encontrados = buscar_datos(clave, valor)

        mostrar_productos(productos_encontrados)


def reporte_productos():

    cabecera('Reporte de Stock', ' ')

    if not stock:

        print(Fore.LIGHTRED_EX + f'\nNo existen productos cargados en el sistema.')
        return False

    stock_minimo = ingresar_dato('cantidad')

    print(Fore.LIGHTGREEN_EX + f'\nProductos con stock menor o igual a {stock_minimo}')

    encontrado = False

    productos_encontrados = []

    for producto in stock:        

        if producto['Cantidad'] <= int(stock_minimo):        
            productos_encontrados.append(producto)
            encontrado = True

    mostrar_productos(productos_encontrados)

    if not encontrado:
        print(Fore.LIGHTRED_EX + f'No se encontraron productos con stock menor o igual a {stock_minimo}.')


    




