from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import data_router, indicators_router, documentation_router

app = FastAPI(
    root_path="/api",
    title="Data API",
    description="An API for fetching data about cryptocurrencies and calculating technical indicators.",
    version="0.0.1",
)

app.include_router(data_router)
app.include_router(indicators_router)
app.include_router(documentation_router)

# For future implementation:
# Adds CORS middleware to control which origins, methods, and headers can interact with the API.
# Essential for enabling secure cross-origin requests, especially when integrating with frontend applications.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Startup event
async def lifespan():
    print("HELLO WORLD 🌍")
    yield
    print("BY WORLD 🌍")

# Default root endpoint
@app.get("/")
async def root():
    return {"message": "That's a small step for a man, but even smaller for an ant."}
