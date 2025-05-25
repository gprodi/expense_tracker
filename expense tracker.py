# Expense Tracker Program
# This program allows users to track their expenses by adding, listing, and filtering them by category.
# It also calculates the total expenses.

#define functions to handle expenses
def add_expense(expenses, amount, category):
# Adds an expense to the list of expenses
    expenses.append({'amount': amount, 'category': category})

# Function to print all expenses   
def print_expenses(expenses):
# Prints all expenses in a formatted way
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Function to calculate total expenses    
def total_expenses(expenses):
# Calculates the total amount of all expenses
    return sum(map(lambda expense: expense['amount'], expenses))

# Function to filter expenses by category    
def filter_expenses_by_category(expenses, category):
# Filters expenses by a given category
    return filter(lambda expense: expense['category'] == category, expenses)
    
# Main function to run the expense tracker program
def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

#main function call to start the program
main()