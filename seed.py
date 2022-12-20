import database as db

def seed():

  db.destroyAll()

  user1 = {
    'username': 'abcdef',
    'password': 'strongPassword1!'
  }
  db.addOne('users', user1)

  sampleUsers = [{'username': 'admin', 'password': 'admin'}, {'username': 'user1', 'password': 'password1'}, {'username': 'user2', 'password': 'password2'}, {'username': 'user3', 'password': 'password3'}]
  db.addMany('users', sampleUsers)

  palette1 = {
    'name': 'palette1',
    'theme': 'Warm',
    'colours': "{'#3dc522', '#c20945', '#2d84ee'}",
    'public': 1,
    'user_id': 1
  }
  db.addOne('palettes', palette1)

  samplePalettes = [
    {
    'name': 'palette2',
    'theme': 'Warm',
    'colours': "{'#FF9014', '#46DC9C', '#23D4E0'}",
    'public': 1,
    'user_id': 1
  },
  {
    'name': 'palette3',
    'theme': 'Warm',
    'colours': "{'#024449', '#097275', '#F4E9CD', '#E2AD38', '#C96D1C'}",
    'public': 0,
    'user_id': 1
  },
  {
    'name': 'Warm pruple',
    'theme': 'Warm',
    'colours': "{'#472F5B', '#715C83', '#8F79A1', '#526863', '#314641', '#203732'}",
    'public': 0,
    'user_id': 2
  },
  {
    'name': 'Warm flower',
    'theme': 'Warm',
    'colours': "{'#4F2C8A', '#422964', '#1E310F', '#793730', '#D7841D'}",
    'public': 0,
    'user_id': 2
  },
  {
    'name': 'Fun Purple',
    'colours': "{'#C796E5', '#EDA4C2', '#A540FC', '#912CE0', '#54E2BA'}",
    'public': 1,
    'user_id': 2
  },
  {
    'name': 'Dark Purple',
    'theme': 'Dark',
    'colours': "{'#BF00FF', '#6300A9', '#000059', '#000113'}",
    'public': 0,
    'user_id': 2
  },
  {
    'name': 'Dark Clouds',
    'theme': 'Dark',
    'colours': "{'#9F9177', '#111E24', '#0F3D42', '#3A727A'}",
    'public': 1,
    'user_id': 2
  },
  {
    'name': 'Flower 6',
    'colours': "{'#0A073A', '#223F96', '#3861BE', '#FFAE7D', '#FA6B34'}",
    'public': 1,
    'user_id': 3
  }
  ]
  db.addMany('palettes', samplePalettes)

  db.updatePalettesTheme('Warm', 'Warm2', 1)



  # db.destroyAll()
  # print(db.findAll('users'))

  # user1 = {
  #   'username': 'abcdef',
  #   'password': 'strongPassword1!'
  # }
  # db.addOne('users', user1)
  # print(db.findAll('users'))
  # print(db.findUserByUsername('abcdef'), "\n")

  # sampleUsers = [{'username': 'admin', 'password': 'admin'}, {'username': 'user1', 'password': 'password1'}, {'username': 'user2', 'password': 'password2'}, {'username': 'user3', 'password': 'password3'}]
  # db.addMany('users', sampleUsers)
  # print(db.findAll('users'))

  # palette1 = {
  #   'name': 'palette1',
  #   'theme': 'Warm',
  #   'colours': "{'#3dc522', '#c20945', '#2d84ee'}",
  #   'public': 1,
  #   'user_id': 1
  # }
  # db.addOne('palettes', palette1)
  # print(db.findAll('palettes'))

  # samplePalettes = [
  #   {
  #   'name': 'palette2',
  #   'theme': 'Warm',
  #   'colours': "{'#FF9014', '#46DC9C', '#23D4E0'}",
  #   'public': 1,
  #   'user_id': 1
  # },
  # {
  #   'name': 'palette3',
  #   'theme': 'Warm',
  #   'colours': "{'#024449', '#097275', '#F4E9CD', '#E2AD38', '#C96D1C'}",
  #   'public': 0,
  #   'user_id': 1
  # },
  # {
  #   'name': 'Warm pruple',
  #   'theme': 'Warm',
  #   'colours': "{'#472F5B', '#715C83', '#8F79A1', '#526863', '#314641', '#203732'}",
  #   'public': 0,
  #   'user_id': 2
  # },
  # {
  #   'name': 'Warm flower',
  #   'theme': 'Warm',
  #   'colours': "{'#4F2C8A', '#422964', '#1E310F', '#793730', '#D7841D'}",
  #   'public': 0,
  #   'user_id': 2
  # },
  # {
  #   'name': 'Fun Purple',
  #   'colours': "{'#C796E5', '#EDA4C2', '#A540FC', '#912CE0', '#54E2BA'}",
  #   'public': 1,
  #   'user_id': 2
  # },
  # {
  #   'name': 'Dark Purple',
  #   'theme': 'Dark',
  #   'colours': "{'#BF00FF', '#6300A9', '#000059', '#000113'}",
  #   'public': 0,
  #   'user_id': 2
  # },
  # {
  #   'name': 'Dark Clouds',
  #   'theme': 'Dark',
  #   'colours': "{'#9F9177', '#111E24', '#0F3D42', '#3A727A'}",
  #   'public': 1,
  #   'user_id': 2
  # },
  # {
  #   'name': 'Flower 6',
  #   'colours': "{'#0A073A', '#223F96', '#3861BE', '#FFAE7D', '#FA6B34'}",
  #   'public': 1,
  #   'user_id': 3
  # }
  # ]
  # db.addMany('palettes', samplePalettes)
  # print(db.findAll('palettes'))

  # print(db.findPalettesByUserId("2"))

  # print(db.findPalettesByTheme('Warm', "1"))

  # print(db.findPublicPalettes())

  # db.updatePalettesTheme('Warm', 'Warm2', 1)

  # print(db.findPaletteById("1"))

  # print(db.findDistinctPalettes("2"))

  # print(db.findLatestPalette())





# db.destroyAll()
# db.addOne('palettes', 'Summer Leaves', 'Warm', "{'#A34508', '#8C51F6', '#123D1F'}")
# print("Find All Palettes:\n", db.findAll('palettes'))

# db.addOne('users', 'Victoria', 'Sponge', 'cake@icing.org')
# print("Find All Users:\n", db.findAll("users"))
# db.addMany('users', [
#   ('Sara', 'Kins', 'sara33kinS@google.com'),
#   ('Jane', 'Green', 'jg94@yahoo.com'),
#   ('Mike', 'Black', 'blackM01@google.com'),
#   ('Mary', 'Green', 'greeneyesmly@user.com')
# ])
# print("Find All Users:\n", db.findAll('users'))
# print("Find One User (without condition):\n", db.findOne('users'))
# print("Find One User (with condition):\n", db.findOne('users', "first_name='Jane' AND last_name='Green'"))
# print("Find Many Users (with condition):\n", db.findMany('users', "last_name='Green'"))

# print("Find All Users:\n", db.findAll('users'))
# db.remove(db.findOne('users'))
# print("Find All Users:\n", db.findAll('users'))

# print()
# db.addOne('palettes', 'Summer Flower', 'Warm', "{'#AA2234', '#8C51F6', '#45DC2F'}")
# print(db.findAll('palettes'))
# db.remove(db.findOne('palettes', "name='Summer Flower' AND theme='Warm'"))
# print(db.findAll('palettes'))