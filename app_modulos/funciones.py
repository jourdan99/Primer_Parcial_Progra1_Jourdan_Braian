from UTN_Heroes_Dataset.utn_pp import (get_original_matrix)

from .auxiliares import cargar_lista_indices, sumar_total_fila


martriz_concesionaria = get_original_matrix()

#punto 1 
def cagar_existencias (matriz:list[list]):
    '''
    '''
    

    cargar_lista_indices(matriz)

    return matriz





#punto 2
def cantidad_total_fila(matriz,fila):
    '''
    '''
    resultado = sumar_total_fila(matriz,fila)

    mensaje = f'La cantidad total de unidades almacenadas entre todos los vehiculos es de: {resultado}'

    print(mensaje)



#punto 3 

def garage_con_menor_unidades (matriz,fila):
    '''
    '''
    indice_con_menor_unidad = None

    for indice in range (len(matriz[fila])):
        if indice_con_menor_unidad == None or matriz[fila][indice] < matriz [fila][indice_con_menor_unidad]:
            indice_con_menor_unidad = indice

    garage = indice_con_menor_unidad + 1
    marca = matriz[0][indice_con_menor_unidad]
    modelo = matriz[1][indice_con_menor_unidad]
    cantidad = matriz[2][indice_con_menor_unidad]
    precio = matriz[3][indice_con_menor_unidad]
    ganancias = matriz[4][indice_con_menor_unidad]

    mensaje = f'el garage con menos unidades ({cantidad}) es el Numero {garage} que corresponde a:\n'\
            f'Marca: {marca}\nModelo: {modelo}'
    
    print(mensaje)
    


#punto 4
def garage_con_max_cantidad(matriz,fila):
    '''
    '''
    indice_con_mayor_unidad = None

    for indice in range (len(matriz[fila])):
        if indice_con_mayor_unidad == None or matriz[fila][indice] > matriz [fila][indice_con_mayor_unidad]:
            indice_con_mayor_unidad = indice

    garage = indice_con_mayor_unidad + 1
    marca = matriz[0][indice_con_mayor_unidad]
    modelo = matriz[1][indice_con_mayor_unidad]
    cantidad = matriz[2][indice_con_mayor_unidad]
    precio = matriz[3][indice_con_mayor_unidad]
    ganancias = matriz[4][indice_con_mayor_unidad]

    mensaje = f'el garage con mas unidades ({cantidad}) es el Numero {garage} que corresponde a:\n'\
            f'Marca: {marca}\nModelo: {modelo}'
    
    print(mensaje)


#punto 5

def obtener_recaudacion(matriz):
    '''
    '''
    
    indice_cantidad = 2 
    indice_precio = 3
    indice_ganancia = 4 

    
    for indice in range (20):

        ganacias_calculadas = matriz[indice_cantidad][indice] * matriz[indice_precio][indice]
        matriz[indice_ganancia][indice] = ganacias_calculadas

    return matriz
    

#punto 6
def garages_con_mas_de(matriz:int,fila:int , mas_de:int):
    '''
    '''
    garages_encontrados = 0 
    
    cantidad_de_columnas = len(matriz[0])
    for indice in range (cantidad_de_columnas):

        dato_encontrado = matriz[fila][indice]
        if dato_encontrado >= mas_de:
            garages_encontrados += 1


    mensaje =f'Son {garages_encontrados} los garages encontrados que tienen mas de {mas_de} unidades de vehiculos'
    print(mensaje)





#punto 7
def porcentaje_por_marca():
    ''''''

    
#punto 8 

def informe_recaudacion_garage():
    ''''''