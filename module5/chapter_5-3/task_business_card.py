from faker import Faker
import datetime

fake = Faker("pl_PL")

class BaseContact:
    def __init__(self, name, surname, e_mail, phone):
        self.name = name
        self.surname = surname
        self.e_mail = e_mail
        self.phone = phone

    @property
    def label_length(self):
        return len(self.name) + len(self.surname) + 1

    def contact(self):
        return f"I dial the number {self.phone} and call to {self.name} {self.surname}"

    def __str__(self):
        return f"{self.name} {self.surname}, e-mail: {self.e_mail}, phone: {self.phone}"


class BusinessContact(BaseContact):
    def __init__(self, business_phone, position, company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_phone = business_phone
        self.position = position
        self.company = company

    def contact(self):
        return f"I dial the number {self.business_phone} and call to {self.name} {self.surname}, company {self.company}"

    def __str__(self):
        return f"{self.name} {self.surname}, {self.position} in {self.company}\ne-mail: {self.e_mail}, phone: {self.phone}, business phone: {self.business_phone}"


def create_contact(contact_type):
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone = fake.phone_number()
    company = fake.company()

    if issubclass(contact_type, BusinessContact):
        return BusinessContact(
            name=first_name,
            surname=last_name,
            company=company,
            position=fake.job(),
            e_mail=fake.company_email(),
            phone=phone,
            business_phone=fake.phone_number()
        )
    else:
        return BaseContact(
            name=first_name,
            surname=last_name,
            e_mail=fake.email(),
            phone=phone
        )

def creation_time(function):
    def inter_function(*args):
        start = datetime.datetime.now()
        result = function(*args)
        duration = datetime.datetime.now() - start
        return result, duration.total_seconds()

    return inter_function


@creation_time
def create_contact_list(contact_type, amount):
    card_list = []
    for i in range(amount):
        card_list.append(create_contact(contact_type))
    return card_list


business_contact_list, time_business = create_contact_list(BusinessContact, 2)
base_contact_list, time_basic = create_contact_list(BaseContact, 3)

for item in business_contact_list:
    print(item)
    print(item.contact())
print(f"Time for create business contact list is: {time_business} seconds")

for item in base_contact_list:
    print(item)
    print(item.contact())
print(f"Time for create basic contact list is: {time_basic} seconds")