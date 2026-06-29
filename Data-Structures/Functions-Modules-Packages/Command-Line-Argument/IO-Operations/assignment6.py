filename = input("Enter file name: ")
word = input("Enter word: ")

with open(filename, "r") as file:
    text = file.read().lower()

print("Frequency:", text.split().count(word.lower()))