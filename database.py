import sqlite3
tables = {
  'users': {
    'id': 'INTEGER PRIMARY KEY',
    'username': 'TEXT NOT NULL UNIQUE',
    'password': 'TEXT NOT NULL'
  },
  'palettes': {
    'id': 'INTEGER PRIMARY KEY',
    'name': 'TEXT NOT NULL',
    'theme': 'TEXT DEFAULT NULL',
    'colours': 'TEXT[] NOT NULL',
    'public': 'INTEGER DEFAULT 0',
    'user_id': 'INTEGER DEFAULT NULL, FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE SET DEFAULT'
  }
}
# Create function to easily use SQL queries in other files
def query(sql, params = ()):
  # Connect to a database
  connection = sqlite3.connect('post_db.db')
  try:
    # For data formatting after query execution
    connection.row_factory = sqlite3.Row

    # Create a cursor
    cursor = connection.cursor()

    # Run sql query
    if type(params) == str:
      params = tuple((params,))
    print(f"\n------------------------------\nSQL QUERY:\nsql = {sql}\nparams = {params}\n------------------------------\n")
    data = cursor.execute(sql, params)

    # Convert data into JSON (array[dict1, dict2, dict3...])
    values = data.fetchall()
    json = []
    for item in values:
      json.append({k: item[k] for k in item.keys()})

    # # Fetch all data if exists
    # if (bool(data)):
    #   data = data.fetchall()

    # Commit our command
    connection.commit()

    # Return json-formatted data
    return json[0] if len(json) == 1 else json
  except Exception as e:
    print(f"Failed to execute. Query: {sql}\n Parameters: {params}\n Error: {e}")
    raise Exception(e)
  finally:
    # Close our connection
    connection.close()


# Flexible functions -----------------------------------------------------------------------------

# Create tables if don't exist
def initialise():
  for tableName in tables.keys():
    sql = f"CREATE TABLE IF NOT EXISTS {tableName}("
    for colName in tables[tableName].keys():
      sql += f"{colName} {tables[tableName][colName]}, "
    sql = sql[:-2] + ')'
    query(sql)

# Drop table and re-create with empty contents
def destroy(tableName):
  if tableName in tables.keys():
    sql = f"DROP TABLE IF EXISTS {tableName}"
    query(sql)

# Drop all tables and re-create with empty contents
def destroyAll():
  destroy('users') 
  destroy('palettes')
  initialise()

# Find a user by their id
def findUserById(id):
  return query("""
  SELECT * FROM users
  WHERE id = (?)
  LIMIT 1
  """, str(id))

# Find a user by their username (for signing in)
def findUserByUsername(username):
  return query("""
  SELECT * FROM users
  WHERE username = (?)
  LIMIT 1""", username)

# Find a palette by their id
def findPaletteById(id):
  return query("""
  SELECT * FROM palettes
  WHERE id = (?)
  """, str(id))

# Find a palettes by the user's id (to retrieve a user's palettes)
def findPalettesByUserId(user_id):
  return query("""
  SELECT * FROM palettes
  WHERE user_id = (?)
  """, str(user_id))

# Find palettes which share the given theme
def findPalettesByTheme(theme, user_id):
  return query("""
  SELECT * FROM palettes
  WHERE theme = (?) AND user_id = (?)
  """, (theme, str(user_id)))

# Find all entries from a table for testing
def findAll(tableName):
  """
  Returns all entries of a table.
  :param string tableName: Name of the Table.
  :returns: Array of entries as tuples, [(entry1), (entry2), (entry3)...]
  """
  if tableName in tables.keys():
    sql = f"SELECT * FROM {tableName}"
    return query(sql)

# Remove a user by their id for delete requests (removing their account)
def removeUserById(id):
  query("""
  DELETE FROM users WHERE id = (?)
  """, str(id))

# Remove a palette by their id for delete requests (removing a palette fromt their account)
def removePaletteById(id):
  query("""
  DELETE FROM palettes
  WHERE id = (?)
  """, str(id))

# Remove all palettes from a user for delete requests (removing a user and their palettes)
def removePalettesByUserId(user_id):
  query("""
  DELETE FROM palettes WHERE user_id = (?)
  """, str(user_id))

# Update a palette's name in PUT requests
def updatePalettesName(name, id):
  query("""
  UPDATE palettes
  SET name = (?)
  WHERE id = (?)
  """, (name, id))

# Update a palette's theme in PUT requests
def updatePalettesTheme(oldTheme, newTheme, id):
  query("""
  UPDATE palettes
  SET theme = (?)
  WHERE theme = (?) AND id = (?)
  """, (newTheme, oldTheme, str(id)))

# Update a palette's colours in PUT requests
def updatePalettesColours(id, colours):
  query("""
  UPDATE palettes
  SET colours = (?)
  WHERE id = (?)
  """, (colours, id))

# Remove a palette's theme (set the value to null) to remove a palette from a theme
def removePaletteTheme(theme, user_id):
  query("""
  UPDATE palettes
  SET theme = null
  WHERE theme = (?) AND user_id = (?)
  """, (theme, str(user_id)))

# Find all public palettes with their username (creator) using an INNER JOIN query
def findPublicPalettes():
  return query("""
  SELECT palettes.name, palettes.theme, palettes.colours, users.username 
  FROM palettes
  INNER JOIN users ON palettes.user_id = users.id
  WHERE palettes.public = 1
  """)

# Find all distinct themes from a user for displaying palettes by theme
def findDistinctPalettes(user_id):
  return query("""
  SELECT DISTINCT theme FROM palettes
  WHERE user_id = (?)
  """, str(user_id))

# Find the latest palette added to the table, in order get the pallete just created by the user
def findLatestPalette():
  return query("""
  SELECT * FROM palettes WHERE
  id = (SELECT MAX(id) FROM palettes)
  """)

# Add one entry to any table (with alot of SQL injection avoidance)
def addOne(tableName, props):
  if tableName not in tables.keys():
    return False
  columns = props.keys()  
  placeholder_columns = ", ".join(props.keys())
  placeholder_values = ", ".join([":{0}".format(col) for col in columns])
  sql = "INSERT INTO {table_name} ({placeholder_columns}) VALUES ({placeholder_values})".format(
    table_name=tableName,
    placeholder_columns=placeholder_columns,
    placeholder_values=placeholder_values
  )
  query(sql, props)

# Add many entries to any table, using the function above to avoid SQLi
def addMany(tableName, arr):
  if tableName not in tables.keys():
    return False
  for entry in arr:
    addOne(tableName, entry)

