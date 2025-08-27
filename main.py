"""
FastAPI main application for CS2 esports analytics bot
"""
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
from typing import List, Optional
import uvicorn

from app.database import init_db, get_db_session
# Remove unused imports to fix errors
from app.services.hltv_scraper import HLTVScraper
from app.services.gemini_analyzer import GeminiAnalyzer
from app.services.telegram_bot import TelegramBot
from app.routers import matches, teams, analytics, admin


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application on startup"""
    print("Starting CS2 Analytics FastAPI application...")
    
    # Initialize database
    await init_db()
    
    # Initialize services
    app.state.hltv_scraper = HLTVScraper()
    app.state.gemini_analyzer = GeminiAnalyzer()
    
    # Start Telegram bot
    if os.getenv("TELEGRAM_BOT_TOKEN"):
        app.state.telegram_bot = TelegramBot()
        await app.state.telegram_bot.start()
        print("Telegram bot started")
    
    yield
    
    # Cleanup on shutdown
    if hasattr(app.state, 'telegram_bot'):
        await app.state.telegram_bot.stop()


# Create FastAPI app with lifespan
app = FastAPI(
    title="CS2 Esports Analytics API",
    description="AI-powered CS2 match analytics and betting predictions",
    version="2.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(matches.router, prefix="/api", tags=["matches"])
app.include_router(teams.router, prefix="/api", tags=["teams"])
app.include_router(analytics.router, prefix="/api", tags=["analytics"])
app.include_router(admin.router, prefix="/api", tags=["admin"])

# Static files will be served by the existing Node.js server
# app.mount("/", StaticFiles(directory="client/dist", html=True), name="static")


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": "2.0.0"}


if __name__ == "__main__":
    # For development
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5001,
        reload=True,
        log_level="info"
    )