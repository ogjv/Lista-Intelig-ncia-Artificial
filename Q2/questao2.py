def count_vowels(text):
    """
    Função que conta o número de vogais em um texto.
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    text = ""
    while True:
        line = input("Digite uma linha de texto (ou deixe em branco para encerrar):\n")
        if line == "":
            break
        text += line + "\n"

    vowel_count = count_vowels(text)
    print(f"Total de vogais no texto: {vowel_count}")

if __name__ == "__main__":
    main()
