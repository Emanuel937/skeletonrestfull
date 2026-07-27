
from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    origins = [
        "http://localhost:3000",  # your Next.js dev server
        # "https://your-production-domain.com", # production
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # or ["*"] for dev
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )