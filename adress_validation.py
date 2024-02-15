# Exercício proposto: 

# Um provedor de endereços retorna endereços apenas com ruas concatenadas,
# nomes e números em uma única string. Nosso próprio sistema, por outro lado,
# tem campos específicos para armazenar o nome da rua e o número da rua.
# Portanto, se faz necessário escrever um código simples que processe a 
# entrada e retorne esses campos na saída.

# Entrada: string de endereço com os dados concatenados.
# Saída: string da rua e string do número da rua.


# Simple Case
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

    # Splits the address into two arrays
    cut_phrase = phrase.split(" ")

    # Adress right
    adress_right = {cut_phrase[0], cut_phrase[1]}
    print(adress_right)


# Call function 
ConcertAdress()
