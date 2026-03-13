LIMITE_MINIMO = 10
def verificar_estado(cantidad):
    """
    Logica del sistema: compara la cantidad con el limite minimmo.
    Regla: Si cantidad >= 10 es suficiente, si no, reabastecer[cite: 41, 42].
    """
    if cantidad >= LIMITE_MINIMO:
        return "Hay suficiente inventario" 
    else:
        return "Se debe reabastecer el producto"