import random, pathlib, pickle

integers = []

file_path = pathlib.Path("data") / "integers.txt"
if file_path.exists():
    with open(file_path, "r") as f:
        integers = f.readlines()
else:
    for _ in range(10000):
        integers.append(random.randint(0, 10000))

    with open(file_path, "w") as f:
        for integer in integers:
            f.write(f"{integer}\n")

# serialize
file_path2 = pathlib.Path("data") / "integers2.txt"
f = open(file_path2, "wb")
pickle.dump(integers, f)
f.close()

# deserialize
f = open(file_path2, "rb")
integers = pickle.load(f)
f.close()
print(integers)