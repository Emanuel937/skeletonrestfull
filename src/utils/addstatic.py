from fastapi.staticfiles import StaticFiles

def add_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")