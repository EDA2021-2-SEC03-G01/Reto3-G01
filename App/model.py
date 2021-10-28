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
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'events': None,
                'dateIndex': None,
                'ciudades': None}

    analyzer['events'] = lt.newList('SINGLE_LINKED', compareDates)
    analyzer['dateIndex'] = om.newMap(omaptype='BST',
                                      comparefunction=compareDates)
    analyzer['ciudades'] = om.newMap(omaptype='BST',
                                    comparefunction=None)
    return analyzer
# Funciones para agregar informacion al catalogo
def addEvent(analyzer, event):
    lt.addLast(analyzer['events'], event)
    updateDateIndex(analyzer['dateIndex'], event)
    updateCiudades(analyzer["ciudades"],event)
    return analyzer

def updateDateIndex(map, event):
    occurreddate = event['datetime']
    eventdate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, eventdate.date())
    if entry is None:
        datentry = newDataEntry(event)
        om.put(map, eventdate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    add(datentry, event)
    return map

def updateCiudades(map, event):
    city = event['city']
    entry = om.get(map, city)
    if entry is None:
        datentry = newDataEntry(event)
        om.put(map, city, datentry)
    else:
        datentry = me.getValue(entry)
    add(datentry, event)
    return map

def add(datentry, event):
    lt.addLast(datentry, event)
    return datentry

def newDataEntry(event):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry=lt.newList(datastructure="ARRAY_LIST")
    return entry
# Funciones para creacion de datos

# Funciones de consulta
def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['dateIndex'])


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['dateIndex'])
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1