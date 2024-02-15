import unittest


# Function that splits the address into two arrays
def split_address(address):
    return address.split(" ")


# Test class for the split_address function
class TestSplitAddress(unittest.TestCase):

    # Simple Cases
    def test_split_address_simple(self):
        input_address = str(input('Insira seu endereço:'))
        result = split_address(input_address)
        adress_right = {result[1], result[0]}
        expected = {result[0], result[1]}
        self.assertEqual(adress_right, expected)

    def test_split_address_another_input_simple(self):
        input_address = "Miritiba 339"
        result = split_address(input_address)
        expected = ["Miritiba", "339"]
        self.assertEqual(result, expected)

    def test_split_address_another_input1_simple(self):
        input_address = "Babaçu 500"
        result = split_address(input_address)
        expected = ["Babaçu", "500"]
        self.assertEqual(result, expected)

    def test_split_address_another_input2_simple(self):
        input_address = "Cambuí 804B"
        result = split_address(input_address)
        expected = ["Cambuí", "804B"]
        self.assertEqual(result, expected)


# If the file is executed directly, run the tests
if __name__ == '__main__':
    unittest.main()
