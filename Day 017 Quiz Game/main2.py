class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
        print(f"You are now following {user.username}")

    def print_follow(self):
        print(f"User: {self.username}\nFollowers: {self.followers}")
        print(f"Following: {self.following}")


user_1 = User(username="Klint", id="038")
user_2 = User("42", "Christian")
user_2.follow(user_1)
user_1.print_follow()
user_2.print_follow()
