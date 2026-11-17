import unittest

from situacao import situacao


class TesteSituacao(unittest.TestCase):

    def test_limite_aprovacao(self):
        self.assertEqual(situacao(7.0, 80), "APROVADO")

    def test_media_invalida_baixa(self):
        with self.assertRaises(ValueError):
            situacao(-0.1, 50)

    def test_media_invalida_alta(self):
        with self.assertRaises(ValueError):
            situacao(10.1, 50)

    def test_limite_media_recuperacao(self):
        self.assertEqual(situacao(4.0, 80), "RECUPERACAO")

    def test_abaixo_da_recuperacao(self):
        self.assertEqual(situacao(3.9, 80), "REPROVADO")

    def test_media_minima_valida(self):
        self.assertEqual(situacao(0.0, 80), "REPROVADO")

    def test_limite_frequencia_valida_alta(self):
        self.assertEqual(situacao(10.0, 100), "APROVADO")

    def test_limite_frequencia_valida_baixa(self):
        self.assertEqual(situacao(10.0, 0), "REPROVADO_POR_FALTA")

    def test_frequencia_abaixo_do_minimo(self):
        self.assertEqual(situacao(10.0, 74), "REPROVADO_POR_FALTA")

    def test_frequencia_minima_para_aprovacao(self):
        self.assertEqual(situacao(10.0, 75), "APROVADO")

    def test_frequencia_invalida_baixa(self):
        with self.assertRaises(ValueError):
            situacao(10.0, -1)

    def test_frequencia_invalida_alta(self):
        with self.assertRaises(ValueError):
            situacao(10.0, 101)

    def test_reprovacao_por_falta_com_media_baixa(self):
        self.assertEqual(situacao(3.0, 74), "REPROVADO_POR_FALTA")

    def test_limite_superior_recuperacao(self):
        self.assertEqual(situacao(6.9, 75), "RECUPERACAO")


    
    # Escreva aqui os seus testes.
    # Dica: uma lista de casos e um laço com self.subTest(...)
    # e self.assertRaises(ValueError) para as entradas inválidas.


if __name__ == "__main__":
    unittest.main(verbosity=2)
