from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn



templates = Jinja2Templates(directory="templates")
app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request:Request):
    return templates.TemplateResponse("about.html",{"request":request})

@app.get("/contact", response_class=HTMLResponse)
async def about(request:Request):
    return templates.TemplateResponse("contact.html",{"request":request})

