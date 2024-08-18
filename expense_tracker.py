import menu

def main():
    choice = menu.get_menu_choice()
    print (choice)
    # menu
        # Present menu
        # Collect input (test for errors)
        # menu state machine
            # New Expense
                # Collect inputs: expense name, amount, category
                # Store in a dictionary
                # Back to menu
            # View Expenses
                # Display list of exprenses in table format



def get_input(prompt):
    return input(f"{prompt}")
    


if __name__ == "__main__":
    main()
