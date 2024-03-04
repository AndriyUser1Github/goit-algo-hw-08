import pickle
from datetime import datetime, timedelta
from AddressBookbot import addressbook as adbk
from Recordbot import record as rec
from Fieldbot import field as fld


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return adbk.AddressBook() 

def save_data(book, filename="addressbook.pkl"): 
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    return "Дані змінено"

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):  
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдено"
        except ValueError:
            return "Не вірні дані" 
        except IndexError: 
            return "Не вірно введені дані"
        except SyntaxError: 
            return "Номер вже існує"
        except NameError:
            return "Таке ім'я вже існує"               
    return inner


@input_error
def show_contacts(args, contacts: adbk.AddressBook):
    name = args[0]
    record_find = contacts.find_record(name)
    if record_find:
        return record_find
    raise KeyError

@input_error                                           
def add_contact(args, contacts: adbk.AddressBook): 
    name, phone = args
    record_find = contacts.find_record(name)      
    if record_find:
        phone = fld.Phone(phone)
        record_find.add_phone(phone)
        contacts.add_record(record_find)
        return f'Існуючий контакт {name} оновлено'
    name = fld.Name(name)
    phone = fld.Phone(phone)
    new_record = rec.Record(name)
    new_record.add_phone(phone)
    contacts.add_record(new_record)
    return f'Контакт {name} додано'
             
@input_error   
def change_contact(args: str, contacts: adbk.AddressBook): 
    
    name, phone, new_phone  = args 
    phone = fld.Phone(phone)    
    if phone.value:
        record_find = contacts.find_record(name)         
        if record_find:
            record_find.edit_phone(record_find.phones[0].value, phone.value)
            return f"Контакт змінено"
    return "Не вірний номер телефону"

@input_error    
def del_contact(args: str, contacts: adbk.AddressBook): 
        name = args[0]
        contacts.delete_record(name)
        return f"Контакт видалено"
               
@input_error
def add_birthday(args:str, contacts: adbk.AddressBook):
    name = args[0]
    birthday = args[1]    
    record_find = contacts.find_record(name)
    if record_find:
        record_find.add_birthday(fld.Birthday(birthday))
        return f"До контакту додано дату нородження"
 
@input_error
def show_birthday(args:str, contacts: adbk.AddressBook):
    name = args[0]
    record_find = contacts.find_record(name)
    if record_find:
        return record_find.birthday.value.strftime("%d-%m-%Y")

@input_error
def birthdays (contacts: adbk.AddressBook):
    today = datetime.today().date()
    congratulation_list = []
    for contact in contacts.data.items():
        if contact[1].birthday:
            congratulation_dict = {}
            keys_dict = ("Ім'я", "Дата привітання")
            contact_birthday = contact[1].birthday.value
            if contact_birthday:
                birthday_this_year = datetime(year = today.year,\
                                            month = birthday_this_year.month,\
                                            day = birthday_this_year.day).date()
                if birthday_this_year < today:
                    continue
                elif birthday_this_year.toordinal() - today.toordinal() > 7:
                    continue
                else:
                    congratulation_date = datetime(year = today.year,\
                                                    month = birthday_this_year.month,\
                                                    day = birthday_this_year.day).date()
                    if congratulation_date.weekday() == 6:
                        congratulation_date += timedelta(days = 1)
                    elif congratulation_date.weekday() == 5:
                        congratulation_date += timedelta(days = 2)

                    congratulation_date = congratulation_date.strftime("%d-%m-%Y")
                    congratulation_dict.update({keys_dict[0]: contact[1].name,\
                                                keys_dict[1]: congratulation_date})
                    congratulation_list.append(congratulation_dict)
    if congratulation_list:
        return "\n".join(map(str, congratulation_list))
    return "На цьому тижні імениники відсутні"

        
