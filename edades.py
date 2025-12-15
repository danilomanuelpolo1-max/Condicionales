def obtener_categoria(edad: int) -> str:
    if 0 <= edad <= 5:
        rango_caso = "R1"
    elif 6 <= edad <= 10:
        rango_caso = "R2"
    elif 11 <= edad <= 15:
        rango_caso = "R3"
    elif 16 <= edad <= 18:
        rango_caso = "R4"
    elif 19 <= edad <= 25:
        rango_caso = "R5"
    elif 26 <= edad <= 40:
        rango_caso = "R6"
    elif 41 <= edad <= 55:
        rango_caso = "R7"
    elif edad >= 56:
        rango_caso = "R8"
    else:
        rango_caso = "No valido"

    match rango_caso:
        case "R1":
            return "Infante"
        case "R2":
            return "Niño"
        case "R3":
            return "Pre adolescente"
        case "R4":
            return "Adolescente"
        case "R5":
            return "Pre adulto"
        case "R6":
            return "Adulto"
        case "R7":
            return "Pre anciano"
        case "R8":
            return "Anciano"
        case _:
            return "Edad no válida o fuera de rango."

def main():
    while True:
        try:
            edad = int(input("Por favor, introduce la edad de la persona: "))
            if edad < 0:
                print("La edad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    categoria = obtener_categoria(edad)

    print("-" * 35)
    print(f"La edad introducida es: {edad} años.")
    print(f"La persona pertenece a la categoría: **{categoria}**")
    print("-" * 35)

if __name__ == "__main__":
    main()