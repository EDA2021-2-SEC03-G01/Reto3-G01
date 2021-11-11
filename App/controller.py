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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init():
    analyzer = model.newAnalyzer()
    return analyzer
# Funciones para la carga de datos
def loadData(analyzer, UFOS):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    i=0
    if UFOS == 'UFOS/UFOS-utf8-small.csv':
        t=803
    else:
        t=80332
    UFOS = cf.data_dir + UFOS
    input_file = csv.DictReader(open(UFOS, encoding="utf-8"),
                                delimiter=",")
    for crime in input_file:
        model.addEvent(analyzer, crime)
        print(f"{i}/{t}", end='\r')
        i+=1
    return analyzer
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)

#Requerimientos

#Req 1
def avistamientos_ciudad(analyzer, ciudad):
    tot, lista_avs, tot_avs = model.avistamientos_ciudad(analyzer, ciudad)
    return tot, lista_avs, tot_avs

#Req 2
def avistamientos_duracion(analyzer, min, max):
    tot_duraciones, max_duracion, max_count, total_avs, lista_avs = model.avistamientos_duracion(analyzer, min, max)
    return tot_duraciones, max_duracion, max_count, total_avs, lista_avs

#Req 3
def avistamientos_hora(analyzer, hora_in, hora_fin):
    max_hora, max_count, tot_horas, total_avs, lista_def = model.avistamientos_hora(analyzer, hora_in, hora_fin)
    return max_hora, max_count, tot_horas, total_avs, lista_def

#Req 4
def avistamientos_fecha(analyzer, min, max):
    min_fecha, min_count, tot_fechas, total_avs, lista_avs = model.avistamientos_fecha(analyzer, min, max)
    return min_fecha, min_count, tot_fechas, total_avs, lista_avs

#Req 5
def avistamientos_long_lat(analyzer, minLong, maxLong, minLat, maxLat):
    total_avs, lista_avs = model.avistamientos_long_lat(analyzer, minLong, maxLong, minLat, maxLat)
    return total_avs, lista_avs

#Bono
def avistamientos_zona(analyzer, minLong, maxLong, minLat, maxLat):
    total_avs, lista_avs, map = model.avistamientos_zona(analyzer, minLong, maxLong, minLat, maxLat)
    return total_avs, lista_avs, map