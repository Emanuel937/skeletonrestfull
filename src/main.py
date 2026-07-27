from fastapi import FastAPI
from middleware.cors import add_cors_middleware
from routes import base_routes

app = FastAPI()

add_cors_middleware(app)
base_routes(app)
