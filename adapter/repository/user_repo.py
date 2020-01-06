from adapter.repository.models.usermodel import UserModel
from domain.user import User


class UserRepo:

    def __init__(self):
        self.users = self.create_users()

    def create_users(self):
        user_list = []
        for n in range(3):
            u = UserModel(n, "name" + str(n), n)
            user_list.append(u)
        return user_list

    def find_by_id(self, id):
        for user in self.users:
            if user.id == id:
                return User.from_dict(user.to_dict())

    def find_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return User.from_dict(user.to_dict())
