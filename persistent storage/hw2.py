while True:
    try:
        float(input())
        break
    except ValueError:
        print("Invalid value, try again.")