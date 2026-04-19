class User:
    def __init__(self, user: str, age: int):
        self.user = user
        self.age = age

user = User("Erkin", 30)
print(user.age)
