from adapter.repository.user_repo import UserRepo
from usecase.find_user import FindUser


class User:

    @classmethod
    def find_user(cls):
        user_repo = UserRepo()
        return FindUser(user_repo)