import factory

find_user = factory.User.find_user()

user = find_user.by_id(2)

print(user.id, user.name, user.age)

user = find_user.by_name('name1')

print(user.id, user.name, user.age)