def solicitar_datos():
    print("\n--- REGISTRO DE INVENTARIO---")

    nombre = ""
    while not nombre.strip(): # .strip() elimina espacios vacios para asegurar que haya un nombre [cite: 31, 38]
        nombre = input("Ingrese el nombre del producto: ")
        if not nombre.strip():
            print("Error: El nombre no puede estar vacio.")

    # Validacion de cantidad: no negativos y solo numeros [cite: 32, 39]
    cantidad = -1 
    while cantidad < 0:
        try:
            entrada = input(f"Ingrese la cantidad disponible de '{nombre}': ")
            cantidad = int(entrada)
            if cantidad < 0:
                print("Error: La cantidad no puede ser negativa. ")
        except ValueError:
            print("Error: Debe ingresar un numero entero valido")
            cantidad = -1
    return nombre, cantidad

def mostrar_resultado(nombre, estado):
    # .upper() pone el nombre en mayusculas para la salida [cite: 34]
    print("\n" + "=" * 35)
    print(f"PRODUCTO: {nombre.upper()}")
    print(f"ESTADO: {estado}")
    print("=" * 35)