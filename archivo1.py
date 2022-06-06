# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 23:07:04 2022

@author: USER
"""

import os 

def crear_archivo(nombre_archivo,contenido):
    archivo = open(nombre_archivo,"wt")#crear archivo que permita escribir
    archivo.write(contenido)#escribir contenido en el archivo
    archivo.close()

def eliminar_archivo(nombre_archivo):
    os.remove(nombre_archivo)#eliminar archivo
    
def agregar_contenido_archivo(nombre_archivo,contenido_nuevo):
    archivo = open(nombre_archivo,"at")#agregar nuevo contenido a un archivo
    archivo.write("\n" + contenido_nuevo)#agregando 
    archivo.close()
    
def leer_contenido_archivo(nombre_archivo):
    archivo = open(nombre_archivo,"rt",encoding="utf8")
    return archivo.read()

