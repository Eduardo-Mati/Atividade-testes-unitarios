import unittest

from situacao import situacao

class TesteSituacao(unittest.TestCase):

    CASOS_VALIDOS = [
        (7.0, 80, "APROVADO"), # Verifica se a média mínima de aprovação, 7.0, é aceita.
        (4.0, 80, "RECUPERACAO"), # Verifica se a média 4.0 entra na recuperação.
        (3.9, 80, "REPROVADO"), # Verifica se 3.9 ainda resulta em reprovação.
        (0.0, 80, "REPROVADO"), # Verifica se a menor média permitida é aceita.
        (10.0, 100, "APROVADO"), # Verifica se a frequência máxima de 100% é válida.
        (10.0, 0, "REPROVADO_POR_FALTA"), # Verifica se a frequência mínima de 0% é válida, embora resulte em reprovação por falta.
        (10.0, 74, "REPROVADO_POR_FALTA"), # Verifica se 74% resulta em reprovação por falta.
        (10.0, 75, "APROVADO"), # Verifica se 75% já permite a aprovação pela média.
        (3.0, 74, "REPROVADO_POR_FALTA"), # Verifica se a falta também prevalece quando a média é baixa.
        (6.9, 75, "RECUPERACAO"), # Verifica se 6.9 ainda resulta em recuperação.
    ]

    def test_media_invalida_baixa(self):
        with self.assertRaises(ValueError):
            situacao(-0.1, 50)

    def test_media_invalida_alta(self):
        with self.assertRaises(ValueError):
            situacao(10.1, 50)

    def test_frequencia_invalida_baixa(self):
        with self.assertRaises(ValueError):
            situacao(10.0, -1)

    def test_frequencia_invalida_alta(self):
        with self.assertRaises(ValueError):
            situacao(10.0, 101)

    def test_casos_validos(self):
        for media, frequencia, esperado in self.CASOS_VALIDOS:
            with self.subTest(media=media, frequencia=frequencia):
                self.assertEqual(
                    situacao(media, frequencia),
                    esperado
                )
    
    # Escreva aqui os seus testes.
    # Dica: uma lista de casos e um laço com self.subTest(...)
    # e self.assertRaises(ValueError) para as entradas inválidas.


if __name__ == "__main__":
    unittest.main(verbosity=2)
