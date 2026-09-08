def main():
    time = input("What time is it? ")
    time = convert(time)
    if time >= 7.0 and time <= 8.0:
        print("breakfast")
    elif time >= 12.0 and time <= 13.0:
        print("lunch")
    elif time >= 18.0 and time <= 19.0:
        print("dinner")
    else:
        print(" ")

def convert(time):
    h,m = time.split(":")
    h = float(h)
    m = float(m)
    m = m / 60
    return(h + m)

if __name__ == "__main__":
    main()