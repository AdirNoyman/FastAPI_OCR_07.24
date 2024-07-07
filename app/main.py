import pathlib
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Get the path to the app
BASE_DIR = pathlib.Path(__file__).parent
app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
def home_view(request: Request):
    print(request)
    return templates.TemplateResponse("home.html", {"request": request, "msg": "Adiros The Great 😎🤘"})


@app.post("/")
def home_detail_view():
    return {"Hello": "Adiros details"}
