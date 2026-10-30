"""
Testes Unitários Automatizados da Calculadora Evoluída
Garante que a nova funcionalidade de porcentagem funcione e que
não haja regressão nas operações anteriores (adição, subtração, multiplicação e divisão).
"""
import unittest
from calculadora import somar, subtrair, multiplicar, dividir, calcular_porcentagem

class TestCalculadoraEvoluida(unittest.TestCase):

    # 1. Testes das operações legadas (Garantia de Não-Regressão)
    def test_somar(self):
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(somar(-2, 5), 3)
        self.assertAlmostEqual(somar(1.5, 2.3), 3.8)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 4), 6)
        self.assertEqual(subtrair(5, 10), -5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(6, 7), 42)
        self.assertEqual(multiplicar(-3, 4), -12)
        self.assertEqual(multiplicar(10, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(20, 4), 5)
        self.assertAlmostEqual(dividir(7, 2), 3.5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    # 2. Testes da nova operação (Porcentagem)
    def test_calcular_porcentagem_basica(self):
        # 15% de 200 = 30.0
        self.assertEqual(calcular_porcentagem(200, 15), 30.0)

    def test_calcular_porcentagem_com_decimais(self):
        # 12.5% de 80 = 10.0
        self.assertEqual(calcular_porcentagem(80, 12.5), 10.0)

    def test_calcular_porcentagem_zero(self):
        # 0% de 500 = 0
        self.assertEqual(calcular_porcentagem(500, 0), 0.0)
        # 50% de 0 = 0
        self.assertEqual(calcular_porcentagem(0, 50), 0.0)

    def test_calcular_porcentagem_maior_que_cem(self):
        # 150% de 200 = 300.0
        self.assertEqual(calcular_porcentagem(200, 150), 300.0)

if __name__ == "__main__":
    unittest.main()
