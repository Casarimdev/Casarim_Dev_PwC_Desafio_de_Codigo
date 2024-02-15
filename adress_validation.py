# Exercício proposto:

# Um provedor de endereços retorna endereços apenas com ruas concatenadas,
# nomes e números em uma única string. Nosso próprio sistema, por outro lado,
# tem campos específicos para armazenar o nome da rua e o número da rua.
# Portanto, se faz necessário escrever um código simples que processe a
# entrada e retorne esses campos na saída.

# Entrada: string de endereço com os dados concatenados.
# Saída: string da rua e string do número da rua.


# Simple Cases + Complicated Cases
# Adress
def ConcertAdress():
    phrase = str(input('Insira seu endereço:'))

    # Check if the user input is empty
    if not phrase:
        print("O endereço não pode estar vazio.")
        return

    # Check if the input contains only numbers
    elif phrase.isdigit():
        print("O endereço não pode conter apenas números.")
        return

     # Split the address into parts
    parts = phrase.split(" ")

    # Check if the last part is a number
    if parts[-1].isdigit():
        # If the last part is a number, consider all parts except the last one as the address name
        address_name = " ".join(parts[:-1])
        # The final part of the address is the last part
        address_final = parts[-1]
    else:
        # If the last part is not a number, the address name consists of all parts until the second-to-last
        address_name = " ".join(parts[:-2])
        # The final part of the address consists of the second-to-last part and the last part
        address_final = " ".join(parts[-2:])

    adress_right = {f"{address_name}, {address_final}"}
    # Print the address name and the final part of the address
    print(adress_right)


# Call function
ConcertAdress()
