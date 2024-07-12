from fastapi import FastAPI, APIRouter

from views import user_route, assets_route

app = FastAPI()
router = APIRouter()

@app.router.get('/')
def first():
    return 'Hell-o world'

app.include_router(prefix='/first', router=router)
app.include_router(user_route)
app.include_router(assets_route)