from fastapi import APIRouter

from .get import router as router_get
from .get_all import router as router_get_all
from .content import router as router_content
from .faq import router as router_faq
from .info import router as router_info
router = APIRouter(
    prefix="/settings",
    tags=['Settings'],
)
routers = [
    router_get, router_get_all, router_content,router_faq,router_info
]

[router.include_router(router_) for router_ in routers]
