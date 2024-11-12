import unittest
from codigo import *

class TestCodigo(unittest.TestCase):

    def test_avaliar_nota(self):
        self.assertEqual(avaliar_nota(8), 'aprovado')
        self.assertEqual(avaliar_nota(6), 'recuperacao')
        self.assertEqual(avaliar_nota(4), 'reprovado')

    def test_pode_votar(self):
        self.assertEqual(pode_votar(20), 'voto obrigatório')
        self.assertEqual(pode_votar(17), 'voto facultativo')
        self.assertEqual(pode_votar(15), 'não pode votar')

    def test_avaliar_produto(self):
        self.assertEqual(avaliar_produto(5), 'excelente')
        self.assertEqual(avaliar_produto(4), 'bom')
        self.assertEqual(avaliar_produto(3), 'regular')
        self.assertEqual(avaliar_produto(2), 'ruim')
        self.assertEqual(avaliar_produto(1), 'péssimo')
        self.assertEqual(avaliar_produto(0), 'valor inválido')

if __name__ == "__main__":
    unittest.main()