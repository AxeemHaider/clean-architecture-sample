class User:

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, d):
        return User(d['id'], d['name'], d['age'])
