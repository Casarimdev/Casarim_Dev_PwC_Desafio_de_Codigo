import unittest
from adress_validation import ConcertAdress


# If you run this test, the function ConcertAdress will be called along with the tests. So, if you would like to verify the tests results, simply type 'sair' in the terminal that is executing the function.

class TestExtrairEndereco(unittest.TestCase):

    # Simple Cases
    def test_extrair_endereco_simple(self):
        address = "Miritiba 339"
        result = ConcertAdress(address)
        expeted = {"Miritiba, 339"}
        self.assertEqual(result, expeted)

    def test_extrair_endereco_another_input_simple(self):
        address = "Babaçu 500"
        result = ConcertAdress(address)
        expeted = {"Babaçu, 500"}
        self.assertEqual(result, expeted)

    def test_extrair_endereco_another_input1_simple(self):
        address = "Cambuí 804B"
        result = ConcertAdress(address)
        expeted = {"Cambuí, 804B"}
        self.assertEqual(result, expeted)

    # Complicated Cases
    def test_extrair_endereco_complex_valid_input(self):
        address = "Rio Branco 23"
        result = ConcertAdress(address)
        expeted = {"Rio Branco, 23"}
        self.assertEqual(result, expeted)

    def test_extrair_endereco_complex_valid_input_2(self):
        address = "Quirino dos Santos 23 b"
        result = ConcertAdress(address)
        expeted = {"Quirino dos Santos, 23 b"}
        self.assertEqual(result, expeted)

    # Complex Cases
    def test_extrair_endereco_complex_valid_input_3(self):
        address = "4, Rue de la République"
        result = ConcertAdress(address)
        expeted = {"Rue de la République, 4"}
        self.assertEqual(result, expeted)

    def test_extrair_endereco_complex_valid_input_4(self):
        address = "100 Broadway Av"
        result = ConcertAdress(address)
        expeted = {"Broadway Av, 100"}
        self.assertEqual(result, expeted)

    def test_extrair_endereco_complex_valid_input_5(self):
        address = "Calle Sagasta, 26"
        result = ConcertAdress(address)
        expeted = {"Calle Sagasta, 26"}
        self.assertEqual(result, expeted)

    def test_extrair_endereco_complex_valid_input_6(self):
        address = "Calle 44 No 1991"
        result = ConcertAdress(address)
        expeted = {"Calle 44, No 1991"}
        self.assertEqual(result, expeted)

    # Variable Cases
    def test_split_address_variable_check(self):
        input_address = input("Agora vamos para o teste variável, insira seu endereço: ")
        result = ConcertAdress(input_address)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()


# Desafio Finalizado! Acompanhe a evolução e a explicação dos commits acessando a descrição no repositório:
# https://github.com/Casarimdev/Casarim_Dev_PwC_Desafio_de_Codigo