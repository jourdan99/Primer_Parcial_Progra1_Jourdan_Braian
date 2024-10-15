from UTN_Heroes_Dataset.utn_pp import get_original_matrix

from UTN_Heroes_Dataset.utn_pp import (mostrar_matriz_texto_tabla, clear_console ,color_text)

from app_modulos import *


martriz_concesionaria = get_original_matrix()



def mostrar_prueba(matriz):
    for fila in range (len(matriz)):
        for columna in range (len(matriz[fila])):
            print(matriz[fila][columna] , end = '|')
        print('')





def cargar_lista_indices (matriz:list[list])->list[list]:
    '''Esta funcion carga una lista de indices 
    como elemento final de la matriz

    recibe como parametro una matriz 

    retorna la matriz modificada
    '''
    cantidad_de_columnas = len(matriz[0])

    lista_indices = []

    for i in range (cantidad_de_columnas):
        indice_encontrado = i + 1

        lista_indices.append(indice_encontrado)

    matriz.append(lista_indices)

    return matriz



#testing = cargar_lista_indices(martriz_concesionaria)


#mostrar_prueba(testing)

# mostrar_matriz_texto_tabla (martriz_concesionaria,)


# calculo = len(martriz_concesionaria[0])

# print(calculo)

# def cagar_existencias (matriz:list[list]):
#     '''
#     '''
#     cantidad_columnas = len(matriz[0])
#     indice_cantidad = 2 
#     indice_precio = 3
#     indice_ganancia = 4 

#     if(cantidad_columnas == 20):
#         for indice in range (20):

#             ganacias_calculadas = matriz[indice_cantidad][indice] * matriz[indice_precio][indice]
#             matriz[indice_ganancia][indice] = ganacias_calculadas

#     cargar_lista_indices(matriz)

#     return matriz



# testing = cagar_existencias(martriz_concesionaria)

# mostrar_prueba(testing)



def cargar_nueva_matriz (matriz:list[list]):
    '''
    '''


    nueva_matriz = [[],[],[]]







print(nueva_matriz)