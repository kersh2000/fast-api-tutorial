from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
  return {"Data": "Home"}

@app.get("/about")
def about():
  return {"Data": "About"}