Simple RESTful API using FastAPI.


Versions:
Python - 3.6.8
PIP - 18.1
FastAPI - 0.83.0
Uvicorn - 0.16.0
Python-multipart - 0.0.5 six-1.16.0


Instructions:
To start server: uvicorn server:app --reload
Server site (localhost): http://127.0.0.1:8000
Server site for instructions on endpoints: http://127.0.0.1:8000/docs


DB Design:
- users: id (int) | username (unique str) | password (str)
- palettes: id (int) | name (str) | theme (str) | colours (str[]) | public (0/1) | user_id (int)


API Design:
users:
- (POST) /login => Get user's information when logging in to check the password and username passed in do match, and if so, return with a token or the user's id?
- (POST) /register => Create a user with the information passed through the body, and return with the user's id / token? (body = { "username": "_string_", "email": "_string_", "password": "_string_" })
- **(DELETE) /users/{id} => Delete a user by passing their id

palettes:
- (GET) /palettes/{user_id} => Get user's palettes by passing through their user_id, and return an array of palettes.
- (POST) /palettes/{user_id} => Create a pallete with the user_id and the information passed through the body. (body = { "name": "_string_", "theme": "_optional string_", "colours": _["string"]_, "public": _optional int_, "user_id": _int_ })
- (GET) /palettes/{user_id}/{theme} => Get all palettes which correspond to the user_id and theme passed in.
- (DELETE) /palettes/{id} => Delete the pallete which matches with the ID of the pallete passed in, return a conformation message or status code if succesful or unsuccessful.
- (DELETE) /palettes/{user_id}/{theme} => Remove the theme of the palette with the match ID passed in.
- *(PUT) /palettes/{theme} => Change the theme of the palette to the values passed in, return new array of updated palettes.
- *(PUT) /palettes/name => Change the name of the palette to the values passed in.
- **(PUT) /palettes/colour => Change the colours of the palette through the body. (body = {"id": _int_, "new_colours": _["string"]_})
- **(GET) /palletes/public => Get all palettes and their user's username (with inner join) in order to get all palettes from the DB which have a public value of 1.