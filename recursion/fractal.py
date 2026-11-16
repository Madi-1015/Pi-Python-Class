def test(x):
    print(x * "*")
    if x == 1:
        return 1
    else:
        test(x-1)
    print(x * "*")

x = int(input("Number "))
(test(x))

