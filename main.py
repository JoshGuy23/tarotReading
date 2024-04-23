import random


def read_file():
    with open(file="Arcanas.txt") as file:
        lines = file.readlines()
    return lines


def determine_state():
    state = random.randint(0, 1)
    if state == 1:
        return "upright"
    else:
        return "reversed"


print("Today, we will draw a set of tarot cards to read your past, present, & future.")
arcana = read_file()

print(f"Past: {random.choice(arcana).strip()}, {determine_state()}")
print(f"Present: {random.choice(arcana).strip()}, {determine_state()}")
print(f"Future: {random.choice(arcana).strip()}, {determine_state()}")
