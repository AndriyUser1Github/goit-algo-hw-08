import re
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"
    
    def setValue(self, value: str):
        self.value = value


class Name(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Phone(Field):
    def __init__(self, value = None):
        super().__init__(value)

    def format_phone(self, value):
        number_pattern = r"[\d\+]+"
        number_phone = "".join(re.findall(number_pattern, value))
        if len(number_phone) == 10:
            phone_number = "+38" + number_phone
            return phone_number
        elif len(number_phone) == 11 and number_phone.startswith("8"):
            phone_number = "+3" + number_phone
            return phone_number
        elif len(number_phone) == 12 and number_phone.startswith("38"):
            return phone_number
        elif len(number_phone) == 13 and number_phone.startswith("+38"):
            return phone_number
        else:
            raise ValueError

        
class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d-%m-%Y").date()
        except ValueError:
            print(f"Помилка вводу: {ValueError}")
            self.value = None
            raise ValueError("Не вірна дата. Формат дати: ДД-ММ-РРРР")
        
     


        






    

    

        

    



