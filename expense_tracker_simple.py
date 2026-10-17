import json
from datetime import date

DATA_FILE = "expenses.json"
CATEGORIES = ["Food", "Transport", "Fun", "Study", "Other"]


def load_expenses():
    """Read expenses from the JSON file. Return an empty list if it doesn't exist."""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    """Write the expenses list to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses):
    """Ask the user for details and add a new expense."""
    print("Categories:", ", ".join(CATEGORIES))
    category = input("Category: ").strip().capitalize()
    if category not in CATEGORIES:
        print("Unknown category.")
        return

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be positive.")
        return

    description = input("Description: ").strip()

    expense = {
        "id": len(expenses) + 1,
        "date": date.today().isoformat(),
        "category": category,
        "amount": amount,
        "description": description,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added!")


def show_expenses(expenses):
    """Print all expenses and the total."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    total = 0
    for e in expenses:
        print(f"{e['id']}. {e['date']} | {e['category']} | "
              f"{e['amount']:.2f} | {e['description']}")
        total += e["amount"]
    print(f"Total: {total:.2f}")


def show_summary(expenses):
    """Show how much was spent in each category."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    totals = {}
    for e in expenses:
        category = e["category"]
        totals[category] = totals.get(category, 0) + e["amount"]

    for category, amount in totals.items():
        print(f"{category}: {amount:.2f}")

    biggest = max(expenses, key=lambda e: e["amount"])
    print(f"Biggest expense: {biggest['amount']:.2f} ({biggest['description']})")


def delete_expense(expenses):
    """Delete an expense by its ID."""
    try:
        expense_id = int(input("ID to delete: "))
    except ValueError:
        print("Please enter a number.")
        return

    for e in expenses:
        if e["id"] == expense_id:
            expenses.remove(e)
            save_expenses(expenses)
            print("Deleted.")
            return
    print("No expense with that ID.")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add expense")
        print("2. Show all expenses")
        print("3. Summary by category")
        print("4. Delete expense")
        print("0. Quit")

        choice = input("> ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
