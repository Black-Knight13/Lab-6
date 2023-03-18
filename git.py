# encoder written by Jackson Turnbull

def encode_password(password):
    alpha = ""
    theta = password
    for i in theta:
        if int(i) in range(1, 7):
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

print(encode_password("12345666"))


def main():
    print("Menu \n------------- \n1.Encode \n2.Decode \n3.Quit")
    while True:
        option = int(input("Please enter an option: "))

        if option == 1:
            theta = input("Please enter your password to encode: ")
            alpha = encode_password(theta)
            print("Your password has been encoded and stored!")

        elif option == 3:
            break


if __name__ == "__main__":
    main()
