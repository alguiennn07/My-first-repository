age=int(input("Enter your age: "))
adult= age>= 18
if adult:
    print("You are old enough to drive")
elif not adult:
        print(f"You need {18-age} more years to drive")