import pathlib
import uvicorn
from app.core.create_app import App
from app.core.docs import docs_router
from fastapi.routing import APIRouter
from app.core.db import engine, metadata


BASE_PATH = pathlib.Path(pathlib.Path(__file__).parent.parent)


test_router = APIRouter(prefix="/test", tags=["Test endpoint"])


@test_router.get(
    "/test-api/",
)
async def test():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"message": "Hello there"}


routers = (test_router, docs_router)

instance = App("FastApi Posts", routers, APP_HOME=BASE_PATH, prefix="/api")

metadata.create_all(engine)

app = instance.configure()


@app.on_event("startup")
async def startup():
    print("Application startup")


@app.on_event("shutdown")
async def shutdown():
    print("Application shutdown")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=1)
