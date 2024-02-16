# Exercício proposto:

# Um provedor de endereços retorna endereços apenas com ruas concatenadas,
# nomes e números em uma única string. Nosso próprio sistema, por outro lado,
# tem campos específicos para armazenar o nome da rua e o número da rua.
# Portanto, se faz necessário escrever um código simples que processe a
# entrada e retorne esses campos na saída.

# Entrada: string de endereço com os dados concatenados.
# Saída: string da rua e string do número da rua.


# Complete Exercise
import re


def ConcertAdress(address):

    # Check if the address starts with a number
    if address[0].isdigit():
        pattern = r'^(?P<numero>\b\d+\b)(?:[,\s]+)?(?P<rua>.+)$'

    # Check if the address contains words like "No", "N°", or "número"
    elif re.match(r'.*\b(?:No|N°|número)\b', address):
        pattern = r'^(?P<rua>.+?)(?:[,\s]+(?P<numero>No\s+\d+))'

    # Check if the address contains a number
    elif re.search(r'\b\d+\b', address):
        pattern = r'^(?P<rua>[^\d,]+)(?:,\s*)?(?P<numero>\b\d+[A-Za-z]*\s*[A-Za-z]*)?$'

    # If none of the above conditions are met, assume the address starts with a street name followed by a number
    else:
        pattern = r'^(?P<rua>[^\d,]+)\s*(?P<numero>\b\d+[A-Za-z]*\s*[A-Za-z]*)$'

    # Search for the pattern in the address string
    match = re.match(pattern, address)

    if match:
        # Extract the street name and street number
        street = match.group('rua').strip()
        number = match.group('numero').strip() if match.group('numero') else ''
        return {f"{street}, {number}"}
    else:
        return "Endereço Inválido. Por favor, tente novamente."


while True:
    # Ask the user to input an address
    address = input("Insira deu endereço (ou 'sair' para encerrar): ").strip()

    # Check if the user wants to exit
    if address.lower() == 'sair':
        print("Saindo do programa...")
        break

    # Extract the street name and street number
    result = ConcertAdress(address)

    # Print the result
    print(result)


# Desafio Finalizado! Acompanhe a evolução e a explicação dos commits acessando a descrição no repositório:
# https://github.com/Casarimdev/Casarim_Dev_PwC_Desafio_de_Codigo