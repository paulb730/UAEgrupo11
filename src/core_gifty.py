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
import importlib.util
import re
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
    if prod is not None:
        #Agregar producto
        productofinal=tuple(prod.values())
        Inventario.append(productofinal) 
#Contiene letras 
def contieneletras(expresion:str):
    return any(i.isalpha() for i in expresion)
#Contiene numeros
def contienenumeros(expression:str):
    return bool(re.fullmatch(r"\d+(\.\d+)?", expression))
#Contiene solo numeros enteros
def contienenumerosint(expression:str):
    return expression.isdigit()
#imprimir data como tablas data obtenemos la informacion y prod obtenemos los headers
#imprime diccionarios y tuplas
def imprimirtablas(data,prod,cant):
    if existe_este_paquete("tabulate"): 
        from tabulate import tabulate
        if isinstance(data,list):
            return print("\nINVENTARIO", tabulate(data[0:cant],headers=tuple(prod.keys()),tablefmt="grid"))
        elif isinstance(data,dict):
            return print("\nPRODUCTOS POR CATEGORIA",tabulate(data,headers=tuple(prod.keys()),tablefmt="grid")) 
    else: 
        return print(data)    
#Esta funcion permite saber si el paquete externo ha sido instalado en un entorno de python
def existe_este_paquete(nombrepaquete):
    return importlib.util.find_spec(nombrepaquete) is not None
#Esta funcion registra todos los campos del producto inventario
def digitarproductos():
    print("****************Módulo Agregar Productos****************")
    #Pedir al usuario los datos del producto Nombre, Descripción, Precio, Stock
    flag:bool=True   
    estaduplicado:bool=False
    while flag:
        nombre=input("Ingrese el Nombre del Producto: ") 
        if nombre!='':
            if contieneletras(nombre):
                break
            else:
                print("El nombre debe contener al menos una letra")
        else:
            print("El nombre no puede ser vacio")
   
                
    while flag:
        desc=input("Ingrese la descripción del Producto: ")
        if desc!='':
            if contieneletras(desc):
                break
            else: 
                print("la descripcion al menos debe tener una letra")
        else:
            print("Se recomienda poner una descripcion el campo esta vacio")
    while flag:
        precio=input("Ingrese el precio del producto: ")
        if precio!='':
            if  contienenumeros(precio):
                if precio !='0':
                    break
                else:
                    print("El precio no puede ser cero")
            else:
                print("El precio debe ser numérico ")       
        else:
            print("El precio no puede ser vacio")
    while flag:
        stock=input("Ingrese la cantidad disponible en bodega (Stock): ")
        if stock!='':
            if contienenumerosint(stock):
                if stock!='0':
                    break
                else: 
                    print("El stock no puede ser cero")    
            else: 
                print("El stock debe ser un numero entero")
        else:
            print("El stock no puede ser vacio")        
    if len(Inventario)>0:
        for i in range(len(Inventario)):
            item=Inventario[i]
            if nombre==item[1]:
                print("Parece que agregaste un producto ya agregado anteriormente, se actualizara el stock, precio y descripcion") 
                estaduplicado=True
                              

    if estaduplicado==False:
        #Agregar los nuevos datos al objeto diccionario que es el producto
        prod['nombre']=nombre
        prod['descripción']=desc
        prod['precio']=precio
        prod['stock']=stock
        print("Estamos validando sus datos")
        #Aqui agrgeo el codigo al campo codigo del producto
        prod['codigo']=generar_codigo(nombre)
        print("\n Ahora desea agregar su producto a una categoria:" )
        while flag:
            agregar=input( "Digite 1 para Si y 0 Para NO ")
            if agregar=='1':
                #Añadir producto a un grupo
                print("Estas son las opciones para agregar producto:")
                tipoproductosmenu()
                tipoproducto=input("Elige una categoria (solo digite el numero que corresponde): ")
                cat=elegirtipoproducto(tipoproducto,prod)
                print(f"Su producto se agrego exitosamente a la categoria {cat}") 
                print("Su Producto agregado es el siguiente: ", prod)
                break
            elif agregar=='0':
                cat=elegirtipoproducto('tipoproducto',prod)
                print("Su producto no tendrá categoria")
                print("Su Producto agregado es el siguiente: ", prod)
                break
            else:
                print("Elija entre 1 o 0")
        return prod;        
    else:
        for i in range(len(Inventario)):
            item=Inventario[i]
            if nombre==item[1]:
                
                #transformo la tupla en lista para poder editarlo
                listatemp=list(item)
                listatemp[2]=desc
                listatemp[4]=precio

                oldstock=int(listatemp[5])
                oldstock+=int(stock)
                listatemp[5]=oldstock
                Inventario[i]=tuple(listatemp)
                print("producto actualizado",Inventario[i])
            #actualizo la tupla con los nuevos resultados
