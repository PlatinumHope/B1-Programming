Grade = int(input("Enter your grade (0-100): "))

if Grade >= 100 or Grade >= 90:
    print("Excellent A.")
elif Grade >= 80:
    print("Great B.")
elif Grade >= 70:
    print("Good C.")
elif Grade >= 60:
    print("Fair D.")
elif Grade <= 60:
    print("Dumbass lmao.")
elif Grade not in range(0, 101):
    print("Invalid grade. Please enter a grade between 0 and 100.")