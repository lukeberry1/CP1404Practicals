min_length = 5

def main():
    password = get_password(min_length)
    print_asterrisks(password)


def get_password(min_length):
    password = str(input("Enter Password of {} characters or more:".format(min_length)))
    while len(password) < min_length:
        password = str(input("Enter Password of {} characters or more:".format(min_length)))
    return password

def print_asterrisks(sequence):
    print(len(sequence) * "*")

main()