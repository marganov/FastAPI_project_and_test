"""
Main FastAPI application entry point.
"""
from fastapi import FastAPI

from routers.routers import router

app = FastAPI(
    title="FastAPI Authentication Project",
    version="1.0.0",
    description="Simple authentication system with session cookies",
)

# Include routers
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
