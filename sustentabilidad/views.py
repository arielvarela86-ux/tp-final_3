from django.shortcuts import render
from .services import obtener_metricas_consumo

def vista_panel_sustentabilidad(request):
    registros_industriales = [
        {'planta': 'Planta Mendoza', 'consumo_kwh': 4500.0},
        {'planta': 'Planta Buenos Aires', 'consumo_kwh': 8200.5},
        {'planta': 'Planta Córdoba', 'consumo_kwh': 3100.0},
    ]

    metricas = obtener_metricas_consumo(registros_industriales)
    return render(request, 'sustentabilidad/panel.html', metricas)