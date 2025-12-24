def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        note = input("Enter note: ")

        with open("expenses.txt", "a") as f:
            f.write(f"{amount},{category},{note}\n")

        print("✅ Expense added")

    except ValueError:
        print("❌ Please enter a valid number for amount")


def view_expenses():
    total = 0.0
    print("\n--- Expenses ---")

    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                amount, category, note = line.strip().split(",")
                total += float(amount)
                print(f"₹{amount} | {category} | {note}")

        print(f"\n💰 Total Expense: ₹{total}")

    except FileNotFoundError:
        print("No expenses found yet.")


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
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice")
