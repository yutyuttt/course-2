import pathlib, statistics


file_path = pathlib.Path("data") / input() # idk why directly putting full path in input returns os error
try:
    with open(file_path, "r") as f:
        integers = f.readlines()
        mean = statistics.mean([int(integer) for integer in integers])
        print(mean)
except FileNotFoundError:
    print("File does not exist")
except UnicodeDecodeError:
    print("File cannot be opened")
except ValueError:
    print("Invalid values in file")