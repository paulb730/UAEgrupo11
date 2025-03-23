"""
tres  funciones Marco:
* Menú:  while > bucle / if  elif  else > opciones
  a)	Agregar producto
* b)	Actualizar producto
  c)	Eliminar producto
  d)	Ver inventario
  e)	Buscar productos
  f)	Control de Stock critico
  g)	Crear reporte
  h)	Salir: rompe el bucle
* i)      Salida producto
*
""" 

from core_gifty import agregar


def menu():
    print("Bienvenido al sistema de control de inventario GYFTY")
    print("Seleccione una de las siguientes opciones:")
    print("1) Agregar producto")
    print("2) Actualizar producto")
    print("3) Eliminar producto")
    print("4) Ver inventario")
    print("5) Buscar productos")
    print("6) Control de Stock critico")
    print("7) Crear reporte")
    print("9) Salir")
    print("10) Salida producto")
    
def actualizar():
    codigo = input("Ingrese el código del producto a actualizar: ")
    # Buscar el producto en el inventario
    for codigo, info in inventario():
        if codigo == codigo:
            print("Producto encontrado")
            print(f"Nombre: {info['nombre']}")
            print(f"Cantidad: {info['cantidad']}")
            print(f"Precio: {info['precio']}")
            print(f"Descripción: {info['descripcion']}")
            break
        
    # Si no existe, mostrar mensaje de error
        else:
          print("Producto no encontrado")
    # Si existe, mostrar los datos actuales del producto
    # Solicitar los nuevos datos del producto
    # Actualizar los datos del producto
    # Guardar el inventario actualizado


while True:
    menu()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
      agregar() 
    elif opcion == "2":
      actualizar()
    elif opcion == "3":
      pass
    elif opcion == "4":
      pass
    elif opcion == "5":
      pass
    elif opcion == "6":
      pass
    elif opcion == "7":
      pass
    elif opcion == "8":
      pass
    elif opcion == "9":
      print("Hasta pronto")
      break
    elif opcion == "10":
      pass
    else:
        print("Opción no valida")
    
  