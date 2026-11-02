import unittest
from .services import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_nominal(self):
        resultado = calcular_emisiones_carbono(100.0, factor_emision=0.4)
        self.assertAlmostEqual(resultado, 40.0)

    def test_consumo_negativo_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10.0)