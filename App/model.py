﻿"""
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


from DISClib.DataStructures.arraylist import getElement
from posixpath import split
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
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
def busquedaID(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if element == int(lt.getElement(array,mid)['ConstituentID']):
        return mid

    if element < int(lt.getElement(array,mid)['ConstituentID']):
        return busquedaID(array, element, start, mid-1)
    else:
        return busquedaID(array, element, mid+1, end)
    
def busquedaano(lista, ano, start, end, tipo,criterio):
    if (start != end) and (end - start) > 1:
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
        if ano < (aentero(lt.getElement(lista,end)[criterio])):
            while (ano < aentero(lt.getElement(lista,end)[criterio])) and aentero(lt.getElement(lista,end)[criterio]) != 0:
                end -= 1
            return end + 1    
        elif ano > aentero(lt.getElement(lista,end)[criterio]):
            
            while (ano > aentero(lt.getElement(lista,end)[criterio])) and aentero(lt.getElement(lista,end)[criterio]) != 0:
                end += 1
            return end - 1      
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
        lt.addLast(indices,lt.getElement(artistas,(busquedaID(artistas,int(i),0,lt.size(artistas) - 1))))
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
    if lt.getElement(obras,indiceinicial)['DateAcquired'] == '':
        return lt.newList(datastructure='ARRAY_LIST')
    indicefinal = busquedaano(obras,fecha_final,0,lt.size(obras) - 1,'mayor','DateAcquired')
    rango = lt.subList(obras,indiceinicial,(indicefinal-indiceinicial+1))
    return rango

def no_compradas(list):
    i = 1
    compradas = 0
    while i <= lt.size(list):
        if 'purchase' in ((lt.getElement(list,i))['CreditLine']).lower():
            compradas += 1
        i += 1
    return compradas

def rangoartistas(artistas,fecha_inicial,fecha_final):
    """
    Crea y devuelve la sublista de catalog con los artistas ordenados desde un año
    de inicio hasta otro de final.
    """
    fecha_inicial = aentero(fecha_inicial)
    fecha_final = aentero(fecha_final)
    indiceinicial = busquedaano(artistas,fecha_inicial,0,lt.size(artistas) - 1,'menor','BeginDate')
    if lt.getElement(artistas,indiceinicial)['BeginDate'] == '0':
        return lt.newList(datastructure='ARRAY_LIST')
    indicefinal = busquedaano(artistas,fecha_final,0,lt.size(artistas) - 1,'mayor','BeginDate')
    rango = lt.subList(artistas,indiceinicial,(indicefinal-indiceinicial+1))
    return rango
    #Requerimiento 3
def buscarnombre(artistas,nombre):
    """
    Encuentra el ID asociado a un nombre de artista que llega por parámetro
    """
    p = 1
    while p <= lt.size(artistas):
        if lt.getElement(artistas,p)['DisplayName'] == nombre:
            return (lt.getElement(artistas,p)['ConstituentID'])
        p += 1
    return 0

def obrasartista(lista,id):
    obrasartista = lt.newList(datastructure='ARRAY_LIST')
    z = 1
    while z <= lt.size(lista):
        idsobra = lt.getElement(lista,z)['ConstituentID']
        x = idsobra.replace('[','')
        y = x.replace(']','')
        ids = y.split(',')
        if id in ids:
            lt.addLast(obrasartista,lt.getElement(lista,z))
        z += 1
    return obrasartista

def catalogarmedios(lista):
    dicc = mp.newMap(maptype='PROBING',numelements=25)
    z = 1
    while z <= lt.size(lista):
        if not(mp.contains(dicc,(lt.getElement(lista,z))['Medium'])):
            mp.put(dicc,(lt.getElement(lista,z))['Medium'],lt.newList(datastructure='ARRAY_LIST'))
        lt.addLast((mp.get(dicc,(lt.getElement(lista,z))['Medium']))['value'],lt.getElement(lista,z))   
        z += 1
    return dicc

def tecnicamayor(obrasartista):
    """
    Devuelve la técnica más usadas entre las obras del artista
    """
    iterador = lt.iterator(mp.keySet(obrasartista))
    mayor = ''
    for key in iterador:
        #if mayor != '':
        try:
            if lt.size((mp.get(obrasartista,key))['value']) > lt.size((mp.get(obrasartista,mayor))['value']):
                mayor = key                
        except:
            mayor = key
    return mayor

    #Requerimiento 5
def obrasdpto(lista,dpto):
    """
    Devuelve una lista con las obras de un departamento
    """
    obrasdpto = lt.newList(datastructure='ARRAY_LIST')
    z = 1
    while z <= lt.size(lista):
        if lt.getElement(lista,z)['Department'] == dpto:
            lt.addLast(obrasdpto,lt.getElement(lista,z))
        z += 1
    return obrasdpto

def agregarprecios(obras):
    """
    Agrega una columna de precio de transporte a cada obra en la lista
    """
    costos = lt.newList(datastructure='ARRAY_LIST')
    costototal = 0
    z = 1
    while z <= lt.size(obras):
        costofinal = 0
        pesofinal = 0
        try:
            costofinal = 72.00 * float(lt.getElement(obras,z)['Weight (kg)'])
            pesofinal += float(lt.getElement(obras,z)['Weight (kg)'])
        except:
            None
        try:
            costo_area = 72.00 * ((2 * 3.1416 * (float(lt.getElement(obras,z)['Diameter (cm)'])/2) * float(lt.getElement(obras,z)['Diameter (cm)']) + 2 * 3.1416 * ((float(lt.getElement(obras,z)['Diameter (cm)'])/2) ** 2))/10000)
        except:
            try:
                costo_area = 72.00 * (((2 * float(lt.getElement(obras,z)['Height (cm)']) * (float(lt.getElement(obras,z)['Depth (cm)']) + float(lt.getElement(obras,z)['Width (cm)']))) + (2 * float(lt.getElement(obras,z)['Depth (cm)'] * float(lt.getElement(obras,z)['Width (cm)']))))/10000)
            except:
                try:
                    costo_area = 72.00 * ((float(lt.getElement(obras,z)['Width (cm)']) * float(lt.getElement(obras,z)['Height (cm)']))/10000)
                except:
                    costo_area = 0
        try:
            costo_volumen = 72.00 * (((3.1416 * (float(lt.getElement(obras,z)['Diameter (cm)'])/2) ** 2) * (float(lt.getElement(obras,z)['Height (cm)'])))/1000000)
        except:
            try:
                costo_volumen = 72.00 * ((float(lt.getElement(obras,z)['Width (cm)']) * float(lt.getElement(obras,z)['Height (cm)']) * float(lt.getElement(obras,z)['Depth (cm)']))/1000000)
            except:
                costo_volumen = 0
        if costo_area > costofinal:
            costofinal = costo_area
        if costo_volumen > costofinal:
            costofinal = costo_volumen
        if costofinal == 0:
            costofinal = 48.00
        lt.addLast(costos,lt.newList('ARRAY_LIST'))
        lt.addLast(lt.getElement(costos,z),lt.getElement(obras,z))
        lt.addLast(lt.getElement(costos,z),costofinal)
        costototal += costofinal
        z += 1
    return (costos,costototal,pesofinal)

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
    artist2: informacion del segundo artista que incluye su valor 'ConstituentID'
    """
    return int(artist1['ConstituentID']) < int(artist2['ConstituentID'])

