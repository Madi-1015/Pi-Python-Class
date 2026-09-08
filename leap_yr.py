a = int(input("What year is it? "))
if a % 4 == 0:
    if a % 100 == 0 and a % 400 != 0:
        print ("Not a Leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")