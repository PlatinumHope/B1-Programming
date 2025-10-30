Correct_PIN = 1984
Attempts = 0
Max_Attempts = 3
login_successful = False

while Attempts < Max_Attempts:
    if (PIN := int(input("Enter your 4-digit PIN: "))) == Correct_PIN and str(PIN).isdigit():
        print("Welcome Admin.")
        login_successful = True
        break
    elif not str(PIN).isdigit():
        print("Invalid input. Please enter a 4-digit PIN.")
        Attempts += 1
        print(f"Attempt {Attempts} of {Max_Attempts}")

    elif PIN != Correct_PIN:
        print("Incorrect PIN. Please try again.")
    Attempts += 1
    print(f"Attempt {Attempts} of {Max_Attempts}")

if not login_successful:
    print("Maximum attempts reached. We have contacted the authorities.")
