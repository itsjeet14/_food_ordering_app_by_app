
import random
import string

# Admin functionalities

def add_food_item():
        food_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(4)])
        print("Food ID: ",food_id)

        name = input("Enter Food Name: ")
        quantity = input("Enter quantity: ")
        price = float(input("Enter Food Price: INR "))
        discount = float(input("Enter Discount on food: "))
        stock = (input("Enter availability of stocks: "))
    
        with open("food_items.txt", "a") as f:
            f.write(f"{food_id},{name},{quantity},{price},{discount},{stock}\n")
       
        print("Food Item Added Successfully!\n")

def edit_food_item():
       
        food_id = input("Enter FoodID of food item to edit: ")
        with open("food_items.txt", "r") as f:
            lines = f.readlines()
        found = False
        with open("food_items.txt", "w") as f:
            for line in lines:
                if line.startswith(food_id):
                    found = True
                    name = input("Enter new name (leave blank to keep old name): ")
                    quantity = input("Enter new quantity (leave blank to keep old quantity): ")
                    price = input("Enter new price (leave blank to keep old price): ")
                    discount = input("Enter new discount (leave blank to keep old discount): ")
                    stock = input("Enter new stock (leave blank to keep old stock): ")
                    if not name.strip():
                        name = line.split(",")[1]
                    if not quantity.strip():
                        quantity = line.split(",")[2]
                    if not price.strip():
                        price = line.split(",")[3]
                    if not discount.strip():
                        discount = line.split(",")[4]
                    if not stock.strip():
                        stock = line.split(",")[5]
                    f.write(f"{food_id},{name},{quantity},{price},{discount},{stock}\n")
                    print("Food item edited successfully.")
                else:
                    f.write(line)
        if not found:
            print("Food item not found.")


