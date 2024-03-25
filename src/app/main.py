import pathlib
import uvicorn
from core.create_app import App
from core.docs import docs_router
from fastapi.routing import APIRouter


BASE_PATH = pathlib.Path(pathlib.Path(__file__).parent.parent)

test_router = APIRouter(prefix="/test", tags=["Test endpoint"])


@test_router.get(
    "/test-api/",
)
def test():
    return {"message": "Hello there"}


routers = (test_router, docs_router)

instance = App("FastApi Posts", routers, APP_HOME=BASE_PATH, prefix="/api")

app = instance.configure()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
