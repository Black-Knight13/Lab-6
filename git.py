# encoder written by Jackson Turnbull

def encode_password(password):
    alpha = ""
    theta = password
    for i in theta:
        if int(i) in range(0, 7):
            theta = str(int(i) + 3)
            alpha += theta

        elif int(i) >= 7:
            if i == '7':
                theta = '0'
                alpha += theta
            elif i == '8':
                theta = '1'
                alpha += theta
            elif i == '9':
                theta = '2'
                alpha += theta

    return alpha


def decode_password(password):
    decoded = ''
    a = 0
    for i in password:
        if int(i) in range(3,10):
            a = int(i) - 3
            decoded += str(a)
        elif int(i) == 2:
            a = 9
            decoded += str(a)
        elif int(i) == 1:
            a = 8
            decoded += str(a)
        elif int(i) == 0:
            a = 7
            decoded += str(a)
    return decoded

print(encode_password("12345666"))


def main():
    print("Menu \n------------- \n1.Encode \n2.Decode \n3.Quit")
    alpha = ''
    while True:
        option = int(input("Please enter an option: "))

        if option == 1:
            theta = str(input("Please enter your password to encode: "))
            # added str to this - travis
            alpha = encode_password(theta)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f'The encoded password is {alpha}, and the original password is {decode_password(alpha)}.')
        elif option == 3:
            break


if __name__ == "__main__":
    main()
