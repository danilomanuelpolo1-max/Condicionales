import math

print("--- TEST DE CAPACITACIÓN ---")

try:
    total_preguntas = int(input("Ingrese la cantidad total de preguntas realizadas: "))
    
    if total_preguntas <= 0:
        print("\nERROR: La cantidad de preguntas debe ser un número positivo.")
    else:
        respuestas_correctas = math.ceil(total_preguntas * 0.70)
        
        if respuestas_correctas > total_preguntas:
            respuestas_correctas = total_preguntas

        porcentaje_correcto = (respuestas_correctas / total_preguntas) * 100

        nivel = ""
        mensaje = ""

        if porcentaje_correcto >= 90:
            nivel = "Nivel máximo"
            mensaje = "Felicidades! Ha demostrado un conocimiento excepcional."
            
        elif porcentaje_correcto >= 75 and porcentaje_correcto < 90:
            nivel = "Nivel medio"
            mensaje = "Buen trabajo. Su desempeño es superior al promedio."
            
        elif porcentaje_correcto >= 50 and porcentaje_correcto < 75:
            nivel = "Nivel regular"
            mensaje = "Necesita reforzar algunos temas. Su desempeño es regular."
            
        else:
            nivel = "Fuera de nivel"
            mensaje = "Debe capacitarse intensivamente. No cumple con el nivel mínimo requerido."

        print("\n" + "="*40)
        print("          RESULTADOS DEL TEST")
        print("="*40)
        print(f"Total de preguntas: **{total_preguntas}**")
        print(f"Respuestas correctas: **{respuestas_correctas}**")
        print("-" * 40)
        print(f"Porcentaje Obtenido: **{porcentaje_correcto:.2f}%**")
        print(f"Nivel Alcanzado: **{nivel}**")
        print(f"Mensaje: {mensaje}")
        print("="*40)

except ValueError:
    print("\nERROR: La entrada para la cantidad de preguntas debe ser un número entero.")