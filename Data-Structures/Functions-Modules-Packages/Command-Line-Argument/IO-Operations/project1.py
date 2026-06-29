import re
from collections import Counter

import os

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "Sample.txt")

with open(file_path, "r") as file:
    lines = file.readlines()
    

# Meeting Time
n = len(lines)

if n <= 12:
    if n == 12:
        time = "12 PM"
    else:
        time = str(n) + " AM"
else:
    if n == 24:
        time = "12 AM"
    else:
        time = str(n - 12) + " PM"

# Meeting Place
text = " ".join(lines)
words = re.findall(r"[A-Za-z]+", text)
words = [word.lower() for word in words]

count = Counter(words)
place = count.most_common(1)[0][0].capitalize()

print("Meeting time:", time)
print("Meeting place:", place + " Street")