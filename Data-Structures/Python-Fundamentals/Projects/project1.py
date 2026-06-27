distance = float(input("how far would you like to travel in miles?"))
if distance < 3:
    print("I suggest Bicycle to your destination")
elif distance < 300:
    print("I suggest Car to your destination")
else:
    print("I suggest Plane to your destination")
