"""
Este archivo se encarga de configurar la estructura de datos general la lista de todos los productos Paul

"""
Lista_Productos_Gifty:list=[]

"""
Copia de la lista 
"""


Lista_Productos_Gifty_BP:list=Lista_Productos_Gifty[:]

"""
Estructura de producto
El Código se generara automaticamente
El ID dependera de su posicion en la lista + codigo generado 
Tipo de producto se genera dependiendo su nombre 
Ejemplo: telefono=movil
"""

tipoproducto={
    "Tecnologia":[],
    "Ropa":[],
    "Hogar":[],
    "Alimentos":[],
    "Automotirz":[],
    "Salud":[],
    "Libros":[],
    "Juguetes":[],
    "SinCategoria":[]
}



producto={
    "codigo":'',
    "nombre":"",
    "descripción":"",
    "tipoproducto":"",
    "precio":0,
    "stock":0,
   }