def cmpArtistsByDate(artist1, artist2):
    """
    Devuelve verdadero (True) si el 'BeginDate' de artist1 es menor que el de artist2
    Args:
    artist1: informacion del primer artista que incluye su valor 'BeginDate'
    artist2: informacion del segundo artista que incluye su valor 'BeginDate'
    """
    return int(artist1['BeginDate']) < int(artist2['BeginDate'])

def cmpArtworkByCost(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el costo de transporte de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su costo de transporte
    artwork2: informacion de la segunda obra que incluye su costo de transporte
    """
    return lt.lastElement(artwork1) > lt.lastElement(artwork2)

def cmpArtworkByDate(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'Date' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'Date'
    artwork2: informacion de la segunda obra que incluye su valor 'Date'
    """
    return (lt.firstElement(artwork1)['Date'] < lt.firstElement(artwork2)['Date'])

# Funciones de ordenamiento

def organizarobras(obras):
    """
    Organiza el catálogo por el método elegido
    """
    mergesort.sort(obras,cmpArtworkByDateAcquired)

def organizarartistas(artistas,cmpf):
    """
    Organiza los artistas por el método elegido
    """
    if cmpf == 'ID':
        mergesort.sort(artistas,cmpArtistsByConstituentID)
    else:
        mergesort.sort(artistas,cmpArtistsByDate)

def organizarcostos(costos):
    """
    Organiza los costos por el método elegido
    """
    mergesort.sort(costos,cmpArtworkByCost)

def organizarfechas(costos):
    """
    Organiza las obras por su año de creación
    """
    mergesort.sort(costos,cmpArtworkByDate)