class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self,name,phone_number,email):
        cur_dict = {"name":name,"phone_number":phone_number,"email":email}
        self.contacts.append(cur_dict)
    def get_phone(self,name):
        for el in self.contacts:
            if el["name"] == name:
                print(el["phone_number"])
        print("added")
    def update_phone(self,name, phone_number):
        for el in self.contacts:
            if el["name"]== name:
                el["phone_number"]=phone_number
        print("updated")
    def delete_contact(self,name):
        for el in self.contacts:
            if el["name"]==name:
                self.contacts.remove(el)
        print("removed")
    def get_contacts(self):
        print(self.contacts)
contact1=ContactBook()
contact1.add_contact("yashika","72996628661","yashikaa292gmail.com")
contact1.add_contact("Aniruth","9674422555","aniruth29@gmail.com")
contact1.get_contacts()
contact1.get_phone("Aniruth")
contact1.update_phone("Aniruth","9677085823")
contact1.get_contacts()
contact1.delete_contact("yashika")
contact1.get_contacts()


