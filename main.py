from fastapi import FastAPI
import ollama
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# JWT dependencies start
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI,Depends,HTTPException, Form
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecret"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")

fake_user = {"username":"test","password":"testPass"}

def create_token(username:str):
  expiration = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  return jwt.encode({"sub":username,"exp":expiration},SECRET_KEY,algorithm=ALGORITHM)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# JWT dependencies end


app=FastAPI()

CHAT_HISTORY=[]

@app.get("/showModels")
def show():
  obj=ollama.list()
  models=[]
  for item in obj['models']:
    models.append(item['name'])
  return{'available_models':models}



@app.get("/promptllama/")
# async def ollama_prompt(token:str=Depends(oauth2_scheme), query:str=""):
async def ollama_prompt(token:str, query:str):
  try:
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    response = ollama.generate('tinyllama', query)
    print(response['response'])
    chat_pair={"query":query,"response":response['response']}
    CHAT_HISTORY.append(chat_pair)
    return {"response":response["response"]}
  except:
    raise HTTPException(status_code=401, detail="Invalid token or You have not started ollama server")




@app.get("/history")
async def show_history(token:str=Depends(oauth2_scheme)):
  try:
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    return CHAT_HISTORY
  except:
    raise HTTPException(status_code=401, detail="Invalid token")




@app.post("/token")
async def login(username:str=Form(...),password:str=Form(...)):
  if username == fake_user["username"] and password==fake_user["password"]:
    return {"access_token":create_token(username),"token_type":"bearer"}
  raise HTTPException(status_code=400, detail="Invalid credentials")

