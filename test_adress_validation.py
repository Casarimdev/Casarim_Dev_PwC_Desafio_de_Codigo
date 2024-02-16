import unittest


# Function that splits the address into two arrays
def split_address(address):
    if not address:
        return None, "O endereço não pode estar vazio"
    parts = address.split(" ")
    if parts[-1].isdigit() or any(char.isdigit() for char in parts[-1]):
        address_name = " ".join(parts[:-1])
        address_final = parts[-1]
    else:
        address_name = " ".join(parts[:-2])
        address_final = " ".join(parts[-2:])
    return address_name, address_final


# Test class for the split_address function
class TestSplitAddress(unittest.TestCase):

    # Simple Cases
    def test_split_address_simple(self):
        input_address = "Miritiba 339"
        result = split_address(input_address)
        expected = ("Miritiba", "339")
        self.assertEqual(result, expected)

    def test_split_address_another_input_simple(self):
        input_address = "Babaçu 500"
        result = split_address(input_address)
        expected = ("Babaçu", "500")
        self.assertEqual(result, expected)

    def test_split_address_another_input1_simple(self):
        input_address = "Cambuí 804B"
        result = split_address(input_address)
        expected = ("Cambuí", "804B")
        self.assertEqual(result, expected)

    # Complicated Cases
    def test_split_address_complex_valid_input(self):
        input_address = "Rio Branco 23"
        result = split_address(input_address)
        expected = ("Rio Branco", "23")
        self.assertEqual(result, expected)

    def test_split_address_complex_valid_input_2(self):
        input_address = "Quirino dos Santos 23 b"
        result = split_address(input_address)
        expected = ("Quirino dos Santos", "23 b")
        self.assertEqual(result, expected)


# If the file is executed directly, run the tests
if __name__ == '__main__':
    unittest.main()
