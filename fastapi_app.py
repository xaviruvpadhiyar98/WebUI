from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from uuid import uuid4
from arel import HotReload
from arel import Path as ArelPath
import os


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

if _debug := os.getenv("DEBUG"):
    hot_reload = HotReload(paths=[ArelPath(".")])
    app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = _debug
    templates.env.globals["hot_reload"] = hot_reload


@app.get("/")
async def root(request: Request):
    return HTMLResponse("Hi")
    return templates.TemplateResponse(
        "index.html", {"request": request, "user_id": str(uuid4())}
    )

@app.get("/search")
async def search(request: Request):
    return templates.TemplateResponse(
        "search.html", {"request": request, "user_id": str(uuid4())}
    )

@app.get("/search-results")
async def search_results(q: str):
    results = ""
    for i in range(100):
        results += f"""
        <div class="cursor-pointer" hx-get="/clicked" hx-target="#results-container" hx-include="[name='question{i}']">
            <input
                type="hidden"
                name="question{i}"
                id="question{i}"
                value="{q}"
            />
            {q}
        </div>
        """  # noqa: E501
    return HTMLResponse(results)

@app.get("/clicked")
async def clicked(request: Request):
    values = request.query_params.values()
    print(values)
    return HTMLResponse("answer")




@app.get("/chat")
async def chat(request: Request):
    return templates.TemplateResponse(
        "chat.html", {"request": request}
    )

@app.get("/psd")
async def psd(request: Request):
    return templates.TemplateResponse(
        "psd.html", {"request": request}
    )

@app.get("/ctf")
async def ctf(request: Request):
    return templates.TemplateResponse(
        "ctf.html", {"request": request}
    )

@app.post("/send")
async def send_message(request: Request):
    return HTMLResponse("Hi")

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
