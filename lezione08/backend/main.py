import uvicorn
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import bcrypt

from db import fetchall, fetchone, execute


class Login(BaseModel):
  username: str
  password: str


class Message(BaseModel):
  message: str


app = FastAPI()


def is_logged_in(user: Login):

    query = "SELECT password FROM User WHERE username = %s"
    cols = fetchone(query, (user.username,))
    if not cols:
        return False

    hashed = cols[0]
    return bcrypt.checkpw(user.password.encode(),hashed.encode())


@app.post("/api/login")
def post_login(user: Login):

    if is_logged_in(user):
        resp = JSONResponse(content={"success": True,"message": "Benvenuto"}, status_code=200)
        resp.set_cookie("username", user.username)
        return resp

    raise HTTPException(401, "Wrong Credentials")


@app.get("/api/chat")
def get_chat():
  """
  Interroga il db e ritorna i dati correttamente estratti
  """
  cols = fetchall("SELECT username, message FROM Chat ORDER BY id")
  return cols

@app.post("/api/chat")
def post_chat(message: Message, request: Request):
    """
    Inserire il messaggio nel db, ogni messaggio è associato ad un utente
    Come sappiamo chi ha inviato il messaggio? COOKIES
    Tiro fuori il messaggio dal base model,
    il nome utente dai cookies,
    ritorno al frontend quello che ho inserito
    """

    user = request.cookies.get("username")
    if not user:
        raise HTTPException(401, "Wrong Credentials")

    query = ("INSERT INTO Chat (message, username) VALUES (%s, %s)")

    try: execute(query,(message.message, user))

    except Exception as e:
        print(e)
        raise HTTPException(400,"Impossibile inserire messaggio")
    
    data = {
    "username":user,
    "message": message.message
  }

    return {
        "success": True,
        "message": "Messaggio inserito",
        "data":data
    }


@app.post("/api/signup")   
def post_signup(user: Login, response: Response):
    """
    Inserire un utente nel database
    se esiste già valutare una opzione
    e notificare che non può essere creato
    con successo l'account
    """

    query = ("INSERT INTO User (username, password)VALUES (%s, %s)")

    try:
        hashed = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
        execute(query,(user.username, hashed.decode()))

    except Exception as e:
        print(e)
        raise HTTPException(401,"Impossibile creare utente")

    response.set_cookie("username",user.username)

    return {
        "success": True,
        "message": "Registrazione completata"
    }


uvicorn.run(app)