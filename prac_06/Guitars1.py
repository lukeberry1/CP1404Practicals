
from prac_06.Guitars import Guitars

def main():
    guitars = []
    name = input("Guitar name:")
    while name != "":
        year = int(input("Guitar make:"))
        cost = float(input("Guitar price:"))
        guitar_to_add = Guitars(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Guitar Name: ")

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
                 {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")

main()