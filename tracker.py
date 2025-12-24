def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    note = input("Enter note: ")

    with open("expenses.txt", "a") as f:
        f.write(f"{amount},{category},{note}\n")

    print("✅ Expense added")


def view_expenses():
    print("\n--- Expenses ---")
    with open("expenses.txt", "r") as f:
        for line in f:
            amount, category, note = line.strip().split(",")
            print(f"₹{amount} | {category} | {note}")


while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("❌ Invalid choice")
