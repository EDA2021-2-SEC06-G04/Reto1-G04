"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import sys

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente artistas")
    print("3- Listar cronológicamente adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar obras por la nacionalidad de los artistas")
    print("6- Transportar las obras de un departamento")
    print("7- Crear una nueva exposición")
    print("0- Salir")


def initCatalog(estrucutra):
    """
    Inicializa el catalogo de obras
    """
    return controller.initCatalog(estrucutra)

def loadData(catalog):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        estrucutra = input('Escoja el tipo de estructura de datos escribiendo "ARRAY_LIST" o "SINGLE_LINKED": ')
        while (estrucutra != "ARRAY_LIST") and (estrucutra != "SINGLE_LINKED"):
            estructura = input('Escoja un tipo de estructura de datos válido escribiendo "ARRAY_LIST" o "SINGLE_LINKED": ')
        print("Cargando información de los archivos ....")
        catalog = initCatalog(estrucutra)
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['obras'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artistas'])))
        print('Últimos 3 elementos de obras:')
        tresobras = lt.subList(catalog['obras'],lt.size(catalog['obras'])-2,3)
        print(tresobras)
        print('Últimos 3 elementos de artistas:')
        tresartistas = lt.subList(catalog['artistas'],lt.size(catalog['artistas'])-2,3)
        print(tresartistas)

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
