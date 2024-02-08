import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category):
        date = datetime.date.today()
        self.expenses.append({'date': date, 'amount': amount, 'description': description, 'category': category})
        print("Expense added successfully.")

    def view_monthly_summary(self, month, year):
        total_expenses = 0
        for expense in self.expenses:
            if expense['date'].month == month and expense['date'].year == year:
                total_expenses += expense['amount']
        print(f"Total expenses for {datetime.date(year, month, 1).strftime('%B %Y')}: ${total_expenses}")

    def view_category_expenditure(self, category):
        total_category_expenses = 0
        for expense in self.expenses:
            if expense['category'] == category:
                total_category_expenses += expense['amount']
        print(f"Total expenses for {category}: ${total_category_expenses}")

    def display_menu(self):
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenditure")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                amount = float(input("Enter the amount spent: $"))
                description = input("Enter a brief description: ")
                category = input("Enter the category: ")
                self.add_expense(amount, description, category)
            elif choice == '2':
                month = int(input("Enter the month (1-12): "))
                year = int(input("Enter the year: "))
                self.view_monthly_summary(month, year)
            elif choice == '3':
                category = input("Enter the category: ")
                self.view_category_expenditure(category)
            elif choice == '4':
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    expense_tracker.run()
