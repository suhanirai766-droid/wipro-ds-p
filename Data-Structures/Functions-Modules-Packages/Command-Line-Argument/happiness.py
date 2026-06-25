like = input("Enter liked numbers: ").split("-")
dislike = input("Enter disliked numbers: ").split("-")
numbers = input("Enter numbers: ").split("-")

happiness = 0

for num in numbers:
    if num in like:
        happiness += 1
    elif num in dislike:
        happiness -= 1

print("Final Happiness:", happiness)