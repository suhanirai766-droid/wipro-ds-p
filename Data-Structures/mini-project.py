people = {
    "jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("Original Dictionary:")
for name, fact in people.items():
    print(name + ":", fact)

people["Jeff"] = "Is afraid of heights."
people["jill"] = "can hula dance."

print("\nUpdated Dictionary:")
for name, fact in people.items():
    print(name + ":", fact)
