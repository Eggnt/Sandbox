def main():
    password = get_password()
    while len(password) < 10:
        password = get_password()
    print_stars(len(password))


def get_password():
    password = input("Please enter a password with at least 10 characters: ")
    return password


def print_stars(password_length):
    print("*" * password_length)


main()
