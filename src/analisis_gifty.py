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
from core_gifty import actualizar
from core_gifty import eliminar
from core_gifty import consultar
from venta_simulada import venta_simulada as venta
from control_stock import stockcritico,verInventario,reportes


def menu():
    print("****************Bienvenido al sistema de control de inventario GYFTY****************")
    print("Seleccione una de las siguientes opciones:")
    print("1) Agregar producto ****************")#Listo
    print("2) Actualizar producto ****************")#Listo
    print("3) Eliminar producto ****************")#Listo
    print("4) Buscar productos ****************")#Listo
    print("5) Venta ****************")#Listo
    print("6) Control de Stock critico ****************")#Listo
    print("7) Ver Inventario ****************")#Listo
    print("8) Reportes ****************")#Listo
    print("9) Salir ****************")#Listo
    


def main():
  while True:
    menu()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
      agregar() 
    elif opcion == "2":
      actualizar()
    elif opcion == "3":
      eliminar()
    elif opcion == "4":
      consultar()
    elif opcion == "5":
      venta()
    elif opcion == "6":
      stockcritico()
    elif opcion == "7":
      verInventario()
    elif opcion == "8":
      reportes()
    elif opcion == "9":
      print("Hasta pronto")
      break
    else:
        print("Opción no valida")
    
  