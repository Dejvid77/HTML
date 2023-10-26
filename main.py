from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

name = "Dejvid Dadic"
skills = ["AWS", "Python", "Git"]

@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": name, "skills": skills})

@app.get("/contact", response_class=HTMLResponse)
def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "name": name})

@app.post("/contact", response_class=HTMLResponse)
def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    return templates.TemplateResponse("sub_message.html", {"request": request, "name": name, "email": email, "message": message})