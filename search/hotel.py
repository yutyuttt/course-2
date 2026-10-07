names = ["John", "Mary", "Diana"]
rooms = [111, 123, 111]

key = "Mary"

i = 0
found = False
while (not found) and (i < len(names)):
    if names[i] == key:
        found = True
    else:
        i += 1

if found:
    print(rooms[i])
else:
    print(f"{key} is not a guest here.")