MIN_LENGTH = 5


def main():
    password = get_password(MIN_LENGTH)
    print_asterrisks(password)


def get_password(min_length):
    password = input("Enter Password of {} characters or more:".format(min_length))
    while len(password) < min_length:
        password = input("Enter Password of {} characters or more:".format(min_length))
    return password


def print_asterrisks(sequence):
    print(len(sequence) * "*")


main()
