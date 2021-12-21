from prettytable import PrettyTable
import Validator

class View:
    def __init__(self):
        self.valid = Validator.Validator()

    def list(self):
        print('''
        1 -> Apartment
        2 -> Building
        3 -> Company
        4 -> Person
        ''')

    def CheckTable(self):
        flag = True
        while flag:
            table = input('Choose number of table -> ')
            if table.isdigit():
                table = int(table)
                if table >= 1 and table <= 4:
                    flag = False
                else:
                    print('Wrong number, choose again.')
            else:
                print('Wrong number, choose again.')
        return table

    def print_Apartment(self, table):
        PTables = PrettyTable()
        PTables.field_names = ["id_apartment", "floor", "number", "number_of_rooms", "id_person", "id_building"]
        for row in table:
            PTables.add_row([row.id_apartment, row.floor, row.number, row.number_of_rooms, row.id_person, row.id_building]);
        print('Apartment table:')
        print(PTables)

    def print_Building(self, table):
        PTables = PrettyTable()
        PTables.field_names = ["id_building", "adress", "number_of_apartments", "number_of_floors", "Company_name"]
        for row in table:
            PTables.add_row([row.id_building, row.adress, row.number_of_apartments, row.number_of_floors, row.Company_name]);
        print('Building table:')
        print(PTables)

    def print_Company(self, table):
        PTables = PrettyTable()
        PTables.field_names = ["Company_name", "adress", "phone"]
        for row in table:
            PTables.add_row([row.Company_name, row.adress, row.phone]);
        print('Company table:')
        print(PTables)

    def print_Person(self, table):
        PTables = PrettyTable()
        PTables.field_names = ["id_person", "name", "surname", "patronymic", "phone", "Company_name"]
        for row in table:
            PTables.add_row([row.id_person, row.name, row.surname, row.patronymic, row.phone, row.Company_name]);
        print('Person table:')
        print(PTables)

    def delete_Apartment(self):
        id_apartment = input("id_apartment of row for deletion = ")
        return id_apartment

    def delete_Building(self):
        id_building = input("id_building of row for deletion = ")
        return id_building

    def delete_Company(self):
        Company_name = input("Company_name of row for deletion = ")
        return Company_name

    def delete_Person(self):
        id_person = input("id_person of row for deletion = ")
        return id_person

    def insert_update_Apartment(self):
        print('Enter new value of attribute')
        id_apartment = input('"id_apartment"=')
        floor = input('"floor"=')
        number = input('"number"=')
        number_of_rooms = input('"number_of_rooms"=')
        id_person = input('"id_person"=')
        id_building = input('"id_building"=')
        return id_apartment, floor, number, number_of_rooms, id_person, id_building

    def insert_update_Building(self):
        print('Enter new value of attribute')
        id_building = input('"id_building"=')
        adress = input('"adress"=')
        number_of_apartments = input('"number_of_apartments"=')
        number_of_floors = input('"number_of_floors"=')
        Company_name = input('"Company_name"=')
        return id_building, adress, number_of_apartments, number_of_floors, Company_name
    
    def insert_update_Company(self):
        print('Enter new value of attribute')
        Company_name = input('"Company_name"=')
        adress = input('"adress"=')
        phone = input('"phone"=')
        return Company_name, adress, phone

    def insert_update_Person(self):
        print('Enter new value of attribute')
        id_person = input('"id_person"=')
        name = input('"name"=')
        surname = input('"surname"=')
        patronymic = input('"patronymic"=')
        phone = input('"phone"=')
        Company_name = input('"Company_name"=')
        return id_person, name, surname, patronymic, phone, Company_name

    def mainmenu(self):
        print('''
                Menu
        1 -> Show one table
        2 -> Show all table
        3 -> Insert data
        4 -> Delete data
        5 -> Update data
        6 -> Exit''')

        choice = input('\nSelect from 1 to 6 -> ')

        if (not choice.isdigit() or int(choice)<1 or int(choice)>6):
            print('\nWrong number, choose again.')
        else:
            return choice

    def Print_error(self, er):
        print("Error: ", er)