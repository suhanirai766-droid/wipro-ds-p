from collections import Counter
import re

filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read()

lines = text.splitlines()
line_count = len(lines)

if line_count <= 12:
    time = f"{line_count} AM"
else:
    time = f"{line_count - 12} PM"

words = re.findall(r"[A-Za-z]+", text.lower())

count = Counter(words)

place = count.most_common(1)[0][0].capitalize()

print("Meeting time:", time)
print("Meeting place:", place, "Street")