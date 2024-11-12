# test_atividade.py

import unittest
from codigo import *  # Importa todas as funções do arquivo 'codigo.py'

class TestCodigo(unittest.TestCase):

    # Testa a função 'email_valido'
    def test_email_valido(self):
        self.assertTrue(email_valido("teste@dominio.com"))
        self.assertFalse(email_valido("teste@dominio"))
        self.assertFalse(email_valido("teste@dominiocom"))
        self.assertFalse(email_valido("teste@.com"))

    # Testa a função 'eh_par'
    def test_eh_par(self):
        self.assertTrue(eh_par(4))  # Teste com número par
        self.assertFalse(eh_par(5))  # Teste com número ímpar
        self.assertTrue(eh_par(0))  # Teste com zero
        self.assertFalse(eh_par(-3))  # Teste com número negativo ímpar

    # Testa a função 'fatorial'
    def test_fatorial(self):
        self.assertEqual(fatorial(0), 1)  # Fatorial de 0 é 1
        self.assertEqual(fatorial(1), 1)  # Fatorial de 1 é 1
        self.assertEqual(fatorial(5), 120)  # Fatorial de 5 é 120
        self.assertEqual(fatorial(7), 5040)  # Fatorial de 7 é 5040

    # Testa a função 'quadrado'
    def test_quadrado(self):
        self.assertEqual(quadrado(2), 4)  # 2^2 é 4
        self.assertEqual(quadrado(-3), 9)  # (-3)^2 é 9
        self.assertEqual(quadrado(0), 0)  # 0^2 é 0

    # Testa a função 'eh_positivo'
    def test_eh_positivo(self):
        self.assertTrue(eh_positivo(1))  # 1 é positivo
        self.assertFalse(eh_positivo(0))  # 0 não é positivo
        self.assertFalse(eh_positivo(-1))  # -1 não é positivo

    # Testa a função 'verificar_maioridade'
    def test_verificar_maioridade(self):
        self.assertEqual(verificar_maioridade(18), 'maior de idade')  # Maior de idade
        self.assertEqual(verificar_maioridade(17), 'menor de idade')  # Menor de idade

    # Testa a função 'classificar_temperatura'
    def test_classificar_temperatura(self):
        self.assertEqual(classificar_temperatura(-5), 'frio')  # Temperatura negativa
        self.assertEqual(classificar_temperatura(20), 'moderado')  # Temperatura entre 0 e 25
        self.assertEqual(classificar_temperatura(30), 'quente')  # Temperatura acima de 25

    # Testa a função 'avaliar_nota'
    def test_avaliar_nota(self):
        self.assertEqual(avaliar_nota(8), 'aprovado')  # Nota maior que 7
        self.assertEqual(avaliar_nota(6), 'recuperacao')  # Nota entre 5 e 7
        self.assertEqual(avaliar_nota(4), 'reprovado')  # Nota menor que 5

    # Testa a função 'pode_votar'
    def test_pode_votar(self):
        self.assertEqual(pode_votar(20), 'voto obrigatório')  # Maior de 18 anos
        self.assertEqual(pode_votar(17), 'voto facultativo')  # Entre 16 e 18 anos
        self.assertEqual(pode_votar(15), 'não pode votar')  # Menor de 16 anos

    # Testa a função 'avaliar_produto'
    def test_avaliar_produto(self):
        self.assertEqual(avaliar_produto(5), 'excelente')  # 5 estrelas
        self.assertEqual(avaliar_produto(4), 'bom')  # 4 estrelas
        self.assertEqual(avaliar_produto(3), 'regular')  # 3 estrelas
        self.assertEqual(avaliar_produto(2), 'ruim')  # 2 estrelas
        self.assertEqual(avaliar_produto(1), 'péssimo')  # 1 estrela
        self.assertEqual(avaliar_produto(0), 'valor inválido')  # 0 estrelas
        self.assertEqual(avaliar_produto(6), 'valor inválido')  # Número inválido de estrelas

if __name__ == "__main__":
    unittest.main()
