# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:04:04 2021

@author: Heber Pareja Reinoso
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
        
entrada = 0
while entrada != 4:
    print('--'*20)
    print('1. Crear tabla')
    print('2. Crear producto')
    print('3. Listar productos')
    print('4. Salir')
    entrada = int(input('Ingrese una opción > '))
    if entrada == 1:
        try:
            Producto.crear_tabla()
            print('--'*20)
            print('La tabla ha sido creada')
        except:
            print('--'*20)
            print('La tabla ya existe')
           
    elif entrada == 2:
        nombre =input('Ingrese nombre del producto >')
        precio = input('Ingrese el valor del producto >')
        seccion = input('Ingrese la sección del producto >')
        producto = Producto(nombre, precio, seccion)
        producto.guardar_producto()
        print('--'*20)
        print('Producto creado exitosamente')
       
    elif entrada == 3:
        Producto.listar_productos()
        
    elif entrada == 4:
        print('Gracias por visitarnos, te esperamos de nuevo')
        break
    else:
        print('--'*20)
        print('Opción no válida')
    print('--'*20)
