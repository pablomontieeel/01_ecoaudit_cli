from calculadora import estimar_consumo_wh, calcular_huella_co2

while True:
    print("\n=========================================")
    print(" 🌿 ECOAUDIT CLI - MENÚ PRINCIPAL 🌿 ")
    print("=========================================")
    print("1. Realizar nueva auditoría")
    print("2. Consultar histórico")
    print("3. Salir")
    
    entrada = input("\nSeleccione una opción (1-3): ").strip()
    
    try:
        opcion = int(entrada)
    except ValueError:
        print("⚠️ Error: Debe introducir un número entero.")
        continue
    
    if opcion == 1:
        print("\n--- AUDITORÍA ENERGÉTICA ---")
        equipo_auditor = input("Nombre del equipo auditor: ").strip()
        potencia = float(input("Potencia consumida en Vatios (W): "))
        horas = float(input("Horas de uso diario: "))
        iteraciones_str = input("Número de iteraciones: ").strip()
        if horas <0 and int(iteraciones_str) <= 0:
            print("⚠️ Error: Las horas de uso y el número de iteraciones deben ser mayores que 0.")
        elif horas <0 or  horas >= 24:
            print("⚠️ Error: Las horas de uso deben ser mayores que 0 y menores o iguales que 24.")
        elif int(iteraciones_str) <= 0:
            print("⚠️ Error: El número de iteraciones debe ser mayor que 0.")
        
        else:
            print("Las horas de uso y el número de iteraciones son válidas. Continuando con la auditoría...")
            try:
                iteraciones = int(iteraciones_str)
            except ValueError:
                print("⚠️ Error: Debe introducir un número entero.")
                continue   
    
            print("El número de iteraciones es válido. Continuando con la auditoría...")
            consumo = estimar_consumo_wh(potencia, horas, iteraciones)    
            huella_co2 = calcular_huella_co2(consumo)

            print(f"\n✅ Resultados calculados para '{equipo_auditor}':")
            print(f"   • Consumo total: {consumo:.2f} Wh")
            print(f"   • Huella de carbono estimada: {huella_co2:.4f} kg CO2")
    
    elif opcion == 2:
        print("\n[OPCIÓN 2] Consultando registros históricos...")
    
    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break
    
    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")

### HOLA MUNDO