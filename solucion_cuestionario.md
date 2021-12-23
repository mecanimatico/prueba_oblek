# Desarrollo de cuestionario
1.	¿Qué es Python?
```
Es un lenguaje multiplataforma de código abierto, de alto nivel, interpretado y débilmente tipado, orientado a objetos y su filosofía está orientada a que el código sea fácil de leer
```
 2.	¿Consideras que Python es mejor a Java? ¿Por qué? 
 ```
El punto de vista de implementación de un lenguaje u otro depende de los requerimientos de un proyecto, por ejemplo. Si es un proyecto que requiere siempre estar cambiando y de una alta mantenibilidad, es mejor implementar Python; en cambio, si se requiere tiempo de respuesta rápida hacia el cliente, es mejor java
```
3.	¿Cuántos tipos de datos existen en Python? 
```
Son ellos: cadena de texto (string), número entero(int), número decimal (float), caracter (chr), booleanos (bool), complejos (complex), listas (list), range, arrays, conjunto (set), tuplas (tuples), diccionarios (dict), objects, none, iteradores, clases, instancias, excepciones
```
4.	¿Cuál es la diferencia entre tupla y lista? 
```
Las listas son dinámicas (mutables) y las tuplas son estáticas(inmutables)
```
5.	¿Qué es PEP8? 
```
Es una guía que indica las convenciones de estilo a seguir para escribir código Python, es decir, son recomendaciones que facilitan la escritura y lectura del código
```
6.	¿Qué es "pickling" y "unpickling"?
```
 Es el proceso mediante el cual una jerarquía de objetos de Python se convierte en una secuencia de bytes y unpickling  es la operación inversa
 ```
7.	¿Qué es "lambda"?
```
 Es una palabra reservada de Python para declarar funciones de manera corta, se le conocen también como funciones anónimas
 ```
8.	¿Cómo se administra la memoria dentro del lenguaje Python?
```
 El administrador de memoria de Python controla la asignación y desasignación de este espacio de almacenamiento mediante el uso de funciones API. El administrador de memoria realiza un seguimiento al número de referencias a cada objeto en el programa, cuando el recuento de referencias cae a cero, el recolector de basura automáticamente libera la memoria de ese objeto en particular, dado que ya no se usa
 ```
9.	¿Qué es "pass"? 
```
 Palabra reservada para una declaración nula, es decir, se utiliza cuando se quiere declarar una función o un bucle, pero no se quiere su ejecución
 ```
10.	¿Puedes copiar un objeto en el lenguaje Python?
```
 En Python las declaraciones de asignación no pueden copiar objetos, solo se genera una nueva variable que comparte la referencia a la del objeto original
 ```
11.	¿Cómo borrar un archivo dentro de Python?
``` 
Existen varias maneras de hacerlo, una de ellas es usar la función remove que recibe como argumento la ruta del archivo a eliminar. 
Ejemplo:
```
```
from os import remove
remove('D:\Documents\prueba\archivo.py')
```

12.	¿Qué es un "diccionario"? 
```
Es un conjunto de valores emparejados, al primero se le conoce como clave (key) y al segundo como valor (value), se crean utilizando corchetes {}, entre la clave y el valor se colocan (:), si la clave o el valor es un string se deben colocar entre comillas; otra manera de hacerlo es utilizando la palabra reservada dict.
```
13.	¿Es Python un lenguaje de programación interpretado? 
```
En efecto, así lo es, por consiguiente, necesita de un intérprete que lee el código y ejecuta instrucciones; enfocado a la legibilidad y facilidad de aprendizaje y uso
```
14.	¿Cómo Python se considera un lenguaje orientado a objetos?
```
 Lo es, dado que en Python todos los elementos del lenguaje son objetos, utiliza herencia, modularidad, polimorfismo, y encapsulamiento.
 ```
15.	¿Qué es “slicing"? 
```
La expresión hace referencia a la operación por medio de la cual se extraen elementos de una secuencia, tal como una lista o una cadena de caracteres
```
16.	Según la guía de estilos PEP8 ¿cómo deben escribirse las constantes?
```
Las constantes son generalmente definidas a nivel módulo, escritas con todas las letras en mayúscula y con guiones bajos separando palabras. Por ejemplo, MAX_OVERFLOW y TOTAL.
```
17.	¿Qué es virtualenv y como lo inicias con un interpretador de Python especifico?
```
 virtualenv es un programa que permite crear entornos virtuales de Python. Un entorno virtual consta de un intérprete (podemos elegir la versión concreta) acompañado de todos los módulos que necesitemos instalar para la ejecución de un proyecto. 
 ```
 ```
Para Python3 se crea así: 
	python3 -m venv ~/.virtualenv/nombre_espacio_virtual
para activarlo es así:
	source ~/.virtualenv/nombre_espacio_virtual/bin/activate
```
