from fastapi import FastAPI
import database as db
from pydantic import BaseModel

class User(BaseModel):
  first_name: str
  last_name: str
  email: str

class Palette(BaseModel):
  name: str
  theme: str
  colours: list

app = FastAPI()

# Testing
@app.get("/")
def home():
  return {"Data": "Home"}
@app.get("/about")
def about():
  return {"Data": "About"}

# Get all entriesw from table
@app.get("/{table}")
def get_entries(table: str):
  return db.findAll(table)

# Get user by firstname and lastname as url params
@app.get("/users/{first_name}/{last_name}")
def find_user(first_name: str, last_name: str):
  condition = f"first_name='{first_name}' AND last_name='{last_name}'"
  return db.findOne('users', condition)

# Create user through body
@app.post("/users")
def create_user(user: User):
  db.addOne('users', user.first_name, user.last_name, user.email)

# Create palette through body
@app.post("/palettes")
def create_palette(palette: Palette):
  colours = '{'
  for colour in palette.colours:
    colours += colour + ", "
  colours = colours[:-2]
  colours += '}'
  db.addOne('palettes', palette.name, palette.theme, colours)

@app.delete("/users/{first_name}/{last_name}")
def delete_user(first_name: str, last_name: str):
  condition = f"first_name='{first_name}' AND last_name='{last_name}'"
  db.remove(db.findOne('users', condition))

@app.delete("/palettes/{name}/{theme}")
def delete_palette(name: str, theme: str):
  condition = f"name='{name}' AND theme='{theme}'"
  db.remove(db.findOne('palettes', condition))