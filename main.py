import functions as fun

desea_salir = False

opcion = ''

while desea_salir == False:
    
    fun.pantalla_principal('Sistema de Gestion de Productos', '+')

    opcion = input('\nIngrese la opcion a ejecutar: ')

    match opcion:
        case '0':
            print('\nSaliendo del sistema ...')
            break
        case '1':
            fun.agregar_producto('Agregar Producto', '+')
        case '2':
            fun.mostrar_productos('Mostrar Productos', '+')
        case '3':
            
        case _:
            print('\nNo existe la opcion ingresada.')
    


