"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(estructura):
    """
    Inicializa el catálogo de obras. Crea una lista vacia para guardar
    todas las obras, adicionalmente, crea una lista vacia para los artistas.
     Retorna el catalogo inicializado.
    """
    catalog = {'obras': None,
               'artistas': None,}

    catalog['obras'] = lt.newList(estructura)
    catalog['artistas'] = lt.newList(estructura)

    return catalog

# Funciones para agregar informacion al catalogo
def addObra(catalog, obra):
    lt.addLast(catalog['obras'], obra)

def addArtista(catalog, artista):
    lt.addLast(catalog['artistas'], artista)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artistaname1, artista):
    if (artistaname1.lower() in artista['name'].lower()):
        return 0
    return -1

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return artwork1['DateAcquired'] < artwork2['DateAcquired']


# Funciones de ordenamiento