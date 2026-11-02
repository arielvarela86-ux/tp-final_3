def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser negativo.")
    return consumo_kwh * factor_emision

def obtener_metricas_consumo(registros):
    total_emisiones = 0.0
    emisiones_por_planta = {}

    for reg in registros:
        planta = reg.get('planta', 'Planta Genérica')
        consumo = reg.get('consumo_kwh', 0.0)
        
        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones += emisiones
        emisiones_por_planta[planta] = emisiones_por_planta.get(planta, 0.0) + emisiones

    planta_mayor_consumo = None
    emisiones_maximas = 0.0

    if emisiones_por_planta:
        planta_mayor_consumo = max(emisiones_por_planta, key=emisiones_por_planta.get)
        emisiones_maximas = emisiones_por_planta[planta_mayor_consumo]

    return {
        'total_emisiones': round(total_emisiones, 2),
        'planta_mayor_consumo': planta_mayor_consumo,
        'emisiones_maximas': round(emisiones_maximas, 2),
        'detalle_plantas': {k: round(v, 2) for k, v in emisiones_por_planta.items()}
    }