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

            
print("hola mundo")

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

"""
tres sieguientes funciones Cami:
    
   3) Visualización inventario:
        Definir mostrar inventario
            Print mostar inventario tabulado, enunciados
            
            IDEA DE CÓDIGO:
                def mostrar_inventario():
                    if not inventario:
                        print("El inventario está vacío.")
                        return
                    for codigo, info in inventario():
                        print
                (tabulate(inventario, headers="keys", tablefmt="grid"))
            
   4) Busqueda de producto
        Definir buscar_producto
            Variable inventario
            Busqueda = input de “ingresar ID o nombre del producto”
            Para el código (o ID) en el inventario
            Si la Búsqueda del código o búsqueda de nombre 
                Mostrar el detalle asociado al producto (Id, nombre, precio, cantidad)
            En caso negativo, mostrar “ Producto no encontrado”
            
    5) Control de stock
        Definir control_stock_crítico
            Variable inventario
            Para el código (o ID) en el inventario
                Si la cantidad es menor a 10
                    Mostrar alerta del producto: "nombre" "tiene bajo stock"
                    
                IDEA DE CÓDIGO:
                    def control_stock_critico():
                        inventario = cargar_inventario()
                        for codigo, info in inventario():
                            if info["cantidad"] < 10:
                                print(f"ALERTA: El producto '{info['nombre']}' tiene bajo stock ({info['cantidad']} unidades).")

""" 


"""
tres sieguientes funciones Marco

"""






