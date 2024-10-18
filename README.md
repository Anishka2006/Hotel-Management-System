# Hotel Management System

## Overview
The **Hotel Management System** is a Python-based application that simplifies hotel operations by integrating customer management, room details, food orders, and cost calculation with a **MySQL** backend. It’s designed to help hotel staff manage essential tasks efficiently while maintaining data integrity through a secure database.

## Features
- **Customer Management**: Add, update, and delete customer records, including name, Aadhaar number, phone number, address, and membership status.
- **Room Details**: Manage room availability, rent, and other details.
- **Food Orders**: Track customer food orders and add them to the final bill.
- **Cost Calculation**: Automatically calculate total costs, including room rent, food orders, and membership benefits.
- **Database Integration**: All information is stored in a **MySQL** database for persistence.

## Technologies Used
- **Python**: Application logic.
- **MySQL**: Database management.
- **MySQL Connector for Python**: For Python-MySQL communication.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/hotel-management-system.git
   ```
2. **Install dependencies**:
   ```bash
   pip install mysql-connector-python
   ```
3. **Set up MySQL database**:
   - Create a database named `HotelManagement`.
   - Create the necessary tables using the provided SQL scripts or based on the code structure.

4. **Run the application**:
   ```bash
   python PROJECT_fixed.py
   ```

## How to Use
1. Start the application and choose from the menu:
   - Add, update, or delete customer details.
   - Manage room details and food orders.
   - Calculate final cost based on room rent, food orders, and membership.
2. The system will interact with the MySQL database to store and retrieve data efficiently.

## Future Enhancements
- Adding a **Graphical User Interface (GUI)** for better user interaction.
- Integrating a **payment gateway** for handling online transactions.
- Expanding the system to manage multiple hotel branches.

## Contribution
Feel free to fork this project, submit issues, or contribute through pull requests. All contributions are welcome!
