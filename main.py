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
        print("\n[OPCIÓN 1] Iniciando proceso de auditoría...")

        print("Introduzca el número de iteraciones para la auditoría:")
        iteraciones_str = input("Número de iteraciones: ").strip()
        
        try:
            iteraciones = int(iteraciones_str)
        except ValueError:
            print("⚠️ Error: Debe introducir un número entero.")
            continue   
        if iteraciones <= 0:
            print("⚠️ Error: El número de iteraciones debe ser mayor que 0.")
        else:
            print("El número de iteraciones es válido. Continuando con la auditoría...")
                
    
    elif opcion == 2:
        print("\n[OPCIÓN 2] Consultando registros históricos...")
    
    elif opcion == 3:
        print("\nSaliendo de EcoAudit CLI. ¡Hasta pronto!")
        break
    
    else:
        print("⚠️ Opción no válida. Elija un número entre 1 y 3.")