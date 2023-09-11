from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import Form
import datetime



templates = Jinja2Templates(directory="templates")
app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submitBooking")
async def submitBooking(pickup: str = Form(...), dropoff: str = Form(...),date: datetime.date=Form(...),time: datetime.time=Form(...)):
   print(pickup,"\n",dropoff,"\n",date,"\n",time)
   
   return {"pickup": pickup,"dropoff":dropoff,"date":date,"time":time}



@app.get("/about/", response_class=HTMLResponse)
async def about(request:Request):
    return templates.TemplateResponse("about.html",{"request":request})

@app.get("/contact/", response_class=HTMLResponse)
async def about(request:Request):
    return templates.TemplateResponse("contact.html",{"request":request})

@app.post("/contact/submitContact")
async def submitContact(name:str=Form(...),email:str=Form(...),msg:str=Form()):
    print("\n",name,"\n",email,"\n",msg)
    return {"name":name,"email":email,"msg":msg}