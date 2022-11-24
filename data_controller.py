import subprocess as sp
from database_action import *

create_table()

def add_data(id_, name, phone):
    add_user(id_, name, phone)


def get_data():
    return get_user()


def show_data():
    users = get_data()
    for user in users:
        print(user)


def show_data_by_id(id_):
    users = get_user_by_roll(id_)
    if not users:
        print("No data found at roll", id_)
    else:
        print(users)


def select():
    sp.call("clear", shell=True)
    sel = input("1. Add data\n2.Show Data\n3.Search\n4.Update\n5.Delete\n6.Exit\n\n")

    if sel == '1':
        sp.call("clear", shell=True)
        id_input = input('id: ')
        if not id_input.isdigit():
            input("\n\nWrong data type. ID must be integer. Please try again")
            return 1;
        name = input('Name: ')
        phone = input('phone: ')
        add_data(id, name, phone)
    elif sel == '2':
        sp.call('clear', shell=True)
        show_data()
        input("\n\npress enter to back:")
    elif sel == '3':
        sp.call('clear', shell=True)
        id__ = int(input('Enter Id: '))
        show_data_by_id(id__)
        input("\n\npress enter to back:")
    elif sel == '4':
        sp.call('clear', shell=True)
        id__ = int(input('Enter Id: '))
        show_data_by_id(id__)
        print()
        name = input('Name: ')
        phone = input('phone: ')
        update_user(id__, name, phone)
        input("\n\nYour data has been updated \npress enter to back:")
    elif sel == '5':
        sp.call('clear', shell=True)
        id__ = int(input('Enter Id: '))
        show_data_by_id(id__)
        delete_user(id__)
        input("\n\nYour data has been deleted \npress enter to back:")
    else:
        return 0;
    return 1;