def view_food_item():
        
        with open("food_items.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            print("No food items found.")
        else:
            print("FoodID\tName\tQuantity\tPrice\tDiscount\tStock")
            for line in lines:
                food_id, name, quantity, price, discount, stock = line.strip().split(",")
                print(f"{food_id}\t{name}\t{quantity}\t{price}\t{discount}\t{stock}\n")

def remove_food_item():
       
        food_id = input("Enter FoodID of food item to remove: ")
        with open("food_items.txt", "r") as f:
            lines = f.readlines()
        found = False
        with open("food_items.txt", "w") as f:
            for line in lines:
                if not line.startswith(food_id):
                    f.write(line)
                else:
                    found = True
        if found:
            print("Food item removed successfully.")
        else:
            print("Food item not found.")


# User Functionalities
   
def user_detail():
        full_name = input("Enter Name: ")
        phone_number = (input("Enter Phone Number: "))
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        password = input("Enter Password: ")
     
        with open("users.txt", "a") as f:
            f.write(f"{full_name},{phone_number},{email},{address},{password}\n")
        print("User Registration Successfull!\n")


       
def user_login_by_phone_number():
   
        print("Please enter your Phone Number and password to login:")
        phone_number = input("Phone Number: ")
        password = input("Password: ")

    # Check if user exists and password is correct
        with open("users.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                user_data = line.strip().split(",")
                if user_data[1] == phone_number and user_data[4] == password:
                    print("Login successful!")
                    return True
            print("Invalid Phone Number or password. Please try again.")
            return False
    
def user_login_by_email():
        
        print("Please enter your email and password to login:")
        email = input("Email: ")
        password = input("Password: ")

        # Check if user exists and password is correct
        with open("users.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                user_data = line.strip().split(",")
                if user_data[2] == email and user_data[4] == password:
                    print("Login successful!")
                    return True
            print("Invalid email or password. Please try again.")
            return False

def place_order():
    items = []
    total = 0
    with open("food_items.txt", "r") as file:
        print("Menu")
        print("----")
        for line in file:
            data = line.strip().split(",")
            print(data[0] + ": " + data[1] + " (" + data[2] + ") [INR " + data[3] + "]")
        print("Enter the food item IDs separated by comma (,): ")
        selected_items = input().split(",")
        for item in selected_items:
            with open("food_items.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if data[0] == item:
                        items.append(data[1] + " (" + data[2] + ") [INR " + data[3] + "]")
                        total += float(data[3]) * (1 - float(data[4]) / 100)
                        break
        print("Selected items:")
        for item in items:
            print("- " + item)
        print("Total: INR", total)
        print("Place order? (y/n)")
        choice = input()
        if choice == "y":
            with open("orders.txt", "a") as file:
                file.write(", ".join(items) + " (Total: INR " + str(total) + ")\n")
                print("Order placed successfully")

# Function to view the order history
def view_orders():
    with open("orders.txt", "r") as file:
   
        print("Order History")
        print("--------------")
        for line in file:
            print(line.strip())


def update_profile():
    # Ask the user for their email and password to confirm their identity
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    
    # Open the text file in read mode
    with open('users.txt', 'r') as file:
        # Read each line in the text file
        lines = file.readlines()
        for i, line in enumerate(lines):
            # Split the line into its components
            components = line.strip().split(',')
            # Check if the email and password match
            if email == components[2] and password == components[4]:
                # Ask the user for the new information
                full_name = input('Enter your new full name (press enter to skip): ')
                phone_number = input('Enter your new phone number (press enter to skip): ')
                address = input('Enter your new address (press enter to skip): ')
                password = input('Enter your new password (press enter to skip): ')
                # Replace the old information with the new information in the text file
                if full_name:
                    components[0] = full_name
                if phone_number:
                    components[1] = phone_number
                if address:
                    components[3] = address
                if password:
                    components[4] = password
                lines[i] = ','.join(components) + '\n'
                # Write the updated information to the text file
                with open('users.txt', 'w') as file:
                    file.writelines(lines)
                print('Profile updated successfully!')
                return
        # If the email and password don't match any user, print an error message
        print('Invalid email or password. Please try again.')

print("Welocme to the application!")    
while True:
    # print("Welocme to the application!")
    print("1. Admin \n2. User \n3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("You have sucessfully loged in!")
        while True:
            # print("You have sucessfully loged in!")
            print("1. Add Food Item \n2. Edit Food Item \n3. View Food Item \n4. Remove Food Item \n5. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                add_food_item()
            
            elif choice == "2":
                edit_food_item()

            elif choice == "3":
                view_food_item()
            
            elif choice == "4":
                remove_food_item()
            
            elif choice == "5":
                break

            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        print("Welcome to the application!")

        while True:
            # print("Welcome to the application!")
            print("1. Register\n2. Login using phone number\n3. Login using email\n4. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                user_detail()
        
            elif choice == "2":
                if user_login_by_phone_number():
                    # print("You have sucessfully loged in!")
                    while True:
                        # print("You have sucessfully loged in!")
                        print("1. Place New Order \n2. Order History \n3. Update  profile\n4. Quit")
                        choice = input("Enter your choice: ")

                        if choice == "1":
                            place_order()
                        
                        elif choice == "2":
                            view_orders()

                        if choice == "3":
                            update_profile()
                
                        elif choice == "4":
                            break
                        else:
                            print("Invalid choice. Please try again.")

            elif choice == "3":
                if user_login_by_email():
                    # print("You have sucessfully loged in!")
                    while True:
                        # print("You have sucessfully loged in!")
                        print("1. Place New Order \n2. Order History \n3. Update  profile\n4. Quit")
                        choice = input("Enter your choice: ")

                        if choice == "1":
                            place_order()
                        
                        elif choice == "2":
                            view_orders()

                        elif choice == "3":
                            update_profile()
                
                        elif choice == "4":
                            break
                        else:
                            print("Invalid choice. Please try again.")

            elif choice == "4":    
                break

            else:
                print("Invalid choice. Please try again.")

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please try again.")

                      
print("Thank you for using the application!")

