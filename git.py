def encode_password(password):
    alpha = ""
    for i in password:
        alpha += str(int(i) + 3)

    return alpha

def decode_password(d_password):
    theta = ""
    for i in d_password:
        theta += str(int(i) - 3)
    return theta




def main():
    password = input("Please input your password: ")
    while True:
        print(f"Here is your encoded password: {encode_password(password)}")

        password = input("Please input your password: ")
        print(f"Here is your decoded password: {decode_password(password)}")
        break





if __name__ == "__main__":
    main()
