completed = False

while not completed:
    try:
        filename = input("please give filename: ")
        with open(filename, "at") as f:
            print(440, file=f)
        completed = True
    except Exception as e:
        print("error, try again: " + str(e))