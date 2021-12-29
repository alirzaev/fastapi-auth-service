from fastapi import APIRouter

from .auth import router as auth_router
from .utils import router as utils_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix='/auth')
api_router.include_router(utils_router, prefix='/utils')
