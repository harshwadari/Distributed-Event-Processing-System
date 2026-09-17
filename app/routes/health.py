from fastapi import APIRouter

router = APIRouter()


@router.get("/health/live")
def health_live():
    return {"status": "ok"}