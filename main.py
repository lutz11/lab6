# Name: Luke Kutz-Pears
# Date: 03/18/2024

from decoder import decode

# encode password function which increments numerical password by three numbers
def encode(password):
    encoded_pass = ''
    for i in password:
        encoded_pass += str((int(i) + 3) % 10)
    return str(encoded_pass)


def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        choice = int(input('Please enter an option: '))

        # option 1 encodes the provided password
        if choice == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')

        # option 2 decodes the encoded password, which returns the original password
        if choice == 2:
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}')

        # option 3 exits the program
        if choice == 3:
            break


if __name__ == '__main__':
    main()
