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
import time

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


def initCatalog():
    """
    Inicializa el catalogo de obras
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadData(catalog)

def organizarobras(catalog):
    """
    Organiza el catálogo por el método elegido
    """
    controller.organizarobras(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['obras'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artistas'])))
        print('Últimos 3 elementos de obras:')
        tresobras = lt.subList(catalog['obras'],lt.size(catalog['obras'])-2,3)
        print(tresobras)
        print('Últimos 3 elementos de artistas:')
        tresartistas = lt.subList(catalog['artistas'],lt.size(catalog['artistas'])-2,3)
        print(tresartistas)

    elif int(inputs[0]) == 3:
        fecha_inicial = input('Escriba la fecha inicial en formato YYYY-MM-DD: ')
        fecha_final = input('Escriba la fecha final en formato YYYY-MM-DD: ')
        start_time = time.process_time()
        print('Organizando el catálogo ...')
        organizarobras(catalog)
        rangoobras = controller.rangoobras(catalog,fecha_inicial,fecha_final)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print('El programa se demoró '+ str(elapsed_time_mseg) + ' en ordenar los datos de muestra por medio de Merge sort.')
        i = 0
        print('Hay ' + str(lt.size(rangoobras)) + ' obras en el rango indicado.')
        print(controller.no_compradas(rangoobras) + ' de estas obras fueron adquiridas por compra.')
        print('Las 3 primeras y 3 últimas obras en el rango son:')
        while i < 3:
            print('Titulo: ' + (lt.getElement(rangoobras,i))['Title'] + '   Artista(s): ' + controller.buscarid((lt.getElement(rangoobras,i))['ConstituentID'],catalog) + '    Fecha: ' + (lt.getElement(rangoobras,i))['Date'] + '    Fecha de adquisición: ' + (lt.getElement(rangoobras,i))['DateAcquired'] + '   Medio: ' + (lt.getElement(rangoobras,i))['Medium'] + '    Dimensiones: ' + (lt.getElement(rangoobras,i))['Dimensions'])
            i += 1
        while i > 0:
            print('Titulo: ' + (lt.getElement(rangoobras,lt.size(rangoobras) - i))['Title'] + '   Artista(s): ' + controller.buscarid((lt.getElement(rangoobras,lt.size(rangoobras) - i))['ConstituentID'],catalog) + '    Fecha: ' + (lt.getElement(rangoobras,lt.size(rangoobras) - i))['Date'] + '    Fecha de adquisición: ' + (lt.getElement(rangoobras,lt.size(rangoobras) - i))['DateAcquired'] + '   Medio: ' + (lt.getElement(rangoobras,lt.size(rangoobras) - i))['Medium'] + '    Dimensiones: ' + (lt.getElement(rangoobras,lt.size(rangoobras) - i))['Dimensions'])
            i -= 1

    else:
        sys.exit(0)
sys.exit(0)
