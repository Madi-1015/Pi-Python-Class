target_words = ["james", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]
classifier = input("Input Document ")
user_input = classifier.split(" ")


for a in user_input:
    if a.lower() in target_words:
        print("[REDACTED]", end=" ")
    else:
        print(a, end=" ")