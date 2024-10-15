def mostrar_menu ():
    '''Esta funcion muestra un mensaje en pantalla con diferentes opciones
    '''
    mensaje = ''' Elija una opción
    
1.Obtener existencias: para ello deberá crear una función que cargue la existencia de cada vehículo en todos los garajes y mostrarlos.

2.Calcular por cada garaje la cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria.

3.Datos completos del garaje que almacena menos unidades de vehículos.

4.Máxima cantidad de unidades almacenadas entre todos los garajes.

5.Obtener recaudación: para ello deberás crear una función que calcule la recaudación de cada garaje, teniendo en cuenta 
  su precio unitario y cantidad de unidades almacenadas en cada garaje.

6.Cantidad de garajes que hayan almacenado 6 o más unidades de vehículos.

7.Porcentaje de unidades de cada marca de vehículo sobre el total de vehículos almacenados entre todos los garajes de la sede matriz. 
  Además mostrar todos los datos del garaje con el máximo porcentaje de vehículos almacenados.

8.Generar un informe con la recaudación de cada garaje, ordenada de mayor a menor.

9.Salir


'''
    print(mensaje)



def validar_opcion(min:int , max:int)->int:
    '''Esta funcion se encarga de validar una opcion,
    caso de un ingreso incorrecto, volverá a pedir nuevamente 
    dicha opcion hasta que sea un ingreso valido.

    Como parámetros recibe 2 números (uno minimo y otro maximo)

    Retorna un numero entero como opcion

    '''

    opcion = input(f'Ingrese un numero entre {min} y {max} inclusive: ')
    

    while not opcion.isdigit() or min > int(opcion) or max < int(opcion):
        mensaje_error = 'Error - el valor ingresado no es valido'
        print(mensaje_error)
        opcion = input(f'Re-Ingrese un numero entre {min} y {max} inclusive: ')

    resultado = int (opcion)
    
    return resultado





def cargar_lista_indices (matriz:list[list])->list[list]:
    '''Esta funcion carga una lista de indices 
    como elemento final de la matriz

    recibe como parametro una matriz 

    retorna la matriz modificada
    '''
    cantidad_de_columnas = len(matriz[0])

    lista_indices = []

    for i in range (cantidad_de_columnas):
        indice_encontrado = i 

        lista_indices.append(indice_encontrado)

    matriz.append(lista_indices)

    return matriz


def sumar_total_fila (matriz:list[list],indice_fila:int)->float:
    '''Esta funcion suma una fila correspondiente y arroja
    un resultado

    Recibe como parametro una matriz(list[list]), y un indice de la fila(int)

    Retorna un resultado correspondiente a la operacion (float)
    '''

    resultado = 0

    for dato in matriz[indice_fila]:
        resultado += dato

    return resultado
