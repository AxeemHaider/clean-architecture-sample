class FindUser:

    def __init__(self, user_repo):
        self.user_repo = user_repo

    def by_id(self, id):
        return self.user_repo.find_by_id(id)

    def by_name(self, name):
        return self.user_repo.find_by_name(name)