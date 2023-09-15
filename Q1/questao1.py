def input_float_numbers():
    """
    Função que permite ao usuário digitar números float e gera uma lista.
    """
    number_list = []
    while True:
        try:
            num = float(input("Digite um número (ou deixe em branco para encerrar): "))
            number_list.append(num)
        except ValueError:
            break

    return number_list

def main():
    number_list = input_float_numbers()
    
    print("Valores digitados (originais):", number_list)
    print("Valores originais em índices pares:", number_list[::2])
    print("Valores originais em índices ímpares:", number_list[1::2])
    print("Cada valor da lista arredondado para 1 casa decimal:", [round(num, 1) for num in number_list])
    print("Somatório de valores contidos na lista original arredondado para 2 casas decimais:", round(sum(number_list), 2))
    print("Cada valor da lista arredondado para inteiro:", [int(num) for num in number_list])
    print("Do inteiro de cada valor, mostrar no sistema binário:", [bin(int(num)) for num in number_list])
    print("Do inteiro de cada valor, mostrar no sistema octal:", [oct(int(num)) for num in number_list])
    print("Do inteiro de cada valor, mostrar no sistema hexadecimal:", [hex(int(num)) for num in number_list])

if __name__ == "__main__":
    main()
