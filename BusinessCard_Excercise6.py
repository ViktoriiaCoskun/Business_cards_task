from faker import Faker

class BaseContact:

    def __init__(self,name, surname,phone_number, email_address):
        self.name= name
        self.surname=surname
        self.phone_number=phone_number
        self.email_address=email_address

    def __str__(self):
        return f'{self.name} {self.surname} {self.email_address}'
#Both types of business cards should offer a method contact()that will display a message on the console with the content
#  "I am dialing +48 123456789 and calling Ihor Shevchenko". When choosing
#  a corporate business card, you should choose a working phone number, and when choosing a basic business card, you should choose a personal number.
    def contact (self):
        return f'I am dialing {self.phone_number} and calling {self.name} {self.surname}'

#Both types of business cards must have a dynamic attribute label_length that returns the length of the person's first and last name.
    @property
    def label_length(self):
        return len(self.name)+len(self.surname)+1

class BusinessContact(BaseContact):
    def __init__(self,name, surname,phone_number, email_address, position, company_name, work_phone):
       super().__init__(name, surname,phone_number, email_address)
       self.position=position
       self.company_name=company_name
       self.work_phone=work_phone

#Both types of business cards should offer a method contact()that will display a message on the console with the content
#  "I am dialing +48 123456789 and calling Ihor Shevchenko". When choosing
#  a corporate business card, you should choose a working phone number, and when choosing a basic business card, you should choose a personal number.
    def contact (self):
       return f'I am dialing {self.work_phone} and calling {self.name} {self.surname}'
 
businessContactList=[] 
baseContactList=[]

# Create a function create_contacts that can combine random business cards. 
# Let this function accept two parameters: the type of business card and the number. Use the library fakerto create data.
def create_contacts(card_type,number):

    faker = Faker(locale="pl_PL")
    person_name=faker.name().split()
    if (card_type=="BusinessContact"):
        
        person=BusinessContact(
                name=person_name[0],
                surname=person_name[1],
                company_name=faker.company(),
                position=faker.job(),
                email_address=person_name[0]+"."+person_name[1]+"@gmail.com",
                phone_number=faker.phone_number(),
                work_phone=number
                    )
        businessContactList.append(person)  
    elif(card_type=="BaseContact"):
        person=BaseContact(

            name=person_name[0],
            surname=person_name[1],
            email_address=person_name[0]+"."+person_name[1]+"@gmail.com",
            phone_number=number
            )
        baseContactList.append(person) 

for index in range(3):
    faker = Faker(locale="pl_PL")
    create_contacts("BusinessContact",faker.phone_number()) 
    create_contacts("BaseContact",faker.phone_number())  

for index in range(3):
    print(businessContactList[index].contact())
    print("label_length=",businessContactList[index].label_length)

    print(baseContactList[index].contact())
    print("label_length=",baseContactList[index].label_length)

         #previous exercises:

for index in range(len(businessContactList)):
    print(index+1,":",businessContactList[index].name,businessContactList[index].surname,businessContactList[index].email_address)

by_name = sorted(businessContactList, key=lambda person:person.name)
by_surname = sorted(businessContactList, key=lambda person:person.surname)
by_email = sorted(businessContactList, key=lambda person:person.email_address)

print("By Name:")
for index in range(len(businessContactList)):
    print(index,by_name[index])

print("By Surname:")
for index in range(len(businessContactList)):
    print(index,by_surname[index])

print("By Email:")
for index in range(len(businessContactList)):
    print(index,by_email[index])


