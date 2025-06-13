#inheritance.ipynb
# Parent class
class Publication:
    def publish(self):
        print("Publishing content...")
       
        # Child class
class Book(Publication):
    def details(self):
        print("This is a printed book.")

book = Book()
book.publish()
book.details()

# Parent class
class User:
    def __init__(self, username):
        self.username = username

    def display(self):
        print(f"Username: {self.username}")

        # Child class
class Admin(User):
    def __init__(self, username, privileges):
        super().__init__(username)
        self.privileges = privileges

    def display(self):
        print(f"Admin: {self.username}, Privileges: {self.privileges}")

admin_user = Admin("techadmin", ["add", "delete", "update"])
admin_user.display()
