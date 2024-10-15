from UTN_Heroes_Dataset.utn_pp import get_original_matrix

from UTN_Heroes_Dataset.utn_pp import (mostrar_matriz_texto_tabla, clear_console ,color_text)

from .funciones import (cagar_existencias , cantidad_total_fila, garage_con_menor_unidades,garage_con_max_cantidad,
                        obtener_recaudacion,garages_con_mas_de)

from .auxiliares import mostrar_menu, validar_opcion

matriz_garage = get_original_matrix()

def app_garages (matriz:list[list]):
    '''Esta funcion se encarga de generar una app
    que carga opciones y en base a ello genere 
    distintas acciones

    recibe una matriz

    No retorna nada
    '''

    while True:
        mostrar_menu()
        opcion = validar_opcion(1,9)

        match(opcion):
            case(1):
                cagar_existencias(matriz)
            case(2):
                cantidad_total_fila(matriz,2)
            case(3):
                garage_con_menor_unidades(matriz,2)
            case(4):
                garage_con_max_cantidad(matriz,2)
            case(5):
                obtener_recaudacion(matriz)
            case(6):
                garages_con_mas_de(matriz,2,6)
            case(7):
                pass
            case(8):
                pass
            case(9):
                break
        clear_console()
        