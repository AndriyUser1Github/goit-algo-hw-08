from Recordbot import record as rec
from collections import UserDict


class AddressBook(UserDict):
    def getBook(self):
        titles_column = ("Ім'я", "Тел", "День народження")
        column_width = 12
        column_1 = f"{titles_column[0]:<{column_width}}"
        column_2 = f"{titles_column[1]:<{column_width} * 2}"
        column_3 = f"{titles_column[2]:<{column_width}}"
        lines = "|" + column_1 + "|" + column_2 + "|" + column_3 + "|\n"
        lines += "-" * len(lines) + "\n"
        for elem in self.data.items():
            first_value = f"{elem[0].value:<{column_width}}"
            second_value = f"{'; '.join(p.value for p in elem[1].phones):<{column_width * 2}}"
            third_value = f"{str(elem[1].birthday):<{column_width}}"
            lines += "|" + first_value + "|" + second_value + "|" + third_value + "|\n"
        return lines


    def add_record(self, record: rec.Record):
        self.data[record.name.value] = record


    def find_record(self, owners_name: str):
        for name, phone in self.data.items():
            if name == owners_name:
                return f"Номер телефону: {phone}"
            
    
    def delete_record(self, owners_name):
        for owners_name in self.data:
            del self.data[owners_name]
            return f"Контакт з іменем {owners_name} видалено"
        





