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


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    cli()