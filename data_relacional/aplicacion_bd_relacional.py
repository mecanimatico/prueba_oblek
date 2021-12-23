# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:04:04 2021

@author: User
"""

import sqlite3
import os

os.chdir('D:/Documents/prueba/data_relacional')

# Es la plantilla para crear un producto
class Producto:
    def __init__(self, nombre, precio, seccion):
        self.nombre = nombre
        self.precio = precio
        self.seccion = seccion
    
    # Método para crear una tabla
    @classmethod
    def crear_tabla(cls):
        query = 'CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO VARCHAR(10),SECCION VARCHAR(20))'
        mi_data = sqlite3.connect('data_2')
        mi_cursor = mi_data.cursor()
        mi_cursor.execute(query)
        
    # Método para almacenar un producto en la tabla
    def guardar_producto(self):
        query = 'INSERT INTO PRODUCTOS (NOMBRE_ARTICULO, PRECIO, SECCION) VALUES ("'+ self.nombre +'","'+ str(self.precio) +'","'+ self.seccion +'")'
        self.__ejecutar(query)
    
    # Función privada que ejecuta cualquier query
    def __ejecutar(self, query):
        mi_data = sqlite3.connect('data_2')
        mi_cursor = mi_data.cursor()
        mi_cursor.execute(query)
        mi_data.commit()
     
    # Método de clase lista los productos en la tabla
    @classmethod  
    def listar_productos(cls):
        mi_data = sqlite3.connect('data_2')
        mi_cursor = mi_data.cursor()
        query_1 = 'SELECT * FROM PRODUCTOS'
        mi_cursor.execute(query_1)
        rows = mi_cursor.fetchall()
        for row in rows:
           print(row)
        
# Se crea el producto aceite
# Crear un menú en python
# Desea listar o agregar producto

# Se crea una instancia
#aceite = Producto('oliosoya', 3500, 'grasas')

# Para crear tabla
#Producto.crear_tabla()
# Para listar producto
# Producto.listar_tabla()
