import unittest
from codigo import *

class TestCodigo(unittest.TestCase):

    def test_eh_positivo(self):
        self.assertTrue(eh_positivo(1))
        self.assertFalse(eh_positivo(0))
        self.assertFalse(eh_positivo(-1))

    def test_verificar_maioridade(self):
        self.assertEqual(verificar_maioridade(18), 'maior de idade')
        self.assertEqual(verificar_maioridade(17), 'menor de idade')

    def test_classificar_temperatura(self):
        self.assertEqual(classificar_temperatura(-5), 'frio')
        self.assertEqual(classificar_temperatura(20), 'moderado')
        self.assertEqual(classificar_temperatura(30), 'quente')

if __name__ == "__main__":
    unittest.main()