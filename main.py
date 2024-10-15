from UTN_Heroes_Dataset.utn_pp import get_original_matrix

from app_modulos.app_main import app_garages


matriz_garage = get_original_matrix()


app_garages(matriz_garage)




if __name__ == '__main__':
    get_original_matrix()
    app_garages()

