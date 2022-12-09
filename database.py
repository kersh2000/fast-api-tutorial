import sqlite3
tables = {
  'users': {
    'first_name': 'text',
    'last_name': 'text',
    'email': 'text'
  },
  'palettes': {
    'name': 'text',
    'theme': 'text',
    'colours': 'text[]'
  }
}
# Create function to easily use SQL queries in other files
def query(sql, params = ()):
  # Connect to a database
  connection = sqlite3.connect('post_db.db')

  # Create a cursor
  cursor = connection.cursor()

  # Run sql query
  data = cursor.execute(sql, (params))

  # Fetch all data if exists
  if (bool(data)):
    data = data.fetchall()

  # Commit our command
  connection.commit()

  # Close our connection
  connection.close()

  # Return data
  return data


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
  sql = f"DROP TABLE IF EXISTS {tableName}"
  query(sql)
  initialise()

# Drop all tables and re-create with empty contents
def destroyAll():
  destroy('users') 
  destroy('palettes')
  initialise()

# Select one entry from a table
def findOne(tableName, condition = None):
  """
  Returns first entry of table
  :param string tableName: Name of the Table.
  :param string condition: Conditon included in the WHERE statement.
  :returns: tuple of entry, (entry)
  """
  return(findMany(tableName, condition, 1))

def findMany(tableName, condition = None, limit = None):
  limitSQL = "" if not bool(limit) else f"LIMIT {limit}"
  conditionSQL = "" if not bool(condition) else f"WHERE {condition}"
  sql = f"SELECT * FROM {tableName} {conditionSQL} {limitSQL}"
  print(sql)
  return query(sql)

# Select all entries from a table
def findAll(tableName):
  """
  Returns all entries of a table.
  :param string tableName: Name of the Table.
  :returns: Array of entries as tuples, [(entry1), (entry2), (entry3)...]
  """
  sql = f"SELECT * FROM {tableName}"
  return query(sql)

# Add single entry to table
def addOne(tableName, *args):
  sql = f"INSERT INTO {tableName} VALUES (?, ?, ?)"
  query(sql, args)

# Add multiple entries to table
def addMany(tableName, entries):
  """
  Add's multiple entries into the table.
  :param string tableName: Name of the Table.
  :param array of tuples entries: Entry values, ((col1, col2, ...), (col1, col2)...)
  """
  for entry in entries:
    sql = f"INSERT INTO {tableName} VALUES (?, ?, ?)"
    query(sql, (entry[0], entry[1], entry[2]))

# Delete a single entry from a table.
def remove(ent):
  entry = ent[0] # Get the entry from the user input
  for table in tables:
    cols = []
    for col in tables[table]:
      cols.append(col)
    condition = ""
    for j, col in enumerate(entry):
      condition += f'{cols[j]} = "{col}" AND '
    condition = condition[:-5]
    if bool(findOne(table, condition)):
      sql = f"DELETE FROM {table} WHERE {condition}"
      query(sql)
      break