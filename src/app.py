import argparse
from . import pm


def read_input(help: str, optional: bool = False) -> str:
    data = input(help)
    if data != '' or optional:
        return data
    return read_input(help)


def main():
    parser = argparse.ArgumentParser(
        description='You can manage your passwords with this minimal password manager app:)')

    subparsers = parser.add_subparsers(dest='operation', help='Available operations')

    # Create a sub-parser for the 'add' operation
    add_parser = subparsers.add_parser('add', help='Add new record')
    add_parser.add_argument('--name', type=str, help='Name of new record')
    add_parser.add_argument('--url', type=str, help='URL of new record')
    add_parser.add_argument('--username', type=str, help='Username of new record')
    add_parser.add_argument('--password', type=str, help='Password of new record')

    # Create a sub-parser for the 'subtract' operation
    find_parser = subparsers.add_parser('find', help='Find a record based on name')
    find_parser.add_argument('--name', type=str, help='Name of record')

    args = parser.parse_args()

    if args.operation == 'add':
        name = args.name or read_input("Please enter the name of the record: ")
        url = args.name or read_input("Please enter the URL of the record: ", optional=True)
        username = args.username or read_input("Please enter the username of the record: ")
        password = args.password or read_input("Please enter the password of the record: ")
        pm.add(name=name, url=url, username=username, password=password)

    if args.operation == 'find':
        name = args.name or read_input("Please enter the name of record that you are looking for: ")
        pm.fetch(name=name)
