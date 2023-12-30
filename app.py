from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated


app = FastAPI()

template = Jinja2Templates(directory='Templates')


@app.get('/home')
def home():
    return('Halooo')

@app.get('/home/submit-form', response_class=HTMLResponse)
def get_destination(request:Request):
    return template.TemplateResponse('template_login.html', {'request':request})

@app.post('/home/result', response_class=HTMLResponse)
def result(request:Request, username:str = Form(...), email:str = Form(...)):
    print(username)
    print(email)

    return template.TemplateResponse('result.html', {'request':request, 'nama':username, 'email':email})
 

