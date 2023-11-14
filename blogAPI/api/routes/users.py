from fastapi import FastAPI
from fastapi import APIRouter

router = APIRouter(
    tags=['User Routes']
)



@router.get("/")
def get():
    return {"msg": "World"}

# @router.post("/hel")
# def get():
#     return {"msg": "World"}