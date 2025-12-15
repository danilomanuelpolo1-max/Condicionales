SMMLV = 1423500
AUXILIO_TRANSPORTE = 200000
LIMITE_AUXILIO = SMMLV * 2
LIMITE_RETENCION_ALIMENTOS = 3740000
VALOR_HORA_ORDINARIA = 6471
valor_hora_extra_diurna = 8088
HORAS_SEMANALES_ORDINARIAS = 48
FACTOR_MENSUAL_NOMINA = 4.33
PORCENTAJE_EMI = 0.03
PORCENTAJE_FUNERARIA = 0.02
PORCENTAJE_RETENCION_ALIMENTOS = 0.30

continuar = 1

while continuar != 0:
    print("\n" + "=" *50)
    print("        INICIO CALCULO DE NOMINA")
    print("=" *50)

    print("--- Ingreso de Datos Variables ---")
    horas_extra_diurnas = float(input("Ingrese las horas extra diurnas trabajadas en el mes: "))
    valor_deduccion_fondo = float(input("Ingrese el valor por aportes al fondo de empleados: "))
    valor_demanda_alimentos = float(input("Ingrese el valor fijo mensual de la demanda por alimentos (si aplica, sino ponga 0): "))

    salario_basico_mensual = HORAS_SEMANALES_ORDINARIAS * VALOR_HORA_ORDINARIA * FACTOR_MENSUAL_NOMINA
    total_horas_extra = horas_extra_diurnas * valor_hora_extra_diurna
    salario_bruto_sin_auxilio = salario_basico_mensual + total_horas_extra

    if salario_bruto_sin_auxilio < LIMITE_AUXILIO:
        auxilio_transporte_a_pagar = AUXILIO_TRANSPORTE
    else:
        auxilio_transporte_a_pagar = 0

    salario_bruto_total = salario_bruto_sin_auxilio + auxilio_transporte_a_pagar

    deduccion_emi = salario_bruto_sin_auxilio * PORCENTAJE_EMI
    deduccion_funeraria = salario_bruto_sin_auxilio * PORCENTAJE_FUNERARIA
    deduccion_fondo_empleados = valor_deduccion_fondo
    deduccion_alimentos = valor_demanda_alimentos

    if salario_bruto_sin_auxilio > LIMITE_RETENCION_ALIMENTOS:
        retencion_alimentos_especial = salario_bruto_sin_auxilio * PORCENTAJE_RETENCION_ALIMENTOS
        deduccion_alimentos = retencion_alimentos_especial

    total_deducciones = deduccion_emi + deduccion_funeraria + deduccion_fondo_empleados + deduccion_alimentos
    salario_neto = salario_bruto_total - total_deducciones

    print("\n" + "="*50)
    print("## Resumen del Cálculo de Nómina Mensual")
    print("="*50)
    print(f"\nSalario Bruto Mensual (Base de Cálculos): ${salario_bruto_sin_auxilio:,.2f}")
    print(f"Auxilio de Transporte: ${auxilio_transporte_a_pagar:,.2f}")
    print(f"Salario Bruto Total (Con Auxilio): ${salario_bruto_total:,.2f}")

    print("\n--- Deducciones ---")
    print(f"Deducción EMI (3%): ${deduccion_emi:,.2f}")
    print(f"Deducción Funeraria (2%): ${deduccion_funeraria:,.2f}")
    print(f"Aporte Fondo de Empleados: ${deduccion_fondo_empleados:,.2f}")
    print(f"Retención por Demanda de Alimentos: ${deduccion_alimentos:,.2f}")
    print(f"**TOTAL DEDUCCIONES:** ${total_deducciones:,.2f}")

    print("\n" + "=" *50)
    print(f"## VALOR NETO A PAGAR AL TRABAJADOR: ${salario_neto:,.2f}")
    print("=" *50)

    print("\n--- Control de Ciclo ---")
    continuar = int(input("Para calcular la nómina de otro trabajador ingrese cualquier número diferente de 0. Para TERMINAR ingrese 0: "))

    
print("\n Fin del Algoritmo")