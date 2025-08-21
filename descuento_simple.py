def aplicar_descuento(precio, descuento):
    return precio - (precio * descuento / 100)

# Solicitar datos al usuario
precio = float(input("Ingrese el precio: "))
descuento = float(input("Ingrese el descuento (%): "))

# Calcular y mostrar resultado
precio_final = aplicar_descuento(precio, descuento)
print("El precio final con descuento es:", precio_final)
