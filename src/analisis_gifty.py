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

#from core_gifty import fx



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
    

while True:
    menu()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
      agregar() 
    elif opcion == "2":
      pass
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
    else:
        print("Opción no valida")
    
  