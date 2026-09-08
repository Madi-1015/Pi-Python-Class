def operation(y):
    match y:
        case "+":
            print(x + z)
        case "-":
            print(x * z)
        case "*":
            print(x * z)
        case "/":
            print(x / z)

calc = input("equation: ")
x, y, z = calc.split(" ")
x = int(x)
z = int(z)
operation(y)