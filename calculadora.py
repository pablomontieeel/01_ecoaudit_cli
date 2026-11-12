"""Módulo de cálculo de impacto energético y huella de carbono."""


def estimar_consumo_wh(potencia_w: float, horas_uso: float, iteraciones: int = 1) -> float:
    """Calcula el consumo energético total en Vatios-hora (Wh).
    
    Multiplica la potencia por las horas de uso y las iteraciones del proceso."""

    return potencia_w * horas_uso * iteraciones


def calcular_huella_co2(consumo_wh: float, factor_emision: float = 0.23) -> float:
    """Calcula la huella de carbono en kg de CO2.
    
    Convierte el consumo en Wh a kWh y lo multiplica por el factor de emisión."""
    consumo_kwh = consumo_wh / 1000.0
    return consumo_kwh * factor_emision


def auditar_lote_servidores(num_equipos: int, potencia_media_w: float, horas: float) -> float:
    for i in range(1, num_equipos + 1):

        huella_total = 0.0
    
        consumo_wh = estimar_consumo_wh(potencia_media_w, horas)
        consumo_total = consumo_wh * num_equipos
        huella_co2 = calcular_huella_co2(consumo_wh)
        huella_total = huella_co2 * num_equipos
        
        print(f"Servidor {i}: Consumo = {consumo_total:.2f} Wh, Huella de CO2 = {huella_total:.4f} kg CO2")

        return huella_total