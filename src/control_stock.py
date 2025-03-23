"""
tres siguientes funciones Isai

1 controlstock
2 generar reportes 

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

from data_list import Lista_Productos_Gifty as INVENTARIO
from core_gifty import imprimirtablas
from data_list import producto as prod
from data_list import tipoproducto as TIPO



def stockmaximo():
    
    listamaximos=[]
    if len(INVENTARIO)>0:
        for i in range(len(INVENTARIO)):
            temp=INVENTARIO[i]
            if int(temp[5])>300:
                listamaximos.append(INVENTARIO[i])
               
                imprimirtablas(listamaximos,prod,1000)
                
    else:
        print("Tu inventario no tiene productos")    
def stockcritico():
    
    listacritcos=[]
    if len(INVENTARIO)>0:
        for i in range(len(INVENTARIO)):
            temp=INVENTARIO[i]

            if int(temp[5])<5:
                listacritcos.append(INVENTARIO[i])
                
                imprimirtablas(listacritcos,prod,1000)
                
    else:
        print("Tu inventario no tiene productos")            
def verInventario():
    imprimirtablas(INVENTARIO,prod,100)
def reportes():
    print("****************Reportes Generales****************")
    print("****************Inventario****************")
    imprimirtablas(INVENTARIO,prod,100)
    
    print("****************Productos Por Categoría****************")
    imprimirtablas(TIPO,TIPO,100)
   
    print("****************Stock Critico****************")
    stockcritico()
   
    print("****************Stock Maximo****************")
    stockmaximo()
    
    
