class Reservation:
    def __init__(self, name, room) -> None:
        self.name = name
        self.room = room

reservations = [Reservation("John", 111), Reservation("Mary", 123), Reservation("Diana", 111)]

key = "Diana"

i = 0
found = False
while (not found) and (i < len(reservations)):
    if reservations[i].name == key:
        found = True
    else:
        i += 1

if found:
    print(reservations[i].room)
else:
    print(f"{key} is not a guest here.")
