import psycopg2
import db
import os
import csv

db.init()
app = True

def app_add_contact():
    print('Enter name: ', end='')
    name = input()
    print('Enter phone: ', end='')
    phone = input()
    print('Enter category ("none" for not to add): ', end='')
    cat = input()
    if all([name, phone, cat]):
        db.add_contact(([name, phone, cat],))
        print('Contact have been added!')
    else:
        print('Enter all data!')

def app_add_contact_csv():
    csv_s = os.listdir('csv-files')
    print('Files:')
    for i in range(len(csv_s)):
        print(f'{i+1}. {csv_s[i]}')

    print('Enter number of file: ', end='')
    number = int(input()) - 1
    with open('csv-files/'+csv_s[number], newline='') as File:  
        reader = csv.reader(File)
        data = []
        for row in reader:
            data.append(row)
        print(data)
        db.add_contact(data)
        print('Contacts have been added!')


def app_update_contact():
    print('Enter ID of contact: ', end='')
    id_contact = input()
    con = db.get_by_ID(id_contact)
    if not con:
        print(f'Contact with ID[{id_contact}] not found!')
        return
    
    a, name, phone, cat = con

    print('--If you do not want to change the field, then leave it blank--')
    new_name = input(f'Enter name ({name}) : ') or name
    new_phone = input(f'Enter phone ({phone}) : ') or phone
    new_cat = input(f'Enter category ({cat}) : ') or cat
    db.update_contact(id_contact, new_name, new_phone, new_cat)
    print('Contact have been updated!')

def app_delete_contact():
    print('Enter ID of contact: ', end='')
    id_contact = input()
    con = db.get_by_ID(id_contact)
    if not con:
        print(f'Contact with ID[{id_contact}] not found!')
        return
    
    print(f'Are you sure you want to delete a contact({con[1]}) ? Y/n')
    ans = input()
    if ans in ('Y', 'y'):
        db.delete_contact(id_contact)
        print('Contact have been deleted!')

def app_get_contacts():
    print('\n'*2)
    all_con = []
    print('Do you want to use a filter? Y/n')
    ans = input()
    if ans in ('Y', 'y'):
        print('Enter type(name, phone or category): ', end='')
        type = input()
        print('Enter value: ', end='')
        value = input()
        all_con = db.get_contacts({'type': type, 'value': value.lower()})
    else:
        all_con = db.get_contacts()

    if all_con:
        print('Contacts\n===================================================')
        print('ID    Name                     Phone            Category')
        print('----  -----------------------  ---------------  -------------')

        id_len = 4
        name_len = 23
        phone_len = 15
        cat_len = 13
        for contact in all_con:
            id = str(contact[0])
            name = contact[1]
            phone = contact[2]
            cat = contact[3]

            id_space = id_len - len(id)
            print(id+' '*id_space, end='  ')

            name_space = name_len - len(name)
            print(name+' '*name_space, end='  ')

            phone_space = phone_len - len(phone)
            print(phone+' '*phone_space, end='  ')

            cat_space = cat_len - len(cat)
            print(cat+' '*cat_space)
    else:
        print('You dont have any contacts :(')
        print('Want to add? Y/n')
        ans = input()
        if ans in ('Y', 'y'):
            app_add_contact()
            print('Contact have been added!\n')



def app_choice():
    print('\n'*2)
    print('What do you want to do?')
    print('all - Return all contacts')
    print('add - Add new contact')
    print('add_csv - Add new contact from csv-file')
    print('update - Update contact')
    print('delete - Delete contact')
    print('exit - Exit from app')
    ans = input()
    if ans == 'all': app_get_contacts()
    elif ans == 'add': app_add_contact()
    elif ans == 'add_csv': app_add_contact_csv()
    elif ans == 'update': app_update_contact()
    elif ans == 'delete': app_delete_contact()
    elif ans == 'exit':
        print('Goodbye!')
        db.close()
        exit()
    else: print('Invalid input')

print('Welcome to Console Phone Book!')
#print(db.call_func('find_with_pattern', ('a',)))
print(db.call_proc('Lol','1234567'))
exit()
while app:
    app_choice()
