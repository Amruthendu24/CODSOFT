from contact import Contact

class ContactBook:
    def __init__(self):
        self.contacts=[]
        
    def add_contact(self, contact):
        self.contacts.append(contact)
      
    def view_contacts(self):
        if not self.contacts:
            print("contact list is empty.")
        else:
            for index, contact in enumerate(self.contacts,start=1):
                print(f"Contact{index}:")
                print(contact)
                print("-----------------")  
    def search_contacts(self, search_query):
        found_contacts=[]
        for contact in self.contacts:
            if(search_query.lower()) in contact.store_name.lower() or (search_query in contact.phone_number):
                found_contacts.append(contact)
        return found_contacts
    
    def update_contact(self, index,updated_contact):
        self.contacts[index]=updated_contact
        
    def delete_contact(self,index):
        del self.contacts[index]  
                  
                                