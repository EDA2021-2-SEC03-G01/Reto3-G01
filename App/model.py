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
from DISClib.Algorithms.Sorting import mergesort as ms
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
                                    comparefunction=compareDates)
    analyzer['duraciones'] = om.newMap(omaptype='BST',
                                    comparefunction=compareDates)
    analyzer["horas"] = om.newMap(omaptype='BST',
                                    comparefunction=compareHoras)
    analyzer['longitudes'] = om.newMap(omaptype='BST',
                                    comparefunction=compareDates)
    return analyzer

# Funciones para agregar informacion al catalogo
def addEvent(analyzer, event):
    lt.addLast(analyzer['events'], event)
    updateDateIndex(analyzer['dateIndex'], event)
    updateCiudades(analyzer["ciudades"], event)
    updateDuraciones(analyzer["duraciones"], event)
    updateHoras(analyzer["horas"], event)
    updateLongitudes(analyzer["longitudes"], event)
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

def updateDuraciones(map, event):
    duracion = event['duration (seconds)']
    entry = om.get(map, duracion)
    if entry is None:
        datentry = newDataEntry(event)
        om.put(map, duracion, datentry)
    else:
        datentry = me.getValue(entry)
    add(datentry, event)
    return map

def updateHoras(map, event):
    hora = event["datetime"]
    hora = hora.split(" ")[1]
    entry = om.get(map, hora)
    if entry is None:
        dataentry = newDataEntry(event)
        om.put(map, hora, dataentry)
    else:
        dataentry = me.getValue(entry)
    add(dataentry, event)
    return map

def updateLongitudes(map, event):
    longitude = event['longitude']
    entry = om.get(map, longitude)
    if entry is None:
        datentry = newDataEntry(event)
        om.put(map, longitude, datentry)
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

def compareDates1(av1, av2):
    """
    Compara dos fechas
    """    
    date1 = datetime.datetime.strptime(av1["date"], '%Y-%m-%d %H:%M:%S')
    date2 = datetime.datetime.strptime(av2["date"], '%Y-%m-%d %H:%M:%S')
    if (date1 <= date2):
        return True
    else:
        return False

def compareDuracion(av1, av2):
    """
    Compara dos fechas
    """    
    duration1 = float(av1["duration"])
    duration2 = float(av2["duration"])
    if (duration1 < duration2):
        return True
    elif duration1 == duration2:
        return compareCities(av1, av2)
    else:
        return False

def compareCities(av1, av2):
    """
    Compara dos fechas
    """    
    city1 = av1["city"]
    city2 = av2["city"]
    if (city1 <= city2):
        return True
    else:
        return False

def compareHoras(hora1, hora2):
    """
    Compara dos Horas
    """
    if " " in hora1:
        hora1=hora1.split(" ")[1]
    if " " in hora2:
        hora2=hora2.split(" ")[1]
    hora1 = datetime.datetime.strptime(str(hora1), '%H:%M:%S')
    hora2 = datetime.datetime.strptime(str(hora2), '%H:%M:%S')
    if hora1 > hora2:
        return 1
    elif hora1 == hora2:
        return 0
    else:
        return -1

def compareLatitudes(av1, av2):
    """
    Compara dos fechas
    """    
    lat1 = av1["latitude"]
    lat2 = av2["latitude"]
    if (lat1 <= lat2):
        return True
    else:
        return False

#primeros y ultimos n
def f_primeros_ultimos(lista, n):
    c = 0
    len = lt.size(lista)
    lista_def = lt.newList(datastructure="ARRAYLIST")
    for e in lt.iterator(lista):
        lt.addLast(lista_def, e)
        c += 1
        if c == n:
            c -= 1
            break
    while c >= 0:
        e = lt.getElement(lista, len-c)
        lt.addLast(lista_def, e)
        c -= 1
    return lista_def

#Requerimientos

#Req 1
def avistamientos_ciudad(analyzer, ciudad):
    arbol_ciudades = analyzer["ciudades"]
    ciudades = om.keySet(arbol_ciudades)
    tot_ciudades = lt.size(ciudades)
    avs_ciudad = om.get(arbol_ciudades, ciudad)["value"]
    lista_avs = lt.newList(datastructure="ARRAY_LIST", cmpfunction=compareDates1)
    for av in lt.iterator(avs_ciudad):
        dic_av = {"date":av["datetime"], "city":av["city"], "state":av["state"], "country":av["country"], "shape":av["shape"], "duration":av["duration (seconds)"]}
        lt.addLast(lista_avs, dic_av)
    #Total avistamientos ciudad
    tot_avs = lt.size(lista_avs)
    #Ordenar por fecha
    lista_avs = ms.sort(lista_avs, compareDates1)
    #Primeros y últimos tres
    lista_def = f_primeros_ultimos(lista_avs, 3)
    return tot_ciudades, lista_def, tot_avs

