# Coffee Shop Domain Model

## About

This is a Python project that models a simple coffee shop system. It simulates how customers order coffee and how those relationships are tracked. The main goal was to practice object-oriented programming (OOP) concepts in a practical way.

---

## Key Concepts

- Object-oriented programming
- Many-to-many relationships using an intermediary class
- Input validation and error handling
- Simple business logic like average prices and top-spending customers

---

## Classes

- **Customer** – Represents someone placing coffee orders.
- **Coffee** – A coffee item available to order.
- **Order** – Connects a customer and a coffee, including the price.

---

## How It Works

After setup, you can use the `debug.py` file to simulate real-world usage by creating customers, adding coffees, and placing orders.

You can also:

- View all coffees ordered by a customer
- See how many times a coffee has been ordered
- Calculate average price per coffee
- Identify the customer who spent the most on a particular coffee

---

## Running the App

1. Install dependencies:
   ```bash
   pipenv install
   pipenv shell
   Run the script:
   ```


You’ll see output based on the objects and relationships you create.



Names and prices are validated to ensure data integrity.

Helper methods are used to keep logic clean and reusable.

Could be extended later to include a database or user interface.
