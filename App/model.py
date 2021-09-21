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


from posixpath import split
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort
from DISClib.Algorithms.Sorting import quicksort 
from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import mergesort
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de obras. Crea una lista vacia para guardar
    todas las obras, adicionalmente, crea una lista vacia para los artistas.
     Retorna el catalogo inicializado.
    """
    catalog = {'obras': None,
               'artistas': None,}

    catalog['obras'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['artistas'] = lt.newList(datastructure='ARRAY_LIST')

    return catalog

# Funciones para agregar informacion al catalogo
def addObra(catalog, obra):
    lt.addLast(catalog['obras'], obra)

def addArtista(catalog, artista):
    lt.addLast(catalog['artistas'], artista)

# Funciones para creacion de datos

# Funciones de consulta
def busquedabinaria(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return busquedabinaria(array, element, start, mid-1)
    else:
        return busquedabinaria(array, element, mid+1, end)
    
def busquedaano(lista, ano, start, end, tipo,criterio):
    if start != end:
        mid = (start + end) // 2
        if ano == (aentero(lt.getElement(lista,mid)[criterio])):
            if tipo == 'menor':
                mid -= 1
                while aentero(lt.getElement(lista,mid)[criterio]) == ano:
                    mid -= 1
                return mid + 1
            elif tipo == 'mayor':
                mid += 1
                while aentero(lt.getElement(lista,mid)[criterio]) == ano:
                    mid += 1
                return mid - 1

        if ano < aentero(lt.getElement(lista,mid)[criterio]):
            return busquedaano(lista, ano, start, mid-1,tipo,criterio)
        else:
            return busquedaano(lista, ano, mid+1, end,tipo,criterio)
    elif tipo == 'menor':
            if ano == (aentero(lt.getElement(lista,end)[criterio])):
                return end
            elif ano > aentero(lt.getElement(lista,end)[criterio]):
                while (ano > aentero(lt.getElement(lista,end)[criterio])) and aentero(lt.getElement(lista,end)[criterio]) != 0:
                    end += 1
            return end
    elif tipo == 'mayor':
        if ano < aentero(lt.getElement(lista,end)[criterio]):
            while ano < aentero(lt.getElement(lista,end)[criterio]):
                end -= 1
        return end

    #Requerimientos 1 y 2
def buscarid(id,artistas):
    x = id.replace('[','')
    y = x.replace(']','')
    ids = y.split(',')
    indices = lt.newList(datastructure='ARRAY_LIST')
    for i in ids:
        lt.addLast(indices,lt.getElement(artistas,(busquedabinaria(artistas,int(ids[i]),0,lt.size(artistas) - 1))))
    return indices

def aentero(str):
    if str == '':
        return 0    
    return int(str.replace('-',''))


def rangoobras(obras,fecha_inicial,fecha_final):
    """
    Crea y devuelve la sublista de catalog con las obras ordenadas desde un año
    de inicio hasta otro de final.
    """
    fecha_inicial = aentero(fecha_inicial)
    fecha_final = aentero(fecha_final)
    indiceinicial = busquedaano(obras,fecha_inicial,0,lt.size(obras) - 1,'menor','DateAcquired')
    print(indiceinicial)
    if lt.getElement(obras,indiceinicial)['DateAcquired'] == '':
        return lt.newList(datastructure='ARRAY_LIST')
    indicefinal = busquedaano(obras,fecha_final,0,lt.size(obras) - 1,'mayor','DateAcquired')
    print(indicefinal)
    rango = lt.subList(obras,indiceinicial,(indicefinal-indiceinicial+1))
    return rango

def no_compradas(list):
    i = 0
    compradas = 0
    while i < lt.size(list):
        if (lt.getElement(list,0))['CreditLine'] == 'Purchase':
            compradas += 1
        i += 1
    return compradas

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

def cmpArtistsByConstituentID(artist1, artist2):
    """
    Devuelve verdadero (True) si el 'ConstituentID' de artist1 es menor que el de artist2
    Args:
    artist1: informacion del primer artista que incluye su valor 'ConstituentID'
    artist2: informacion del segund artista que incluye su valor 'ConstituentID'
    """
    return artist1['ConstituentID'] < artist2['ConstituentID']

# Funciones de ordenamiento

def organizarobras(obras):
    """
    Organiza el catálogo por el método elegido
    """
    mergesort.sort(obras,cmpArtworkByDateAcquired)

def organizarartistas(artistas):
    """
    Organiza los artistas por el método elegido
    """
    mergesort.sort(artistas,cmpArtistsByConstituentID)