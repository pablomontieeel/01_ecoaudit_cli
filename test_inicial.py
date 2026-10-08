pareja_autora = input("Introduce el nombre de la pareja: ").strip()
nombre_dispositivo = input("Introduce el nombre del dispositivo: ").strip()
potencia_str = input("Introduce la potencia en Wh: ").strip()

potencia_wh = float(potencia_str)

consumo = potencia_wh * 24

print(f"--- INFORME PARA: {pareja_autora.upper()} ---")
print(f"Dispositivo: {nombre_dispositivo}")
print(f"Potencia: {potencia_wh} Wh")
print(f"Consumo diario: {consumo} Wh")