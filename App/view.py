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

from datetime import datetime
from os import startfile
import config as cf
import sys
import controller
import folium
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
ufos = 'UFOS/UFOS-utf8-small.csv'
cont = None

def printMenu():
    print("\nBienvenido")
    print("1- Crear el catálogo")
    print("2- Cargar datos")
    print("3- Contar los avistamientos en una ciudad")
    print("4- Contar los avistamientos por duracion")
    print("5- Contar los avistamientos por hora/minutos del dia")
    print("6- Contar los avistamientos en un rango de fechas")
    print("7- Contar los avistamientos de una Zona Geografica")
    print("8- Visualizar los avistamientos de una Zona Geografica")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        print("\nInicializando....")
        cont = controller.init()
        
    elif int(inputs[0]) == 2:
        print("\nCargando...\n")
        controller.loadData(cont, ufos)
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))

    elif int(inputs[0]) == 3:
        ciudad = input("\nIngrese la ciudad de interés: ")
        tot, lista_avs, tot_avs = controller.avistamientos_ciudad(cont, ciudad)
        print("\nHay " + str(tot) + " ciudades donde han habido avistamientos reportados.")
        print("\nEn " + ciudad + " se han reportado " + str(tot_avs) + " avistamientos.")
        print("\nA continuación se muestran los primeros y últimos 3:")
        for av in lt.iterator(lista_avs):
            print(av)

    elif int(inputs[0]) == 4:
        min = float(input("\nIngrese la duración mínima: "))
        max = float(input("Ingrese la duración máxima: "))
        tot_duraciones, max_duracion, max_count, total_avs, lista_avs = controller.avistamientos_duracion(cont, min, max)
        print("\nSe registraron " + str(tot_duraciones) + " duraciones direfentes.")
        print("\nLa duración máxima registrada es de " + str(max_duracion) + " segundos y hay " + str(max_count) + " avistamiento(s) con esa duración.")
        print("\nHubo " + str(total_avs) + " avistamientos con duraciones entre " + str(min) + " y " + str(max) + " segundos.")
        print("\nA continuación se muestran los primeros y últimos 3:")
        for av in lt.iterator(lista_avs):
            print(av)

    elif int(inputs[0]) == 5:
        hora_in = input("\nIngrese la hora inicial: ")
        hora_fin = input("Ingrese la hora final: ")
        max_hora, max_count, tot_horas, total_avs, lista_def = controller.avistamientos_hora(cont, hora_in, hora_fin)
        print("\nSe registraron avistamientos en " + str(tot_horas) + " horas diferentes")
        print("\nEl avistamiento más tardio registrado es " + str(max_hora) + " y hay " + str(max_count) + " avistamientos a esa hora")
        print("\nHubo " + str(total_avs) + " avistamientos entre las horas consultadas")
        print("\nA continuacion se muestran los primeros y ultimos 3 avistamientos en este rango:")
        for av in lt.iterator(lista_def):
            print(av)

    elif int(inputs[0]) == 6:
        min = input("\nIngrese la fecha (AAAA-MM-DD) mínima: ")
        max = input("Ingrese la fecha (AAAA-MM-DD) máxima: ")
        min_fecha, min_count, tot_fechas, total_avs, lista_avs = controller.avistamientos_fecha(cont, min, max)
        print("\nSe registraron avistamientos en " + str(tot_fechas) + " fechas direfentes.")
        print("\nLa fecha más antigua registrada es " + str(min_fecha) + " y hay " + str(min_count) + " avistamiento(s) en esa fecha.")
        print("\nHubo " + str(total_avs) + " avistamientos entre " + str(min) + " y " + str(max))
        print("\nA continuación se muestran los primeros y últimos 3:")
        for av in lt.iterator(lista_avs):
            print(av)
    
    elif int(inputs[0]) == 7:
        minLong = float(input("\nIngrese la longitud mínima: "))
        maxLong = float(input("Ingrese la longitud máxima: "))
        minLat = float(input("\nIngrese la latitud mínima: "))
        maxLat = float(input("Ingrese la latitud máxima: "))
        total_avs, lista_avs = controller.avistamientos_long_lat(cont, minLong, maxLong, minLat, maxLat)
        print("\nSe registraron " + str(total_avs) + " avistamientos dentro del área definida. ")
        print("\nA continuación se muestran los primeros y últimos 5:")
        for av in lt.iterator(lista_avs):
            print(av)

    elif int(inputs[0]) == 8:
        minLong = float(input("\nIngrese la longitud mínima: "))
        maxLong = float(input("Ingrese la longitud máxima: "))
        minLat = float(input("\nIngrese la latitud mínima: "))
        maxLat = float(input("Ingrese la latitud máxima: "))
        total_avs, lista_avs, map = controller.avistamientos_zona(cont, minLong, maxLong, minLat, maxLat)
        print("\nSe registraron " + str(total_avs) + " avistamientos dentro del área definida. ")
        print("\nA continuación se muestran los primeros y últimos 5:")
        for av in lt.iterator(lista_avs):
            print(av)
        startfile("mapa.html")

    else:
        sys.exit(0)

sys.exit(0)
