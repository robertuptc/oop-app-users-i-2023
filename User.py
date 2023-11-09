class User:
    def __init__(self, name, last_name, age, email, password ):  
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password

    def __str__(self):
        return f"Welcome {self.name}! Your account has been created. Check your {self.email} for a confirmation code!"

new_user = User('Robert', 'Puentes', 25, "myemail.@gmail.com", "123asd456")
print(new_user.name)