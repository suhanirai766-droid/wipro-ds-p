import os

message = input("Enter welcome message: ")

print("File Name:", os.path.basename(__file__))
print("Welcome Message:", message)