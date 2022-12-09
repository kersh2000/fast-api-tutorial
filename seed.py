import database as db

db.destroyAll()
db.addOne('palettes', 'Summer Leaves', 'Warm', "{'#A34508', '#8C51F6', '#123D1F'}")
print("Find All Palettes:\n", db.findAll('palettes'))

db.addOne('users', 'Victoria', 'Sponge', 'cake@icing.org')
print("Find All Users:\n", db.findAll("users"))
db.addMany('users', [
  ('Sara', 'Kins', 'sara33kinS@google.com'),
  ('Jane', 'Green', 'jg94@yahoo.com'),
  ('Mike', 'Black', 'blackM01@google.com'),
  ('Mary', 'Green', 'greeneyesmly@user.com')
])
print("Find All Users:\n", db.findAll('users'))
print("Find One User (without condition):\n", db.findOne('users'))
print("Find One User (with condition):\n", db.findOne('users', "first_name='Jane' AND last_name='Green'"))
print("Find Many Users (with condition):\n", db.findMany('users', "last_name='Green'"))

print("Find All Users:\n", db.findAll('users'))
db.remove(db.findOne('users'))
print("Find All Users:\n", db.findAll('users'))

print()
db.addOne('palettes', 'Summer Flower', 'Warm', "{'#AA2234', '#8C51F6', '#45DC2F'}")
print(db.findAll('palettes'))
# db.remove(db.findOne('palettes', "name='Summer Flower' AND theme='Warm'"))
# print(db.findAll('palettes'))