# Expense Tracker

## Author: Samuel Muli

This Expense Tracker is a command-line application that allows users to manage their expenses. It is built using Python and SQLAlchemy for database interactions. Users can create accounts, add categories, record expenses and view/delete their expense history.

## Installation

1. Clone the repository

`git clone git@github.com:Samstar10/Expense-tracker-CLI.git`

2. Install the required dependencies

`pipenv install`

## Usage

### Creating a User

To create a user, run the following command:

`python3 app.py create-user <username> <password>`

Replace `<username>` and `<password>` with the desired values.

### Adding Categories

To add a category, use the following command:

`python3 app.py add-category <category_name>`

### Deleting a Category

To delete a category, run the command:

`python3 app.py delete-category <category_name>`

### Logging in

To log in, use the following command:

`python3 app.py login <username> <password>`

### Adding an Expense

To add an expense, run the command:

`python3 app.py add-expense --user=<username> <amount> <description> --category=<category>`

### Viewing Expenses

To view expenses, run:

`python3 app.py view-expenses --user=<username>`

### Deleting an Expense

To delete an expense, use the command:

`python3 app.py delete-expense --user=<username> <expense_id>`


## Contributing

1. Fork the repository.
2. Clone the repository.
3. Install dependencies by running `pipenv install`.
4. Create branch using `git checkout -b new-feature`.
5. Make a pull request.

### NB
User passwords are securely stored using the bcrypt hashing algorithm.