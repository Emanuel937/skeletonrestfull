from fastapi import FastAPI
from middleware.cors import add_cors_middleware
from routes.base_routes import base_routes
from utils.addstatic import add_static

app = FastAPI()

add_cors_middleware(app)
add_static(app)
base_routes(app)
