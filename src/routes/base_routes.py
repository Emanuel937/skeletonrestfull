from fastapi import FastAPI

from routes.user_routes import router as user_routes
from routes.tag_routes import router as tag_routes
from routes.content_routes import router as content_routes
from routes.contentmeta_routes import router as content_meta_routes
from routes.contenttag_routes import router as content_tag_routes
from routes.userprogression_routes import router as user_progress_routes
from routes.media_routes import router as media_routes
from routes.assets_routes import router as assets_routes
from routes.test import router as testing


def base_routes(app: FastAPI):
    app.include_router(user_routes)
    app.include_router(tag_routes)
    app.include_router(content_routes)
    app.include_router(content_meta_routes)
    app.include_router(content_tag_routes)
    app.include_router(user_progress_routes)
    app.include_router(media_routes)
    app.include_router(assets_routes)
    app.include_router(testing)
