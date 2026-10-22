import functions as fun

desea_salir = False

opcion = ''

while desea_salir == False:
    
    fun.pantalla_principal('Sistema de Gestion de Productos', '+')

    opcion = input('\nIngrese la opcion a ejecutar(1|2|3|4|5|6|0): ')

    match opcion:
        case '0':
            print('\nSaliendo del sistema ...')
            break
        case '1':
            fun.agregar_producto()
        case '2':
            fun.mostrar_productos()
        case '3':
            fun.actualizar_producto()
        case _:
            print('\nNo existe la opcion ingresada.')
    


