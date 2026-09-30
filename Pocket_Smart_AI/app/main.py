from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import auth, dashboard

app = FastAPI()

# Mount Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])

@app.get("/")
def home():
    return {"message": "Welcome to PocketSmart AI API"}

