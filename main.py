from view import solicitar_datos, mostrar_resultado
from database import verificar_estado

def ejecutar_sistema():
    # 1. Entrada [cite: 25, 26]
    nombre_producto, cantidad_disponible = solicitar_datos()
    
    # 2. Proceso (Lógica de comparación) [cite: 27, 41, 42]
    estado_inventario = verificar_estado(cantidad_disponible)
    
    # 3. Salida [cite: 28, 46]
    mostrar_resultado(nombre_producto, estado_inventario)

if __name__ == "__main__":
    ejecutar_sistema()