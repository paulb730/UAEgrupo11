"""
En este archivo se concretará la venta se restara de stock el producto que se vende Paul
"""

from data_list import tipoproducto as TIPO
from data_list import Lista_Productos_Gifty as INVENTARIO
import random


def elegircat(case):
    CatList=list(TIPO.keys())

    if case=='1':
        print(f"Elegiste esta categoria: {CatList[0]}")
        return TIPO['Tecnologia']
    elif  case=='2':
        print(f"Elegiste esta categoria: {CatList[1]}")
        return TIPO['Ropa']
    elif  case=='3':
        print(f"Elegiste esta categoria: {CatList[2]}")
        return TIPO['Hogar']
    elif  case=='4':
        print(f"Elegiste esta categoria: {CatList[3]}")
        return TIPO['Alimentos']
    elif  case=='5':
        print(f"Elegiste esta categoria: {CatList[4]}")
        return TIPO['Automotriz']
    elif  case=='6':
        print(f"Elegiste esta categoria: {CatList[5]}")
        return TIPO['Salud']
    elif  case=='7':
        print(f"Elegiste esta categoria: {CatList[6]}")
        return TIPO['Libros']
    elif  case=='8':
        print(f"Elegiste esta categoria: {CatList[7]}")
        return TIPO['Juguetes']
    elif  case=='9':
        print(f"Elegiste esta categoria: {CatList[7]}")
        return TIPO['SinCategoria']
    else: 
        print("Su busqueda no coincide con ninguna categoria")                                  
def venta_simulada():
    print("****************Simulacion de Venta****************")
    if len(INVENTARIO)>0:
        for i in range(len(INVENTARIO)):
            if i==random.randint(0,len(INVENTARIO)):
                listcomprado=list(INVENTARIO[i])
                stocktemp=int(listcomprado[5])
                stocktemp-=1
                listcomprado[5]=str(stocktemp)
                INVENTARIO[i]=tuple(listcomprado)
                print("Usted a comprado un producto")
                break


    else:
        print("No existen productos en la Tienda Gifty")        
    

    


        





