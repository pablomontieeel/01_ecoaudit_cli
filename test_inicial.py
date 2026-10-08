pareja_auditora = input("Introduce ambos nombres: ").strip()
consumo_str = input("Introduce el consumo en Wh: ").strip()

consumo_wh = float(consumo_str)

print(f"--- INFORME PARA: {pareja_auditora.upper()} ---")
print(f"El consumo registrado es de {consumo_wh} Wh.")