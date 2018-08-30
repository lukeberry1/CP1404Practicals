hex_colours = {"alice blue": "f0f8ff", "antique white": "faebd7", "antique white 1": "ffefdb", "antique white 2": "eedfcc", "antique white 3": "cdc0b0",
               "antique white 4": "8b8378", "aquamarine 1": "7fffd4", "aquamarine 2": "76eec6", "aquamarine 4": "458b74", "azure 1": "f0ffff"}
colour = input("Choose Colour:").lower()

# while colour != hex_colours:
#     print(colour, "code is", hex_colours(colour))
while colour != "":
    if colour in hex_colours:
        print(colour, "code is", hex_colours[colour])
    else:
        print("no existing code for this colour")
    colour = input("Choose Colour:").lower()