import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI
from routers import user, auth, balance, criteria, feedback, menu, orders


app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(balance.router)
app.include_router(criteria.router)
app.include_router(feedback.router)
app.include_router(menu.router)
app.include_router(orders.router)