# La busqueda la realiza el usuario por nombre por cantidad por descripcion y por categoria 
def consultarproductos():
    while True:
        print("\n Tipos de Consultas disponibles:")
        tiposconsultas=[' Por Nombre','Por Descripción','Por Categoria','Por stock','Salir']
        buscado=''
        for i in range(len(tiposconsultas)):
            print(f"{i+1} {tiposconsultas[i]} ")
        case=input("Ingrese el tipo de consulta que quiera hacer (solo ingrese el numero): ")
        if case=='1':
            print(f"Ha elegido {tiposconsultas[0]}")
            value=input("Ahora ingrese un nombre a consultar: ")
            buscado=[item for item in Inventario if bool(re.search(value,item[1],re.IGNORECASE))]
            print("Este es el elemento buscado")
            return buscado
        elif case=='2':
            print(f"Ha elegido {tiposconsultas[1]}")
            value=input("Ahora ingrese un descripcion a consultar: ")
            buscado=[item for item in Inventario if bool(re.search(value,item[2],re.IGNORECASE))]
            print("Este es el elemento buscado")          
            return buscado
        elif case=='3':
            print(f"Ha elegido {tiposconsultas[2]}")
            print("Estas son las categorias disponibles en GIFTY")
            listtempcat=list(tipo.keys())
            for i in range(len(listtempcat)):
                print(f"{i+1} {listtempcat[i]} ")
            try:    
                value=int(input("Ahora elija una categoria a consultar (solo digite el numero)"))
            except (ValueError) as e:
                print(f"no es un numero {e}")
            buscado=[item for item in Inventario if bool(re.search(listtempcat[value-1],item[3]))]
            print(f"Los elementos de la categoria: {listtempcat[value-1]} son:")
            return buscado
        elif case=='4':
            print(f"Ha elegido {tiposconsultas[3]}")
            value=input("Ahora ingrese una cantidad a consultar en stock")
            buscado=[item for item in Inventario if bool(re.search(value,item[5],re.IGNORECASE)) ]
            print(f"Este es el elemento buscado")
            return buscado
        elif case=='5': 
            print("Saliendo")
            break
        else:
            print("no ha elegido ningun tema para consultar")
#esta funcion es la agregacion final que se pondrá en el menu 
def agregar():
    flag=True
    while flag:
        prodtemp=digitarproductos()
        agregarproducto(prodtemp)
        while flag:
            seguir=input("Desea agregar otro producto 1 Si 0 No ")
            if seguir=='1':
                flag=True
                break
            elif seguir=='0':
                flag=False
                break
            else:
                print("Ingrese 1 para Si  o 0 para No: ")
            
    #imprimirtablas(Inventario,prod,100)
    imprimirtablas(Inventario,prod,100)
    imprimirtablas(tipo,tipo,100)
    #print("\nINVENTARIO", tabulate(Inventario[0:100],headers=tuple(prod.keys()),tablefmt="grid"))
    #print("PRODUCTOS POR CATEGORIA",tabulate(tipo,headers=tuple(tipo.keys()),tablefmt="grid"))
def actualizarproductos():
    print("****************Módulo Actualizar Productos****************")
    actualizarlist=consultarproductos()
    print(actualizarlist)
    print("El codigo y categoria no se puede editar")
    flag:bool=True
    oldstock:int=0
    for i in range(len(Inventario)):

        for item in actualizarlist:
            
            print(f"\nEste elemento: {item} se actualizara")
            while flag:
                nombre=input("Ingrese el Nombre del Producto: ") 
                if nombre!='':
                    if contieneletras(nombre):
                        break
                    else:
                        print("El nombre debe contener al menos una letra")
                else:
                    print("El nombre no puede ser vacio")
            while flag:
                desc=input("Ingrese la descripción del Producto: ")
                if desc!='':
                    if contieneletras(desc):
                        break
                    else: 
                        print("la descripcion al menos debe tener una letra")
                else:
                    print("Se recomienda poner una descripcion el campo esta vacio")
            while flag:
                precio=input("Ingrese el precio del producto: ")
                if precio!='':
                    if  contienenumeros(precio):
                        if precio !='0':
                            break
                        else:
                            print("El precio no puede ser cero")
                    else:
                        print("El precio debe ser numérico ")       
                else:
                    print("El precio no puede ser vacio")
            while flag:
                stock=input("Ingrese la cantidad disponible en bodega (Stock): ")
                if stock!='':
                    if contienenumerosint(stock):
                        if stock!='0':
                            break
                        else: 
                            print("El stock no puede ser cero")    
                    else: 
                        print("El stock debe ser un numero entero")
                else:
                    print("El stock no puede ser vacio")      
        #Transformo tupla a lista a editarla 
            listtemp=list(item)
            listtemp[1]=nombre
            listtemp[2]=desc
            listtemp[4]=precio
            oldstock=int(listtemp[5])
            oldstock+=int(stock)
            listtemp[5]=str(oldstock)
            Inventario[i]=tuple(listtemp)
            break
        imprimirtablas(Inventario,prod,100)
        break
def eliminarproductos():
    print("****************Módulo Eliminar Productos****************")
    #primero llamar a consultar que producto deseaeliminar
    #primero hay que consultar el producto a eliminar 
    eliminarlist=consultarproductos()
    print(eliminarlist)
    for item in eliminarlist:
        print(f"\nEste elemento: {item} se eliminara")
        try:
            Inventario.remove(item)
            print("Se eliminara solo el primer elemento encontrado")
            imprimirtablas(Inventario,prod,100)
                
        except ValueError:
            print(f"Error: {item} no fue encontrado en el inventario") 

#LLamado de la funcion para probar 
agregar()
consultarproductos()
actualizarproductos()
eliminarproductos()
#agregar()

    



    


     

   
         
    

def consultarproductos():
    return 0

def actualizarproductos():
    return 0

def eliminarproductos():
    return 0


