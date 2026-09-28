lineup = {

}

while True:
    musician = input("Enter a Musician: ").lower()
    if musician == "done":
        break
    else:
        if musician in lineup:
            lineup[musician] += 1
        else:
            lineup[musician] = 1
print("\nVOTES\n---------\n")
for key, value in sorted(lineup.items()):
    print(f"- {key.title()}:{value}")
