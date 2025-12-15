id_sucursal = "S001"
fecha_actual = "25/11/2025"

print("--- MÁQUINA DISPENSADORA DE TICKETS ---")

respuesta_continuar = input("¿Desea continuar con la operación? (si/no): ").lower()

if respuesta_continuar == 'si':
    print("\n--- INGRESO DE DATOS ---")
    cedula_usuario = input("Ingrese su número de cédula: ")
    nombre_usuario = input("Ingrese su nombre: ")

    print("\n--- MENÚ DE SERVICIOS ---")
    print("1. Servicio de Caja")
    print("2. Servicio al Cliente")
    print("3. Pago de Impuestos")
    print("4. Crédito Hipotecario")
    print("5. Operaciones con Tarjeta de Crédito")
    print("----------------------------")
    
    try:
        opcion_elegida = int(input("Seleccione una opción (1-5): "))
    except ValueError:
        print("\nALERTA: La entrada no es un número válido. Transacción cancelada.")
    
    servicio_seleccionado = ""
    
    if opcion_elegida == 1:
        servicio_seleccionado = "CAJA"
        
    elif opcion_elegida == 2:
        servicio_seleccionado = "SERVICIO AL CLIENTE"
        
    elif opcion_elegida == 3:
        servicio_seleccionado = "PAGO DE IMPUESTOS"
        
    elif opcion_elegida == 4:
        servicio_seleccionado = "CRÉDITO HIPOTECARIO"
        
    elif opcion_elegida == 5:
        servicio_seleccionado = "TARJETA DE CRÉDITO"
        
    else:
        print("\nALERTA: Opción no válida. Transacción CANCELADA/INVALIDADA.")
        
    if servicio_seleccionado != "":
        consecutivo_ticket = 789
        
        print("\n" + "="*40)
        print("         TICKET GENERADO")
        print("="*40)
        
        print(f"Sucursal ID: **{id_sucursal}**")
        print(f"Fecha: **{fecha_actual}**")
        print("-" * 40)
        print(f"Cliente: **{nombre_usuario}**")
        print(f"Cédula: **{cedula_usuario}**")
        print(f"Servicio: **{servicio_seleccionado}**")
        print(f"Ticket No.: **{consecutivo_ticket}**")
        print("\nDiríjase al área de:", servicio_seleccionado)
        print("="*40)
        
elif respuesta_continuar == 'no':
    print("\nSistema cancela la transacción. ¡Hasta pronto!")

else:
    print("\nRespuesta no reconocida. Transacción cancelada.")