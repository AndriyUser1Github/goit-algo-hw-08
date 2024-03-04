from Fieldbot import field


class Record:
    def __init__(self, name):
        self.name = field.Name(name)
        self.phones = []
        self.birthday = None


    def __str__(self):
        if self.birthday:
            return f"(Ім'я контакту: {self.name.value},\
                Дата народження: {self.birthday}\
                Телефоні номери: {'; '.join(phone for phone in self.phones)})"
        else:
            return f"(Ім'я контакту: {self.name.value},\
                Телефоні номери: {'; '.join(phone for phone in self.phones)})"
     
        
    def add_phone(self, number):
        phone_number = field.Phone.format_phone(number)
        if phone_number in self.phones:
            raise ValueError("Такий номер вже існує")
        else:
            self.phones.append(field.Phone.format_phone(number))


    def edit_phone(self, phone_number: str, redacted_phone_number: str):
        phone_number = field.Phone.format_phone(phone_number)
        redacted_phone_number = field.Phone.format_phone(redacted_phone_number)
        if phone_number in self.phones:
            selected_phone_number = self.phones.index(phone_number)
            self.phones[selected_phone_number] = redacted_phone_number
            return "Номер телефону змінено"
        else:
            return "Номер телефону не знайдено"


    def find_phone(self, number):
        phone_number= field.Phone.format_phone(number)
        return (phone_number if phone_number in self.phones else f"{phone_number} не знайдено")
    

    def remove_phone(self, number):
        phone_number = field.Phone.format_phone(number)
        if phone_number in self.phones:
            self.phones.remove(phone_number)


    def add_birthday(self, birthday):
        if field.Birthday(birthday):
            self.birthday = birthday
            return f"(Для контакту {self.name} додано дату народження {birthday})"
   