from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name:str
    email:str
    password:str

class LogUser(BaseModel):
    email:str
    password:str

data_path='Backend/database/career.db'
@app.post('/signup')
def signup(user:User):
    con=sqlite3.connect(data_path)
    cursor=con.cursor()
    try:
        cursor.execute(
            """INSERT INTO users(name,email,password) VALUES(?,?,?)""",
            (user.name,user.email,user.password))
        con.commit()
        return{
            'message':f'Hii{user.name}\nThankyou'
        }
    except Exception as e:
        return{
            #'error':str(e)
            'message':'You already Registered Here!'
        }
    finally:
        con.close()

@app.post('/login')
def login(user:LogUser):
    con=sqlite3.connect(data_path)
    cursor=con.cursor()
    try:
        cursor.execute(
            'SELECT * FROM users WHERE email=? AND password=?',(user.email,user.password))
        result=cursor.fetchone()
        con.commit()
        if result:
            _,name,email,_=result
            return{
                'message':'Login success',
                'name':name,
                'email':email
            }
        return{
            'message':'Invalid Credentials'
        }
    except Exception as e:
       return{
        'error':str(e)
        }
    finally:
        con.close()