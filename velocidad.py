import random

def verificar_velocidad():
    restricciones = {
        "Zonas Escolares": 30,
        "Vías Urbanas": 60,
        "Vías Rurales": 80,
        "Rutas Nacionales": 100
    }
    
    zonas = list(restricciones.keys())
    
    zona_actual = random.choice(zonas)
    
    limite_velocidad_ideal = restricciones[zona_actual]
    
    velocidad_x_raw = random.uniform(20.0, 120.0) 
    
    velocidad_x = round(velocidad_x_raw)
    velocidad_x_formateada = f"{velocidad_x:.1f}"
    
    velocidad_actual = float(velocidad_x_formateada)

    infraccion = ""
    
    if velocidad_actual > limite_velocidad_ideal:
        infraccion = "SÍ"
        mensaje_infraccion = " ¡Alerta de Infracción! Estás excediendo el límite."
    else:
        infraccion = "NO"
        mensaje_infraccion = " Límite de velocidad respetado."
    
    print("--- 🛣️ Reporte de Velocidad ---")
    print(f"**Zona Determinada (Restricción):** {zona_actual}")
    print(f"**Velocidad X Generada (Actual):** {velocidad_actual} KM/H")
    print(f"**Velocidad Ideal (Límite):** {limite_velocidad_ideal} KM/H")
    print(f"**¿Infringiendo los Límites?** {infraccion}")
    print(mensaje_infraccion)
    print("-------------------------------")

verificar_velocidad()