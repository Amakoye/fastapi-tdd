from pathlib import Path
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.core import settings

docs_router = APIRouter(include_in_schema=False)
directory = Path(__file__).joinpath("../templates").resolve()
templates = Jinja2Templates(directory)


@docs_router.get("/docs/", response_class=HTMLResponse)
def view_documenntation(request: Request):
    root = getattr(settings, "APP_PREFIX", "")
    url = root + "/openapi.json"
    return templates.TemplateResponse(
        "docs.html",
        {"request": request, "schema_url": url},
    )
