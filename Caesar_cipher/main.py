from constants import logo, alphabet_list

print(logo)


def caesar(input_text: str, shift_amount: int, encode_or_decode: str):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in input_text:
        if char not in alphabet_list:
            output_text += char
        else:
            shifted_index = alphabet_list.index(char) + shift_amount
            shifted_index %= len(alphabet_list)
            output_text += alphabet_list[shifted_index]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


go_again = True

while go_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(input_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n"
    ).lower()
    if restart == "no":
        go_again = False
        print("Goodbye")
