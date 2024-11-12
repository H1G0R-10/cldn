import unittest
from codigo import *

class TestCodigo(unittest.TestCase):

    def test_email_valido(self):
        self.assertTrue(email_valido("teste@dominio.com"))
        self.assertFalse(email_valido("teste@dominio"))
        self.assertFalse(email_valido("teste@dominiocom"))
        self.assertFalse(email_valido("teste@.com"))

    def test_eh_par(self):
        self.assertTrue(eh_par(4))
        self.assertFalse(eh_par(5))

    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(5), 120)

    def test_quadrado(self):
        self.assertEqual(quadrado(2), 4)
        self.assertEqual(quadrado(-3), 9)

if __name__ == "__main__":
    unittest.main()