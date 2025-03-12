"""_summary_
     La tienda de venta de artículos de regalo “gifty”, lleva su control de inventario a través de hojas
de Excel, registrando las entradas de artículos y salidas de cada uno cada vez que se vende un
artículo. Ustedes como equipo de desarrolladores de software en Python deben desarrollar un
sistema sencillo de gestión de inventario. El sistema permitirá a los usuarios administrar el
inventario de la tienda, utilizando los conceptos aprendidos en las cuatro unidades del
diplomado en Python, incluyendo el uso de variables, estructuras de control de flujo, funciones
y módulos, y estructuras de datos.

"""
"""Funciones administrar el inventario de la tienda"""
import time
def atrapartuplas(tupla:tuple):
    listadetuplas=[]
    noson=[]
    for i in range(len(tupla)):
        print("loading...") 
        if str(type(tupla[i]).__name__)=="tuple":
            for j in tupla[i]:
                listadetuplas.append(j)
                time.sleep(0.1)
        if str(type(tupla[i]).__name__)!="tuple":
            noson.append(tupla[i])
               
    print(f"Los elementos que estan dentro de  tuplas son  {listadetuplas} y los que no son {noson}")   
         
tupla=[(1,"pivot","a","b","asd"),2,("asdasd","dos",[12,13]),"a","c",(3,1,2,"tupla"),("1",1,"0","0",0),[1,2,7,10]]

atrapartuplas(tupla)
            
print("hola mundo")

"""

"""

""" Aqui solo se ejecuta el metodo main como JAVA  """