#Req 2 - Daniela
def avistamientos_duracion(analyzer, min, max):
    arbol_duraciones = analyzer["duraciones"]
    duraciones = om.keySet(arbol_duraciones)
    #maxima duracion registrada
    max_duracion = 0
    for d in lt.iterator(duraciones):
        if float(d) > max_duracion:
            max_duracion = float(d)
    #numero de avistamientos con la duracion maxima
    max_count = lt.size(om.get(arbol_duraciones, str(max_duracion))["value"])
    #total duraciones diferentes
    tot_duraciones = lt.size(duraciones)
    lista_avs = lt.newList(datastructure="ARRAY_LIST", cmpfunction=compareDuracion)
    for d in lt.iterator(duraciones):
        if float(d) >= min and float(d) <= max:
            avs_duracion = om.get(arbol_duraciones, d)["value"]
            for av in lt.iterator(avs_duracion):
                dic_av = {"date":av["datetime"], "city":av["city"], "state":av["state"], "country":av["country"], "shape":av["shape"], "duration":av["duration (seconds)"]}
                lt.addLast(lista_avs, dic_av)
    #Total avistamientos en el rango de duraciones
    total_avs = lt.size(lista_avs)
    #Ordenar por duracion y ciudades
    lista_avs = ms.sort(lista_avs, compareDuracion)
    #Primeros y últimos tres
    lista_def = f_primeros_ultimos(lista_avs, 3)
    return tot_duraciones, max_duracion, max_count, total_avs, lista_def

#req 3 - Tomas
def avistamientos_hora(analyzer, hora_in, hora_fin):
    arbol_horas = analyzer["horas"]
    horas = om.keySet(arbol_horas)
    max_hora = lt.getElement(horas, lt.size(horas))
    max_count = lt.size(om.get(arbol_horas, max_hora)["value"])
    tot_horas = lt.size(horas)
    lista_avs = lt.newList(datastructure="ARRAY_LIST", cmpfunction=None)
    hora_in = datetime.datetime.strptime(str(hora_in), "%H:%M:%S")
    hora_fin = datetime.datetime.strptime(str(hora_fin), "%H:%M:%S")
    for h in lt.iterator(horas):
        h = datetime.datetime.strptime(str(h), "%H:%M:%S")
        if h >= hora_in and h <= hora_fin:
            avs_hora = om.get(arbol_horas, str(h))["value"]
            for av in lt.iterator(avs_hora):
                dic_av = {"date":av["datetime"], "city":av["city"], "state":av["state"], "country":av["country"], "shape":av["shape"], "duration":av["duration (seconds)"]}
                lt.addLast(lista_avs, dic_av)
    #Total avistamientos en el rango de horas
    total_avs = lt.size(lista_avs)
    #Primeros y últimos tres
    lista_def = f_primeros_ultimos(lista_avs, 3)
    return max_hora, max_count, tot_horas, total_avs, lista_def  

#req 4
def avistamientos_fecha(analyzer, min, max):
    arbol_fechas = analyzer['dateIndex']
    fechas = om.keySet(arbol_fechas)
    min_fecha = lt.getElement(fechas, 1)
    min_count = lt.size(om.get(arbol_fechas, min_fecha)["value"])
    tot_fechas = lt.size(fechas)
    lista_avs = lt.newList(datastructure="ARRAY_LIST", cmpfunction=compareDuracion)
    for f in lt.iterator(fechas):
        f = datetime.datetime.strptime(str(f), "%Y-%m-%d").date()
        min = datetime.datetime.strptime(str(min), "%Y-%m-%d").date()
        max = datetime.datetime.strptime(str(max), "%Y-%m-%d").date()
        if (f) >= min and (f) <= max:
            avs_fecha = om.get(arbol_fechas, f)["value"]
            for av in lt.iterator(avs_fecha):
                dic_av = {"date":av["datetime"], "city":av["city"], "state":av["state"], "country":av["country"], "shape":av["shape"], "duration":av["duration (seconds)"]}
                lt.addLast(lista_avs, dic_av)
    #Total avistamientos en el rango de duraciones
    total_avs = lt.size(lista_avs)
    #Primeros y últimos tres
    lista_def = f_primeros_ultimos(lista_avs, 3)
    return min_fecha, min_count, tot_fechas, total_avs, lista_def

#Req 5
def avistamientos_long_lat(analyzer, minLong, maxLong, minLat, maxLat):
    arbol_long = analyzer['longitudes']
    longitudes = om.keySet(arbol_long)
    lista_avs = lt.newList(datastructure="ARRAY_LIST", cmpfunction=compareDuracion)
    for long in lt.iterator(longitudes):
        if round(float(long), 2) >= minLong and round(float(long), 2) <= maxLong:
            avs_long= om.get(arbol_long, long)["value"]
            for av in lt.iterator(avs_long):
                lat = round(float(av["latitude"]),2)
                if lat >= minLat and lat <= maxLat:
                    dic_av = {"date":av["datetime"], "city":av["city"], "state":av["state"], "country":av["country"], "shape":av["shape"], 
                            "duration":av["duration (seconds)"], "latitude":round(lat, 2), "longitude":round(float(long), 2)}
                    lt.addLast(lista_avs, dic_av)
    #Total avistamientos en el rango de duraciones
    total_avs = lt.size(lista_avs)
    #Ordenar por latitud y longitud
    lista_avs = ms.sort(lista_avs, compareLatitudes)
    #Primeros y últimos tres
    if total_avs > 10:
        lista_avs = f_primeros_ultimos(lista_avs, 5)
    return total_avs, lista_avs

#BONO
def avistamientos_zona(analyzer, minLong, maxLong, minLat, maxLat):
    
    return