import database as db

def seed():

  db.destroyAll()

  # user1 = {
  #   'username': 'abcdef',
  #   'password': 'strongPassword1!'
  # }
  # db.addOne('users', user1)

  sampleUsers = [{'username': 'admin', 'password': 'admin'}, {'username': 'user1', 'password': 'password1'}, {'username': 'user2', 'password': 'password2'}, {'username': 'user3', 'password': 'password3'}]
  # db.addMany('users', sampleUsers)

  # palette1 = {
  #   'name': 'palette1',
  #   'theme': 'Warm',
  #   'colours': "{'#3dc522', '#c20945', '#2d84ee'}",
  #   'public': 1,
  #   'user_id': 1
  # }
  # db.addOne('palettes', palette1)

  # db.addMany('palettes', samplePalettes)

  # db.updatePalettesTheme('Warm', 'Warm2', 1)


  testUsers = [
    { # user_id = 1
      'username': 'admin',
      'password': 'admin'
    },
    { # user_id = 2
      'username': 'asma',
      'password': 'password'
    },
    { # user_id = 3
      'username': 'bobby',
      'password': 'password'
    },
    { # user_id = 4
      'username': 'bradley',
      'password': 'password'
    },
    { # user_id = 5
      'username': 'ihsan',
      'password': 'password'
    },
    { # user_id = 6
      'username': 'sasha',
      'password': 'password'
    }
  ]

  testPalettes = [
    # Admin palettes (1)
    {
      'name': 'Test1',
      'theme': 'TEST',
      'colours': "{'#FF9014', '#46DC9C', '#23D4E0'}",
      'public': 1,
      'user_id': 1
    },
    {
      'name': 'Test2',
      'theme': 'TEST',
      'colours': "{'#024449', '#097275', '#F4E9CD', '#E2AD38', '#C96D1C'}",
      'public': 1,
      'user_id': 1
    },
    {
      'name': 'Test1',
      'theme': 'TEST',
      'colours': "{'#FF9014', '#46DC9C', '#23D4E0'}",
      'public': 0,
      'user_id': 1
    },
    {
      'name': 'Test1',
      'theme': 'TEST',
      'colours': "{'#FF9014', '#46DC9C', '#23D4E0'}",
      'public': 0,
      'user_id': 1
    },

    # Asma palettes (2)
    {
      'name': 'Natural',
      'theme': 'Light',
      'colours': "{'#2A2B2A', '#5E4955', '#996888', '#C99DA3', '#C6DDF0'}",
      'public': 1,
      'user_id': 2
    },
    {
      'name': 'Plant Life',
      'theme': 'Light',
      'colours': "{'#2C302E', '#474A48', '#909590', '#9AE19D', '#537A5A'}",
      'public': 1,
      'user_id': 2
    },
    {
      'name': 'Planet',
      'theme': 'Light',
      'colours': "{'#ECE2D0', '#CEBEBE', '#D5B9B2', '#A26769', '#6D2E46'}",
      'public': 1,
      'user_id': 2
    },
    {
      'name': 'Waves',
      'theme': 'Sharp',
      'colours': "{'#7B3E19', '#B28B84', '#F5E5FC', '#8AE1FC', '#48B8D0'}",
      'public': 1,
      'user_id': 2
    },
    {
      'name': 'Natural',
      'theme': 'Sharp',
      'colours': "{'#7C9EB2', '#52528C', '#372554', '#231123'}",
      'public': 1,
      'user_id': 2
    },

    # Bobby palettes (3)
    {
      'name': 'Dark Clouds',
      'theme': 'Dark',
      'colours': "{'#9F9177', '#111E24', '#0F3D42', '#3A727A'}",
      'public': 0,
      'user_id': 3
    },
    {
      'name': 'Beach',
      'theme': 'Sunny',
      'colours': "{'#FC9F5B', '#FBD1A2', '#ECE4B7', '#7DCFB6', '#33CA7F'}",
      'public': 0,
      'user_id': 3
    },
    {
      'name': 'Bright',
      'theme': 'Sunny',
      'colours': "{'#CBFF8C', '#E3E36A', '#C16200', '#881600', '#4E0110'}",
      'public': 1,
      'user_id': 3
    },
    {
      'name': 'Zoom',
      'theme': 'Dark',
      'colours': "{'#170312', '#33032F', '#531253', '#A0ACAD', '#97D8B2'}",
      'public': 1,
      'user_id': 3
    },
    {
      'name': 'Simple',
      'colours': "{'#FFFFFF', '#000000'}",
      'public': 1,
      'user_id': 3
    },

    # Bradley palettes (4)
    {
      'name': 'Warm green/red',
      'theme': 'Warm',
      'colours': "{'#4F2C8A', '#422964', '#1E310F', '#793730', '#D7841D'}",
      'public': 1,
      'user_id': 4
    },
    {
      'name': 'Warm again',
      'theme': 'Warm',
      'colours': "{'#0A073A', '#223F96', '#3861BE', '#FFAE7D', '#FA6B34'}",
      'public': 0,
      'user_id': 4
    },
    {
      'name': 'Light Peach',
      'theme': 'Warm',
      'colours': "{'#FFB6C1', '#FFA07A', '#FF7F50', '#FF4500', '#8B2500'}",
      'public': 1,
      'user_id': 4
    },
    {
      'name': 'Dark Peach',
      'theme': 'Warm',
      'colours': "{'#FDEBD0', '#F5B183', '#F4A460', '#CD853F', '#8B4513'}",
      'public': 1,
      'user_id': 4
    },
    {
      'name': 'Modern 1',
      'theme': 'Modern',
      'colours': "{'#EB5E55', '#3A3335', '#D81E5B', '#FDF0D5', '#C6D8D3'}",
      'public': 1,
      'user_id': 4
    },
    {
      'name': 'Modern 2',
      'theme': 'Modern',
      'colours': "{'#2B2D42', '#8D99AE', '#FFFFFF'}",
      'public': 1,
      'user_id': 4
    },

    # Ihsan palettes (5)
    {
      'name': 'Purple 1',
      'theme': 'iLuvPrpl',
      'colours': "{'#472F5B', '#715C83', '#8F79A1', '#526863', '#314641', '#203732'}",
      'public': 0,
      'user_id': 5
    },
    {
      'name': 'Purple 2',
      'theme': 'iLuvPrpl',
      'colours': "{'#BF00FF', '#6300A9', '#000059', '#000113'}",
      'public': 0,
      'user_id': 5
    },
    {
      'name': 'Mint Purple',
      'theme': 'iLuvPrpl',
      'colours': "{'#97EAD2', '#8CC7A1', '#816E94', '#74226C', '#4B2142', '#000000'}",
      'public': 1,
      'user_id': 5
    },
    {
      'name': 'random 1',
      'colours': "{'#F0A202', '#F18805', '#D95D39', '#7B9E89', '#526863', '#0E1428'}",
      'public': 1,
      'user_id': 5
    },
    {
      'name': 'random 2',
      'colours': "{'#F49097', '#DFB2F4'}",
      'public': 1,
      'user_id': 5
    },

    # Sasha palettes (6)
    {
      'name': 'Fun Purple',
      'theme': 'Fun',
      'colours': "{'#C796E5', '#EDA4C2', '#A540FC', '#912CE0', '#54E2BA'}",
      'public': 1,
      'user_id': 6
    },
    {
      'name': 'Seaside',
      'theme': 'Fun',
      'colours': "{'#08415C', '#388697', '#B5FFE1', '#EBBAB9', '#CC2936'}",
      'public': 1,
      'user_id': 6
    },
    {
      'name': 'Zebra',
      'colours': "{'#000000', '#FFFFFC', '#BEB7A4', '#FF7F11', '#FF3F00'}",
      'public': 0,
      'user_id': 6
    },
    {
      'name': 'Colourful',
      'theme': 'Vibrant',
      'colours': "{'#0E7C7B', '#17BEBB', '#4B1D3F', '#D62246'}",
      'public': 0,
      'user_id': 6
    },
    {
      'name': 'Smooth',
      'colours': "{'#C1A5A9', '#F08CAE', '#9A4C95', '#4D2D52', '#1D1A31'}",
      'public': 0,
      'user_id': 6
    },
    {
      'name': 'Crayon',
      'colours': "{'#FFA69E', '#FAF3DD', '#B8F2E6', '#AED9E0', '#5E6472'}",
      'public': 1,
      'user_id': 6
    },

  ]


  db.addMany('users', testUsers)
  db.addMany('palettes', testPalettes)

  db.addOne('users', {
    'username': 'bradz; DROP TABLE users; --',
    'password': 'password12'
  })

  print(db.findAll('users'))

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