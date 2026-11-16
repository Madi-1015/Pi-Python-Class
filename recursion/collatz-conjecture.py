def col(x):
    print(x)
    if x <= 1:
        return 0
    elif x % 2 == 0:
        return col(x // 2) + 1
    else:
        return col(3*x+1) + 1
    
x = 42
print(col(x))