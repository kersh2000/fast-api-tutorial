from fastapi import FastAPI, HTTPException, status, Form
from fastapi.middleware.cors import CORSMiddleware
import database as db
import seed as s
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
  username: str
  password: str

  def asdict(self):
    return {
      'username': self.username,
      'password': self.password
    }

class Palette(BaseModel):
  name: str
  theme: Optional[str]
  colours: list
  public: Optional[int]
  user_id: Optional[int]

  def asdict(self):
    data = {}
    org = {
      'name': self.name,
      'theme': self.theme,
      'colours': self.colours,
      'public': self.public,
      'user_id': self.user_id
    }
    for key in org:
      if org[key] != None:
        data[key] = org[key]
    return data

class ThemeChange(BaseModel):
  id: int
  oldTheme: str
  newTheme: str

class ColourChange(BaseModel):
  id: int
  colours: list

class NameChange(BaseModel):
  id: int
  newName: str

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get user by username and password
@app.post("/login", )
def find_user(username: str = Form(), password: str = Form()):
  record = dict(db.findUserByUsername(username))
  if not bool(record):
    raise HTTPException(status_code=404, detail="User not found.")
  elif record["password"] != password:
    raise HTTPException(status_code=401, detail="Incorrect password.")
  return record["id"]

# Create user through body
@app.post("/register")
def create_user(username: str = Form(), password: str = Form()):
  try:
    if not username.isalnum() or len(password) < 6:
      raise ValueError("Invalid username or password")
    db.addOne('users', {
      "username": username,
      "password": password
    })
    record = dict(db.findUserByUsername(username))
    return record["id"]
  except ValueError:
    raise HTTPException(status_code=400, detail="Invalid username or password.")
  except Exception:
    raise HTTPException(status_code=400, detail="User already exists.")

@app.delete("/users/{id}")
def delete_user(id: int):
  record = db.findUserById(id)
  if not bool(record):
    raise HTTPException(status_code=404, detail="User not found.")
  db.removeUserById(id)
  db.removePalettesByUserId(id)

# Get palettes by user_id
@app.get("/palettes/{user_id}")
def find_palettes(user_id: int):
  record = db.findUserById(user_id)
  if not bool(record):
    raise HTTPException(status_code=404, detail="User not found.")
  paletteRecord = db.findPalettesByUserId(user_id)
  return paletteRecord if not isinstance(paletteRecord, dict) else [paletteRecord]

# Get palettes by user_id and theme
@app.get("/palettes/{user_id}/{theme}")
def find_themed_palettes(user_id: int, theme: str):
  record = db.findUserById(user_id)
  if not bool(record):
    raise HTTPException(status_code=404, detail="User not found.")
  paletteRecord = db.findPalettesByTheme(theme, user_id)
  if not bool(paletteRecord):
    raise HTTPException(status_code=404, detail="Theme has no palettes.")
  return paletteRecord if not isinstance(paletteRecord, dict) else [paletteRecord]

# Get pallete by its ID number
@app.get("/palette/{id}")
def find_palette_by_id(id: int):
  record = db.findPaletteById(id)
  if not bool(record):
    raise HTTPException(status_code=404, detail="Palette not found.")
  return record

# Remove palette by id
@app.delete("/palettes/{id}")
def delete_palette(id: int):
  record = db.findPaletteById(id)
  if not bool(record):
    raise HTTPException(status_code=404, detail="Palette not found.")
  db.removePaletteById(id)

# Update palette's name
@app.put("/palettes/name")
def update_palette_name(name: NameChange):
  record = db.findPaletteById(name.id)
  if not bool(record):
    raise HTTPException(status_code=404, detail="Palette not found.")
  db.updatePalettesName(name.newName, name.id)

# Update palette's theme
@app.put("/palettes/theme")
def update_palette_theme(theme: ThemeChange):
  record = db.findPaletteById(theme.id)
  if not bool(record):
    raise HTTPException(status_code=404, detail="Palette not found.")
  themeRecord = db.findPalettesByTheme(theme.oldTheme, theme.id)
  if not bool(themeRecord):
    raise HTTPException(status_code=404, detail="Error")

  db.updatePalettesTheme(theme.oldTheme, theme.newTheme, theme.id)

@app.put("/palettes/colour")
def update_palette_colour(colour: ColourChange):
  record = db.findPaletteById(colour.id)
  if not bool(record):
    raise HTTPException(status_code=404, detail="Palette not found.")
  colours = '{'
  for eachColour in colour.colours:
    colours += "'" + eachColour + "'" + ", "
  colours = colours[:-2]
  colours += '}'
  db.updatePalettesColours(colour.id, colours)

@app.delete("/palettes/{user_id}/{theme}")
def remove_theme(user_id: int, theme: str):
  record = db.findUserById(user_id)
  if not bool(record):
    raise HTTPException(status_code=404, detail="User not found.")
  db.removePaletteTheme(theme, user_id)
  return db.findPalettesByUserId(user_id)

@app.get("/distinct/{user_id}")
def get_distinct_themes(user_id: int):
  record = db.findUserById(user_id)
  if not bool(record):
    raise HTTPException(status_code=404, detail="User not found.")
  paletteRecord = db.findDistinctPalettes(user_id)
  return paletteRecord if not isinstance(paletteRecord, dict) else [paletteRecord]

# Get all public palettes
@app.get("/public")
def get_public_palettes():
  paletteRecord = db.findPublicPalettes()
  return paletteRecord if not isinstance(paletteRecord, dict) else [paletteRecord]

# Create palette through body
@app.post("/palettes")
def create_palette(palette: Palette):
  colours = '{'
  for colour in palette.colours:
    colours += "'" + colour + "'" + ", "
  colours = colours[:-2]
  colours += '}'
  data = palette.asdict()
  data["colours"] = colours
  try:
    db.addOne('palettes', data)
    record =  db.findLatestPalette()
    return record
  except:
    raise HTTPException(status_code=400, detail="Palette already exists.")


# # Testing
# @app.get("/")
# def home():
#   return {"Data": "Home"}
# @app.get("/about")
# def about():
#   return {"Data": "About"}

# Get all entries from table
@app.get("/{table}")
def get_entries(table: str):
  record = db.findAll(table)
  return record if not isinstance(record, dict) else [record]

@app.post("/seed")
def seed():
  s.seed()
