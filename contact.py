class Contact:
    def __init__(self, store_name, phone_number, email, address ):
        self.store_name=store_name
        self.phone_number=phone_number
        self.email=email
        self.address=address
        
    def __str__(self):
        return f"Name:{self.store_name}\nPhone: {self.phone_number}\nEmail:{self.email}\nAddress:{self.address}"
    
    