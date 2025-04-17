def encode(msg, shift):
    result = []
    for char in msg:
        result.append(chr(ord(char) + shift % 26))
    return ''.join(result)


def decode(msg, shift):
    result = []
    for char in msg:
        result.append(chr(ord(char) - shift % 26))
    return ''.join(result)


def run_cipher():
    while True:
        choice = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()
        msg = input("Type your message: ")
        shift = int(input("Type the shift number: "))

        if choice == "encode":
            print("Here's the encoded result:", encode(msg, shift))
        elif choice == "decode":
            print("Here's the decoded result:", decode(msg, shift))
        else:
            print("Invalid choice. Try again.")
            continue

        again = input("Type 'yes' to go again. Otherwise type 'no': ").lower()
        if again == "no":
            break


if __name__ == "__main__":
    run_cipher()
