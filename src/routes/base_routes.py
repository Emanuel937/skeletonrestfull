from fastapi import FastAPI
from routes import (user_routes, tags_route, media_route,
item_tags_route, item_routes, item_meta_route, item_media_route,
item_categories_route, comment_route
)

def includeRoutes(app):
    app.include_router(user_routes)
    app.include_router(tags_route)
    app.include_router(media_route)
    app.include_router(item_categories_route)
    app.include_router(item_tags_route)
    app.include_router(item_routes)
    app.include_router(item_media_route)
    app.include_router(comment_route)
    app.include_router(item_media_route)
   