__all__ = ["data_router", "indicators_router", "documentation_router"]

from app.api.routes.data_api import router as data_router
from app.api.routes.indicators_api import router as indicators_router
from app.api.routes.documentation_api import router as documentation_router