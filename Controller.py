import Model
import View
from psycopg2 import Error

class Controller:
    def __init__(self):
        self.View = View.View()
        self.Model = Model.Model()

    def mainmenu(self):
        exit = False
        while not exit:
            choice = self.View.mainmenu()
            if choice == '1':
                self.showOneTable()
            elif choice == '2':
                self.showAllTables()
            elif choice == '3':
                self.View.list()
                table = self.View.CheckTable()
                if(table == 1):
                    self.insert_Apartment()
                elif (table == 2):
                    self.insert_Building()
                elif (table == 3):
                    self.insert_Company()
                elif (table == 4):
                    self.insert_Person()
            elif choice == '4':
                self.View.list()
                table = self.View.CheckTable()
                if(table == 1):
                    self.delete_Apartment()
                elif (table == 2):
                    self.delete_Building()
                elif (table == 3):
                    self.delete_Company()
                elif (table == 4):
                    self.delete_Person()
            elif choice == '5':
                self.View.list()
                table = self.View.CheckTable()
                if(table == 1):
                    self.update_Apartment()
                elif (table == 2):
                    self.update_Building()
                elif (table == 3):
                    self.update_Company()
                elif (table == 4):
                    self.update_Person()
            elif choice == '6':
                exit = True

    def showOneTable(self):
        self.View.list()
        table = self.View.CheckTable()
        if table == 1:
            self.View.print_Apartment(self.Model.print_Apartment())
        elif table == 2:
            self.View.print_Building(self.Model.print_Building())
        elif table == 3:
            self.View.print_Company(self.Model.print_Company())
        elif table == 4:
            self.View.print_Person(self.Model.print_Person())

    def showAllTables(self):
        self.View.print_Apartment(self.Model.print_Apartment())
        self.View.print_Building(self.Model.print_Building())
        self.View.print_Company(self.Model.print_Company())
        self.View.print_Person(self.Model.print_Person())

    def insert_Apartment(self):
        id_apartment, floor, number, number_of_rooms, id_person, id_building = self.View.insert_update_Apartment()
        int_id_apartment = self.View.valid.check_value(id_apartment)
        int_floor = self.View.valid.check_value(floor)
        int_number = self.View.valid.check_value(number)
        int_number_of_rooms = self.View.valid.check_value(number_of_rooms)
        int_id_person = self.View.valid.check_value(id_person)
        int_id_building = self.View.valid.check_value(id_building)
        if int_id_apartment and int_floor and int_number and int_number_of_rooms:
            if self.Model.find_pk_Person(int_id_person) and self.Model.find_pk_Building(int_id_building):
                try:
                    self.Model.insert_Apartment(int_id_apartment, int_floor, int_number, int_number_of_rooms, int_id_person, int_id_building)
                except (Exception, Error) as er:
                    self.View.Print_error(er)
            else:
                er = "Cann`t find record"
                self.View.Print_error(er)

    def insert_Building(self):
        id_building, adress, number_of_apartments, number_of_floors, Company_name = self.View.insert_update_Building()
        int_id_building = self.View.valid.check_value(id_building)
        int_number_of_apartments = self.View.valid.check_value(number_of_apartments)
        int_number_of_floors = self.View.valid.check_value(number_of_floors) 
        if int_id_building and int_number_of_apartments and int_number_of_floors:
            if self.Model.find_pk_Company(Company_name):
                try:
                    self.Model.insert_Building(int_id_building, adress, int_number_of_apartments, int_number_of_floors, Company_name)
                except (Exception, Error) as er:
                    self.View.Print_error(er)
            else:
                er = "Cann`t find record"
                self.View.Print_error(er)

    def insert_Company(self):
        Company_name, adress, phone = self.View.insert_update_Company()
        try:
            self.Model.insert_Company(Company_name, adress, phone)
        except (Exception, Error) as er:
            self.View.Print_error(er)

    def insert_Person(self):
        id_person, name, surname, patronymic, phone, Company_name = self.View.insert_update_Person()
        int_id_person = self.View.valid.check_value(id_person)
        if int_id_person:
            if self.Model.find_pk_Company(Company_name):
                try:
                    self.Model.insert_Person(int_id_person, name, surname, patronymic, phone, Company_name)
                except (Exception, Error) as er:
                    self.View.Print_error(er)
            else:
                er = "Cann`t find record"
                self.View.Print_error(er)

    def delete_Apartment(self):
        id_apartment = self.View.delete_Apartment()
        int_id_apartment = self.View.valid.check_value(id_apartment)
        if int_id_apartment:
            if self.Model.find_pk_Apartment(int_id_apartment):
                try:
                    self.Model.delete_Apartment(int_id_apartment)
                except (Exception, Error) as er:
                    self.View.Print_error(er)
            else:
                er = "Cann`t find record"
                self.View.Print_error(er)

    def delete_Building(self):
        id_building = self.View.delete_Building()
        int_id_building = self.View.valid.check_value(id_building)
        if int_id_building:
            if self.Model.find_pk_Building(int_id_building):
                new_check = self.Model.find_fk_Apartment(int_id_building, "Building")
                if new_check:
                    er = "This record is connected with another table"
                    self.View.Print_error(er)
                else:
                    try:
                        self.Model.delete_Building(int_id_building)
                    except (Exception, Error) as er:
                        self.View.Print_error(er)
            else:
                er = "Cann`t find record"
                self.View.Print_error(er)

    def delete_Company(self):
        Company_name = self.View.delete_Company()
        if self.Model.find_pk_Company(Company_name):
            if self.Model.find_fk_Building(Company_name) or self.Model.find_fk_Person(Company_name):
                er = "This record is connected with another table"
                self.View.Print_error(er)
            else:
                try:
                    self.Model.delete_Company(Company_name)
                except (Exception, Error) as er:
                    self.View.Print_error(er)
        else:
            er = "Cann`t find record"
            self.View.Print_error(er)

    def delete_Person(self):
        id_person = self.View.delete_Person()
        int_id_person = self.View.valid.check_value(id_person)
        if int_id_person:
            if self.Model.find_pk_Person(int_id_person):
                if self.Model.find_fk_Apartment(int_id_person, "Person"):
                    er = "This record is connected with another table"
                    self.View.Print_error(er)
                else:
                    try:
                        self.Model.delete_Person(int_id_person)
                    except (Exception, Error) as er:
                        self.View.Print_error(er)
            else:
                er = "Cann`t find record"
                self.View.Print_error(er)

    def update_Apartment(self):
        id_apartment, floor, number, number_of_rooms, id_person, id_building = self.View.insert_update_Apartment()
        int_id_apartment = self.View.valid.check_value(id_apartment)
        int_floor = self.View.valid.check_value(floor)
        int_number = self.View.valid.check_value(number)
        int_number_of_rooms = self.View.valid.check_value(number_of_rooms)
        int_id_person = self.View.valid.check_value(id_person)
        int_id_building = self.View.valid.check_value(id_building)
        if int_floor and int_number and int_number_of_rooms:
            if self.Model.find_pk_Apartment(int_id_apartment) and self.Model.find_pk_Person(int_id_person) and self.Model.find_pk_Building(int_id_building):
                try:
                    self.Model.update_Apartment(int_id_apartment, int_floor, int_number, int_number_of_rooms, int_id_person, int_id_building)
                except (Exception, Error) as er:
                    self.View.Print_error(er)
            else:
                er = "Cann`t find record"
                self.View.Print_error(er)

    def update_Building(self):
        id_building, adress, number_of_apartments, number_of_floors, Company_name = self.View.insert_update_Building()
        int_id_building = self.View.valid.check_value(id_building)
        int_number_of_apartments = self.View.valid.check_value(number_of_apartments)
        int_number_of_floors = self.View.valid.check_value(number_of_floors) 
        if int_number_of_apartments and int_number_of_floors:
            if self.Model.find_pk_Building(int_id_building) and self.Model.find_pk_Company(Company_name):
                try:
                    self.Model.update_Building(int_id_building, adress, int_number_of_apartments, int_number_of_floors, Company_name)
                except (Exception, Error) as er:
                    self.View.Print_error(er)
            else:
                er = "Cann`t find record"
                self.View.Print_error(er)

    def update_Company(self):
        Company_name, adress, phone = self.View.insert_update_Company()
        if self.Model.find_pk_Company(Company_name):
            try:
                self.Model.update_Company(Company_name, adress, phone)
            except (Exception, Error) as er:
                self.View.Print_error(er)
        else:
            er = "Cann`t find record"
            self.View.Print_error(er)

    def update_Person(self):
        id_person, name, surname, patronymic, phone, Company_name = self.View.insert_update_Person()
        int_id_person = self.View.valid.check_value(id_person)
        if self.Model.find_pk_Person(int_id_person) and self.Model.find_pk_Company(Company_name):
            try:
                self.Model.update_Person(int_id_person, name, surname, patronymic, phone, Company_name)
            except (Exception, Error) as er:
                self.View.Print_error(er)
        else:
            er = "Cann`t find record"
            self.View.Print_error(er)