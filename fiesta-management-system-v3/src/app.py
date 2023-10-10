from fastapi import FastAPI

from src.helpers.loggers import setup_logger
from src.routers import user, auth, balance, criteria, feedback, menu, orders


setup_logger()
app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(balance.router)
app.include_router(criteria.router)
app.include_router(feedback.router)
app.include_router(menu.router)
app.include_router(orders.router)
