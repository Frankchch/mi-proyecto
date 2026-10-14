# pipeline.py - Nuestro pipeline de datos básico

def extraer_datos():
    """Simula extraer datos de una fuente."""
    datos = [
        {"producto": "Laptop", "precio": 999, "cantidad": 5},
        {"producto": "Mouse", "precio": 29, "cantidad": 50},
        {"producto": "Teclado", "precio": 79, "cantidad": 30},
    ]
    return datos

def calcular_iva(precio, tasa=0.21):
    """Calcula el IVA de un precio."""
    return precio * tasa

def calcular_total(datos, con_iva=True):
    """Calcula el total de ventas, opcionalmente con IVA."""
    total = sum(item["precio"] * item["cantidad"] for item in datos)
    if con_iva:
        total += calcular_iva(total)
    return total

def aplicar_descuento(total, descuento=0.1):
    """Aplica un descuento al total."""
    if total > 10000:
        return total * (1 - descuento)
    return total

if __name__ == "__main__":
    datos = extraer_datos()
    total = aplicar_descuento(calcular_total(datos))
    print(f"Total de ventas (con IVA): {total:,.1f} €")