from typing import Union

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from uuid import uuid4
from time import sleep

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "id": id, "user_id": str(uuid4())}
    )


@app.get("/list_available_models")
async def list_available_models(request: Request):
    return HTMLResponse(
        """
        <ul>
	  		<li>first item</li>
	  		<li>first item</li>
	  		<li>first item</li>
	  		<li>first item</li>
	  		<li>first item</li>
  		</ul>
	"""
    )


# Get existing sessions


@app.get("/api/populate")
async def api_populate():
    global session
    return session.api_populate()
