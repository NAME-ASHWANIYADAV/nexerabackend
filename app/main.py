# app/main.py
import redis.asyncio as redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Try to import FastAPILimiter (may fail on some versions)
try:
    from fastapi_limiter import FastAPILimiter
    HAS_LIMITER = True
except ImportError:
    HAS_LIMITER = False
    print("⚠️ FastAPILimiter not available, rate limiting disabled")

# Load environment variables from .env file for local development
load_dotenv()

from app.core.config import settings
from app.core.db import connect_to_mongo, close_mongo_connection, get_database_client
from app.api.routers import api_router
from app.discovery.clawd_agent import initialize_agent, shutdown_agent

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

# CORS middleware - allow only the frontend origin in production
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    # Connect to databases
    await connect_to_mongo()
    
    # Initialize the rate limiter (if available and Redis configured)
    if HAS_LIMITER and settings.REDIS_URL:
        try:
            redis_connection = redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)
            await FastAPILimiter.init(redis_connection)
            print("✅ Rate limiter initialized")
        except Exception as e:
            print(f"⚠️ Rate limiter init failed: {e}")
    
    # Initialize and start the job discovery agent
    db_client = get_database_client()
    initialize_agent(db_client)

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()
    shutdown_agent()

# The custom exception handler is removed, as this version of the library
# raises HTTPException directly, which FastAPI handles by default.

app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Job Companion Backend"}

