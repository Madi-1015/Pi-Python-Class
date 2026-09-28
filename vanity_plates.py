def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    n = False
    if len(plate) > 6:
        return False
    elif len(plate) < 2:
        return False
    elif plate.isalnum() == False:
        return False
    elif plate[0].isdigit() and plate[1].isdigit():
        return False
    elif plate[0] == "0":
        return False
    else:
        for a in plate:
            if a.isalpha() and n == True:
                return False
            if a.isdigit():
                if n == False and a == "0":
                    return False
                n = True
        return True


main()
