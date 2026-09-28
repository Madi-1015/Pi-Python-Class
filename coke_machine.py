coins = [1, 5, 10, 25]
amount = 50

while True:
    if amount >= 0:
        print(f"Amount due:{amount}")
    else:
        print(f"Change owed: {abs(amount)}")
   
    insert_coin = int(input ("Coins "))
    if insert_coin in coins:
        amount -= insert_coin
    else:
        print("Invalid")
