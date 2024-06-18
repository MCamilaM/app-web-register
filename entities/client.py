class Client:
    def __init__(self, dni, typeDocument, name, lastname, address, phoneNumber, email):
        self.dni = dni
        self.typeDocument = typeDocument
        self.name = name
        self.lastname = lastname
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email

    def __repr__(self):
        return (f"Client(dni={self.dni}, typeDocument={self.typeDocument}, name={self.name}, "
                f"lastname={self.lastname}, address={self.address}, phoneNumber={self.phoneNumber}, "
                f"email={self.email})")