
import mysql.connector as mycon

# Connect to MySQL database
try:
    c1 = mycon.connect(host='localhost', user='root', passwd='1234', database='HotelManagement')
    cur = c1.cursor()
except mycon.Error as err:
    print(f"Error: {err}")
    exit()

total = 0
s = 0

def hotel_divine_paradise():
    print('''
                                        HOTEL DIVINE PARADISE
                                'Come And Dive Into The Divine Paradise'

            Choose your requirement:
            1. Customer Details
            2. Room Details
            3. Room Rent
            4. Membership Details
            5. Food Orders
            6. Cost Checking''')

def adding_customer():
    try:
        nm = input("Enter the customer's name: ")
        mem = input("Enter the membership (yes/no): ")
        adhaar = int(input("Enter the Aadhaar number: "))
        ph = int(input("Enter the customer's phone number: "))
        persons = int(input("Enter the number of people: "))
        address = input("Enter the customer's address: ")
        cur.execute("INSERT INTO customer1 (name, phone, adhaar_no, address, persons, membership) VALUES (%s, %s, %s, %s, %s, %s)", 
                    (nm, ph, adhaar, address, persons, mem))
        c1.commit()
        print("Customer details entered successfully.")
    except Exception as e:
        print(f"Error adding customer: {e}")

def deletion_customer():
    try:
        adhaar = int(input("Enter the Aadhaar number of the customer: "))
        cur.execute("DELETE FROM customer1 WHERE adhaar_no = %s", (adhaar,))
        c1.commit()
        print("Customer details deleted successfully.")
    except Exception as e:
        print(f"Error deleting customer: {e}")

def updating_customer():
    print('''
            What do you want to update:
            1. Name of the customer
            2. Number of people
            3. Membership Details
        ''')
    try:
        s = int(input("Enter your choice: "))
        if s == 1:
            nm = input("Enter the customer's old name: ")
            mm = input("Enter the customer's new name: ")
            cur.execute("UPDATE customer1 SET name = %s WHERE name = %s", (mm, nm))
        elif s == 2:
            np = int(input("Enter the previous number of people: "))
            np1 = int(input("Enter the new number of people: "))
            cur.execute("UPDATE customer1 SET persons = %s WHERE persons = %s", (np1, np))
        elif s == 3:
            adhaar = int(input("Enter Aadhaar number: "))
            mem = input("Enter new membership details (yes/no): ")
            cur.execute("UPDATE customer1 SET membership = %s WHERE adhaar_no = %s", (mem, adhaar))
        c1.commit()
        print("Customer details updated successfully.")
    except Exception as e:
        print(f"Error updating customer: {e}")

# Define additional functions similarly using try-except blocks and validations...

def cost_checking():
    global total
    global s
    try:
        f = int(input("Enter room number: "))
        mb = input("Enter membership (silver/gold/platinum): ").lower()
        fooditems = total
        roomrent = s
        final_cost = 0

        if mb == 'silver':
            final_cost = total + s + 5999
        elif mb == 'gold':
            final_cost = total + s + 6999
        else:
            final_cost = total + s + 9999

        cur.execute("INSERT INTO cost_checking (room_no, food_cost, room_rent, membership, total_cost) VALUES (%s, %s, %s, %s, %s)",
                    (f, fooditems, roomrent, mb, final_cost))
        c1.commit()
        print("Cost checking details entered successfully.")
    except Exception as e:
        print(f"Error in cost checking: {e}")

def main_menu():
    hotel_divine_paradise()
    ans = int(input("Enter your choice: "))
    if ans == 1:
        print('''
            What is your requirement?
            1. Add a customer
            2. Delete a customer
            3. Update customer details
        ''')
        ch = int(input("Enter your choice: "))
        if ch == 1:
            adding_customer()
        elif ch == 2:
            deletion_customer()
        elif ch == 3:
            updating_customer()
    # Additional menu options...

gh = "y"
while gh.lower() == "y":
    main_menu()
    gh = input("Do you want to see the menu again? (y/n): ")
else:
    print("********** Thank You For Visiting Us ************")
