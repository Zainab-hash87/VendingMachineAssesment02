# Creating A Vending Machine 
# With the help of this Program, Customers will be able to choose snacks, sodas, enter cash, and get the appropriate change back.
# Written By: Zainab Afzal (CY1))


# the Feature that shows the welcome message
def welcome_message_():
    print("Welcome")
    print("                                            ")
    print("Thanks for coming at Vending Machine")
    print("............................................")
    print("Languages = English / Spanish")
    print("--------------------------------------------")

    # Select a language
    language = {
        '1': 'English',
        '2': 'Spanish'
    }

    language_code = input("Please choose the language (1 for English, 2 for Spanish): ")
    if language_code == '1':
        print("Selected English.")
    elif language_code == '2':
        print("Selected Spanish.")
    else:
        print("Inserted Language is incorrect. switching into English Language.")

# Feature to present available products
def display_menu(items):
    print("Available Products:")
    for category, products in items.items():
        print(f"{category}:")
        for code, details in products.items():
            name = details["Name"]
            price = details["Price AED"]
            stock = details["Stock"]
            print(f"  {code}: {name} - AED {price:.2f} (Stock: {stock})")

# Feature to select a product
def choose_product(items):
    while True:
        code = input("Insert the code of the item you want to purchase (or 'exit' to quit): ").upper()
        if code.lower() == 'exit':
            print("We appreciate your use of the vending machine! GOOD BYE!")
            return None
        for category, products in items.items():
            if code in products:
                return code, products[code]
        print("Incorrect! product code. Please try again.")

#  payment handling funtion
def payment_process(price):
    print(f"The price of the product is AED {price:.2f}. Please enter money.")
    total_inserted = 0.0
    while total_inserted < price:
        try:
            money = float(input(f"Insert money (remaining: AED {price - total_inserted:.2f}): "))
            if money > 0:
                total_inserted += money
            else:
                print("Please enter a correct number.")
        except ValueError:
            print("Incorrect input, please enter a valid number.")
    return total_inserted

# caculating the amount of payment and returning the balance.
def calculate_balance(total_inserted, price):
    balance  = total_inserted - price
    print(f"We appreciate your use of the vending machine! Here is your balance: AED {balance:.2f}. See you Later!")

#Vending Machine program
def vending_machine():
    items = {
        "Gummies": {
            "G1": {"Name": "Haribo Berries", "Price AED": 8.50, "Stock": 5},
            "G2": {"Name": "Chupa Chups", "Price AED": 5.50, "Stock": 7},
            "G3": {"Name": "Hitschies Saure", "Price AED": 9.50, "Stock": 8},
        },
        "Soft Drinks": {
            "S1": {"Name": "Fanta", "Price AED": 3.50, "Stock": 20},
            "S2": {"Name": "Sprite", "Price AED": 2.50, "Stock": 10},
            "S3": {"Name": "Shani", "Price AED": 1.50, "Stock": 8},
        },
        "Biscuits": {
            "B1": {"Name": "Sooper", "Price AED": 9.25, "Stock": 17},
            "B2": {"Name": "Glucose", "Price AED": 3.50, "Stock": 15},
            "B3": {"Name": "Rio", "Price AED": 4.25, "Stock": 12},
        },
    }

    welcome_message_()
    display_menu(items)

    while True:
        choice = choose_product(items)
        if not choice:
            break

        product_code, product_details = choice
        if product_details["Stock"] > 0:
            print(f"\You chose {product_details['Name']}, which is in AED {product_details['Price AED']:.2f}.")
            confirm = input("Do you want anything else? (yes/no): ").strip().lower()
            if confirm == 'yes':
                total_inserted = payment_process(product_details["Price AED"])
                calculate_balance(total_inserted, product_details["Price AED"])
                product_details["Stock"] -= 1
            else:
                print("\Purchase declined.")
        else:
            print(f"\nSorry, {product_details['Name']} is not available.")

        another = input("\nDo you want to buy another product? (yes/no): ").strip().lower()
        if another != 'yes':
            print("We appreciate your use of the vending machine. Goodbye!")
            break

# Run the vending machine
vending_machine()







