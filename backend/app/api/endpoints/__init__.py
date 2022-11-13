from fastapi import APIRouter
from .prices import router as prices_router
from .users import router as users_router
from .products import router as products_router

router = APIRouter()
router.include_router(router=users_router)
router.include_router(router=prices_router)
router.include_router(router=products_router)