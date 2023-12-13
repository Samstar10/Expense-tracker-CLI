import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Category, Expense

engine = create_engine('sqlite:///expense_tracker.db')
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('username')
@click.argument('password')
def create_user(username, password):
    session = Session()
    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    print(f"User {username} has been created successfully.")

@cli.command()
@click.argument('username')
@click.argument('password')
def login(username, password):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user and user.password == password:
        print(f"Logged in as {username}.")
    else:
        print("Invalid username or password.")

@cli.command()
@click.option('--user', prompt='Username', help='Username of the logged-in user')
@click.argument('amount')
@click.argument('description')
@click.option('--category', prompt='Category', help='Category of the expense')
def add_expense(user, amount, description, category):
    session = Session()
    user_obj = session.query(User).filter_by(username=user).first()
    if user_obj:
        category_obj = session.query(Category).filter_by(name=category).first()
        if category_obj:
            expense = Expense(amount=amount, description=description, user=user_obj, category=category_obj)
            session.add(expense)
            session.commit()
            print("Expense added successfully.")
        else:
            print(f"Category '{category}' does not exist. Please create the category first.")
    else:
        print(f"User '{user}' does not exist. Please create an account first.")




if __name__ == '__main__':
    Base.metadata.create_all(engine)
    cli()