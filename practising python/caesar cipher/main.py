alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def caesar(msg, shift, cipher):
    msg_list = list(msg)
    result_list = []

    if cipher == "decode":
        shift *= -1

    for i in range(len(msg_list)):

        if msg_list[i] in alphabet or msg_list[i] in ALPHABET:
            if msg_list[i].islower():
                letter_index = alphabet.index(msg_list[i])

            else:
                letter_index = ALPHABET.index(msg_list[i])

            if letter_index + shift >= len(alphabet):
                result_index = letter_index + shift - len(alphabet)

            else:
                result_index = letter_index + shift

            result_letter = alphabet[result_index]

            if msg_list[i].islower():
                result_list += result_letter
            else:
                result_list += result_letter.capitalize()

        else:
            result_list += msg_list[i]

        result_msg = "".join(result_list)

    print(f"\nThe {cipher}d message is: {result_msg}")


def run_program():
    action = input(
        "\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    msg_to_encrypt = input("\nType your message: ")
    shift = int(input("\nType the shift number: "))
    caesar(msg_to_encrypt, shift, action)

    print()

    repeat_program = input(
        "\nType 'yes' if you want to reuse the program, type 'no' to exit program: ").lower()

    if repeat_program == "yes":
        run_program()

    else:
        print("\nThank you for using the program.")


run_program()
