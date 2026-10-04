import csv
import os
from datetime import datetime


expenses = []


# ---------- VALIDATE DATE ----------
def get_valid_date():
    while True:
        date = input("Enter the Date (DD-MM-YYYY): ")

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date

        except ValueError:
            print("Invalid date!")
            print("Please enter date in DD-MM-YYYY format.")


# ---------- VALIDATE AMOUNT ----------
def get_valid_amount():
    while True:
        amount = input("Enter the amount: ")

        if amount.isdigit():
            return int(amount)

        else:
            print("Invalid amount!")
            print("Please enter only integers.")


# ---------- VALIDATE MENU CHOICE ----------
def get_valid_choice():
    while True:
        choice = input("Enter your choice (1-7): ")

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            return choice

        else:
            print("Invalid choice!")
            print("Please enter a number from 1 to 7.")


# ---------- MAIN PROGRAM ----------
while True:

    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Category Total")
    print("7. Exit")

    choice = get_valid_choice()


    # ==================================================
    # 1. ADD EXPENSE
    # ==================================================

    if choice == "1":

        date = get_valid_date()

        category = input("Enter the category: ")

        description = input("Enter the description: ")

        amount = get_valid_amount()

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

        file_exists = os.path.exists("expenses.csv")

        if not file_exists:

            with open("expenses.csv", "a", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "date",
                    "category",
                    "description",
                    "amount"
                ])

        with open("expenses.csv", "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                expense["date"],
                expense["category"],
                expense["description"],
                expense["amount"]
            ])

        print("Expense added successfully!")


    # ==================================================
    # 2. VIEW EXPENSES
    # ==================================================

    elif choice == "2":

        if not os.path.exists("expenses.csv"):

            print("No expenses found.")

        else:

            with open("expenses.csv", "r") as file:

                reader = csv.reader(file)

                next(reader)

                found = False

                print("\n----- EXPENSES -----")

                for row in reader:

                    if row:

                        found = True

                        print("Date:", row[0])
                        print("Category:", row[1])
                        print("Description:", row[2])
                        print("Amount:", row[3])
                        print("--------------------")

                if not found:

                    print("No expenses found.")


    # ==================================================
    # 3. CALCULATE TOTAL
    # ==================================================

    elif choice == "3":

        if not os.path.exists("expenses.csv"):

            print("No expenses found.")

        else:

            total = 0
            found = False

            with open("expenses.csv", "r") as file:

                reader = csv.reader(file)

                next(reader)

                for row in reader:

                    if row:

                        found = True

                        total += int(row[3])

            if found:

                print("Total Expense:", total)

            else:

                print("No expenses found.")


    # ==================================================
    # 4. EDIT EXPENSE
    # ==================================================

    elif choice == "4":

        if not os.path.exists("expenses.csv"):

            print("No expenses found.")

        else:

            description = input(
                "Enter the description of the expense to edit: "
            )

            found = False
            rows = []

            with open("expenses.csv", "r") as file:

                reader = csv.reader(file)

                header = next(reader)

                for row in reader:

                    if row:

                        if row[2].lower() == description.lower():

                            print("Current amount:", row[3])

                            new_amount = get_valid_amount()

                            row[3] = str(new_amount)

                            found = True

                        rows.append(row)

            if found:

                with open(
                    "expenses.csv",
                    "w",
                    newline=""
                ) as file:

                    writer = csv.writer(file)

                    writer.writerow(header)

                    for row in rows:

                        writer.writerow(row)

                print("Expense updated successfully!")

            else:

                print("Expense not found!")

                print(
                    "Please enter a description "
                    "that exists in your expenses."
                )


    # ==================================================
    # 5. DELETE EXPENSE
    # ==================================================

    elif choice == "5":

        if not os.path.exists("expenses.csv"):

            print("No expenses found.")

        else:

            description = input(
                "Enter the description of the expense to delete: "
            )

            found = False
            rows = []

            with open("expenses.csv", "r") as file:

                reader = csv.reader(file)

                header = next(reader)

                for row in reader:

                    if row:

                        if row[2].lower() == description.lower():

                            found = True

                        else:

                            rows.append(row)

            if found:

                with open(
                    "expenses.csv",
                    "w",
                    newline=""
                ) as file:

                    writer = csv.writer(file)

                    writer.writerow(header)

                    for row in rows:

                        writer.writerow(row)

                print("Expense deleted successfully!")

            else:

                print("Expense not found!")

                print(
                    "Please enter a description "
                    "that exists in your expenses."
                )


    # ==================================================
    # 6. CATEGORY TOTAL
    # ==================================================

    elif choice == "6":

        if not os.path.exists("expenses.csv"):

            print("No expenses found.")

        else:

            category = input(
                "Enter the category: "
            )

            category_total = 0
            found = False

            with open("expenses.csv", "r") as file:

                reader = csv.reader(file)

                next(reader)

                for row in reader:

                    if row:

                        if row[1].lower() == category.lower():

                            category_total += int(row[3])

                            found = True

            if found:

                print("Category:", category)

                print(
                    "Category Total:",
                    category_total
                )

            else:

                print("Category not found!")

                print(
                    "Please enter a category "
                    "that exists in your expenses."
                )


    # ==================================================
    # 7. EXIT
    # ==================================================

    elif choice == "7":

        print(
            "Thank you for using "
            "Personal Expense Tracker!"
        )

        break
                             