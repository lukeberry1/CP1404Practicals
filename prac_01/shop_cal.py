total= 0
number= int(input("number of items: "))
if number < 0:
    print("invalid number of items")
else:
    for i in range(number):
        number1 = float(input("price of item: "))
        total = total+number1

    if total >= 100:
        total = total - (total*0.1)
    print("total price:", total)

