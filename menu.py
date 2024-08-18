def get_menu_choice():
    options = [1, 2]

    while True:
        try:
            print("1. Enter new expense")
            print("2. View expenses")
            print("Ctr+D. Quit")

            choice = int(input("Choice: "))
            if choice in options:
                return choice
            else:
                raise ValueError
        except ValueError:
            pass
    


""" def step_menu(value):
    match value:
        case "1":

        case "2":
            
        case _:
            print("Unidentified option. Try again.")
 """
