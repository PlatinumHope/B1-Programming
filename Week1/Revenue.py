#This is a business calculator program
#Vibe coding is for nerds

print("Welcome to the Business Calculator!")
print("This calculator helps you with basic business calculations.")

revenue = float(input("Enter your total revenue: $"))
expenses = float(input("Enter your total expenses: $"))


profit = revenue - expenses
print(f"Your profit is: ${profit}")

profit_margin = (profit / revenue) * 100 if revenue != 0 else 0
print(f"Your profit margin is: {profit_margin:.2f}%")

print("Thank you for using the Business Calculator!TM")
