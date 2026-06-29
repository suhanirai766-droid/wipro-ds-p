filename = input("Enter file name: ")

with open(filename, "r") as file:
    words = file.read().split()

print("Longest word:", max(words, key=len))