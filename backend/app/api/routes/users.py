from fastapi import APIRouter

router = APIRouter()

@router.post("/me")
def me():
    pass

@router.post("/stack")
def stack():
    pass