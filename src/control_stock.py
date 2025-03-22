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



