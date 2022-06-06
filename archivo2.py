# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 23:19:30 2022

@author: USER
"""

import archivo1

def menu():
    print("digite una opcion")
    print("1.mostrar \n 2.agregar \n 3.eliminar \n 4.crear \n 5.salir")

def mostrar():
    print("opcion para mostrar el contenido de un archivo")
    nombre_del_archivo = input("digite el nombre del archivo que desea visualizar: ")
    print(archivo1.leer_contenido_archivo(nombre_del_archivo))

def agregar():
    print("opcion para agregar contenido a un archivo")
    nombre_archivo = input("digite aqui el nombre del archivo: ") 
    contenido_nuevo = input("digite aqui el contenido del archivo: ")
    archivo1.agregar_contenido_archivo(nombre_archivo, contenido_nuevo)

def eliminar():
    print("opcion para eliminar un archivo")
    nombre_archivo = input("digite el nombre del archivo que desa eliminar:")
    archivo1.eliminar_archivo(nombre_archivo)

def crear():
    print("opcion para crear archivo")
    nombre_archivo = input("digite el nombre del archivo: ")
    contenido = input("digite aqui el contenido del archivo")
    archivo1.crear_archivo(nombre_archivo, contenido)
    
def salir():
    print("Gracias por su visita")
    
def error():
    print("Opción incorrecta")
    
opcion=1

while opcion!=5:
    menu()
    opcion = int(input("opcion: "))
    if opcion==1:
        mostrar()
    elif opcion==2:
        agregar()
    elif opcion==3:
        eliminar()
    elif opcion==4:
        crear()
    elif opcion==5:
        salir()
    else:
        error()
        