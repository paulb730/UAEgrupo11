
""" 
Funciones base para el funcionamiento de la app  PAUL 
"""
"""Funciones administrar el inventario de la tienda"""
"""
1) Agregar productos: 
    definir agregar_producto
         Input de nombre, precio, descripcion, cantidad 
         guardar en una estructura de datos (diccionario)
         el ID sera generado automáticamente (puede ser un número secuencial)
         print (desea agregar otro producto?)
            si respuesta es si, repetir proceso de agregar producto
            si respuesta es no, salir del proceso de agregar producto
2) Actualizar productos:
    Definir actualizar_producto
        Input de ID del producto
        Si el producto existe
            Input de nombre, precio, descripcion, cantidad
            Actualizar la información del producto
            print (producto actualizado)
     
        En caso negativo, mostrar “Producto no encontrado”

3) Eliminar productos:
    Definir eliminar_producto
        Input de ID del producto
        Si el producto existe
            Eliminar el producto
            print (producto eliminado)
            print (desea eliminar otro producto?)   
                si respuesta es si, repetir proceso de eliminar producto
                si respuesta es no, salir del proceso de eliminar producto            
        En caso negativo, mostrar “Producto no encontrado”
        

"""
from data_list import Lista_Productos_Gifty as Inventario
from data_list import producto as prod
from data_list import tipoproducto as tipo
import random
from tabulate import tabulate

#Esta funcion despliega un menu de tipos de productos 
def tipoproductosmenu():
    
    print("\n" )
    
    lista=list(tipo.keys())
    for i in range(len(lista)):
        print(f"{i+1} {lista[i]} ")
#Esta funcion permite al usuario agregar un producto a un grupo definido
def elegirtipoproducto(case,prod:dict):
    lista=list(tipo.keys())
    
    cat=''
    if case=='1':
        cat=lista[0]
        prod['tipoproducto']=cat
        tipo['Tecnologia'].append(tuple([prod['codigo'],prod['nombre']]))
        
    elif case=='2':
        cat=lista[1]
        prod['tipoproducto']=cat
        tipo['Ropa'].append(tuple([prod['codigo'],prod['nombre']]))
        
    elif case=='3':
        cat=lista[2]
        prod['tipoproducto']=cat
        tipo['Hogar'].append(tuple([prod['codigo'],prod['nombre']]))
        
    elif case=='4':
        cat=lista[3]
        prod['tipoproducto']=cat
        tipo['Alimentos'].append(tuple([prod['codigo'],prod['nombre']]))
        
    elif case=='5':
        cat=lista[4]
        prod['tipoproducto']=cat
        tipo['Automotirz'].append(tuple([prod['codigo'],prod['nombre']]))
        
    elif case=='6':
        cat=lista[5]
        prod['tipoproducto']=cat
        tipo['Salud'].append(tuple([prod['codigo'],prod['nombre']]))
        
    elif case=='7':
        cat=lista[6]
        prod['tipoproducto']=cat
        tipo['Libros'].append(tuple([prod['codigo'],prod['nombre']]))
        
    elif case=='8':
        cat=lista[7]
        prod['tipoproducto']=cat
        tipo['Juguetes'].append(tuple([prod['codigo'],prod['nombre']]))
        
    else:
        print("Su Producto no se ha agregado a ninguna categoria")
        cat=lista[8]
        prod['tipoproducto']=cat
        tipo['SinCategoria'].append(tuple([prod['codigo'],prod['nombre']]))
    
    return cat    
#Esta funcion genera un codigo para cada producto
def generar_codigo(nombre:str):
    numbers = list(range(0, 1001))  # Lista de números del 0 al 1000
    random.shuffle(numbers)  # Mezclar la lista
    unique_number = numbers.pop()  # Tomar un número sin repetir
    posicion=str(unique_number)
    list_random=['A','B','C','D','E','F','G','H','I','J','K']
    #este metodo toma los tres primeras letras del nombre creado
    if len(nombre)!=0:
        if len (nombre)>=3:
            res=''.join(nombre[i] for i in range(3))
        elif len (nombre)<3:
            res=''.join(nombre[i] for i in range(len(nombre)))
    else:
        print("Su producto no tiene nombre no se generará un código")
    #Los codigos son la concatenacion de su posicion en la lista y un caracter + los tres primeras letras del nombre 
    codigo= posicion+str(random.choice(list_random))+res   
    return codigo
#Esta Funcion agrega un producto al inventario
def agregarproducto(prod:dict):
    #Agregar producto
    productofinal=tuple(prod.values())
    Inventario.append(productofinal)   
#Esta funcion registra todos los campos del producto inventario
def digitarproductos():
    print("****************Módulo Agregar Productos****************")
    #Pedir al usuario los datos del producto Nombre, Descripción, Precio, Stock
    nombre=input("Ingrese el Nombre del Producto: ")
    desc=input("Ingrese la descripción del Producto: ")
    precio=input("Ingrese el precio del producto: ")
    stock=input("Ingrese la cantidad disponible en bodega (Stock): ")
    #Agregar los nuevos datos al objeto diccionario que es el producto
    prod['nombre']=nombre
    prod['descripción']=desc
    prod['precio']=precio
    prod['stock']=stock
    print("Estamos validando sus datos")
    #Aqui agrgeo el codigo al campo codigo del producto
    prod['codigo']=generar_codigo(nombre)
    print("\n Ahora desea agregar su producto a una categoria:" )
    agregar=input( "Digite 1 para Si y 0 Para NO ")
    if agregar=='1':
         #Añadir producto a un grupo
        print("Estas son las opciones para agregar producto:")
        tipoproductosmenu()
        tipoproducto=input("Elige una categoria (solo digite el numero que corresponde): ")
        cat=elegirtipoproducto(tipoproducto,prod)
        print(f"Su producto se agrego exitosamente a la categoria {cat}") 
        print("Su Producto agregado es el siguiente: ", prod)
    elif agregar=='0':
        cat=elegirtipoproducto('tipoproducto',prod)
        print("Su producto no tendrá categoria")
        print("Su Producto agregado es el siguiente: ", prod)
    return prod;    
#esta funcion es la agregacion final que se pondrá en el menu 
def agregar():
    flag=True
    while flag:
        prodtemp=digitarproductos()
        agregarproducto(prodtemp)
        seguir=input("Desea agregar otro producto 1 Si 0 No ")
        if seguir=='1':
            flag=True
        elif seguir=='0':
            flag=False
            break
        else:
            print("Ingrese 1 para Si  o 0 para No: ")
            break
    print("\nINVENTARIO", tabulate(Inventario[0:100],headers=tuple(prod.keys()),tablefmt="grid"))
    print("PRODUCTOS POR CATEGORIA",tabulate(tipo,headers=tuple(tipo.keys()),tablefmt="grid"))

#LLamado de la funcion para probar 
#agregar()

    



    


     

   
         
    

def consultarproductos():
    return 0

def actualizarproductos():
    return 0

def eliminarproductos():
    return 0


