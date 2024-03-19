# Name: Luke Kutz-Pears
# Date: 03/18/2024

def encode(password):
    encoded_pass = ''
    for i in password:
        encoded_pass += str(int(i) + 3)
    return int(encoded_pass)


def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        choice = int(input('Please enter an option: '))

        if choice == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!\n')

        if choice == 2:
            # TODO: Implement decoder function and change None placeholder -> original password
            print(f'The encoded password is {encoded_password}, and the original password is {None}')

        if choice == 3:
            break


if __name__ == '__main__':
    main()
