from contact import Contact
from contact_book import ContactBook

def main():
    contact_book=ContactBook()
    
    while True:
        print("\n====Contact Book Menu==== ")
        print("1.Add new contact")
        print("2.view all contacts")
        print("3.search contact")
        print("4.update contact")
        print("5.delete contact")
        print("6.exit")
        
        choice=input("Enter your choice(1-6):")
        
        if choice=='1':
            print("\nEnter contact details:")
            store_name=input("store name:")
            phone_number=input("phone number:")
            email=input("email:")
            address=input("address:")
            new_contact=Contact(store_name,phone_number,email,address)
            contact_book.add_contact(new_contact)
            print("contact added successfully.")
            
        elif choice == '2':
            print("\n---list of contacts---")
            contact_book.view_contacts()
            
        elif choice=='3':
            search_query=input("\n enter name or phone number to search: ")
            found_contacts=contact_book.search_contacts(search_query)
            if found_contacts:
                print("\n---search results---")
                for contact in found_contacts:
                    print(contact)
                    print("--------------------")
            else:
                print("no contacts found.")
            
        elif choice=='4':
            index=int(input("\nEnter the index of contact to update:")) -1
            if 0<=index<len(contact_book.contacts):
                 print("\n enter updated contact details:")
                 store_name=input("store name:")
                 phone_number=input("phone number:")
                 email=input("email:")
                 address=input("address:")
                 updated_contact=Contact(store_name,phone_number,email,address)
                 contact_book.update_contact(index, updated_contact)
                 print("contact updated successfully")
            else:
                print("Invalid index.")   
        elif choice == '5':
            index= int(input("\nenter the index of contact to delete")) -1
            if 0<=index < len(contact_book.contacts):
                contact_book.delete_contact(index)
                print("contact deleted successfully!")
            else:
                print("invalid index.")
        elif choice == '6':
            print("exiting the contact book.")
            break
        else:
            print("Invalid choice.Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()                                          
            