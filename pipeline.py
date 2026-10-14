# pipeline.py - Nuestro pipeline de datos básico

def extraer_datos():
    """Simula extraer datos de una fuente."""
    datos = [
        {"producto": "Laptop", "precio": 999, "cantidad": 5},
        {"producto": "Mouse", "precio": 29, "cantidad": 50},
        {"producto": "Teclado", "precio": 79, "cantidad": 30},
    ]
    return datos

def calcular_total(datos):
    """Calcula el total de ventas."""
    total = sum(item["precio"] * item["cantidad"] for item in datos)
    return total

if __name__ == "__main__":
    datos = extraer_datos()
    total = calcular_total(datos)
    print(f"Total de ventas: {total:,.2f} €")