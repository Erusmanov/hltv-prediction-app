"""
Simplified FastAPI server for CS2 Analytics
"""
import os
import sqlite3
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import uvicorn

# Create FastAPI app
app = FastAPI(
    title="CS2 Analytics FastAPI",
    description="Python backend for CS2 esports analytics",
    version="1.0.0"
)

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple in-memory storage
matches_store = []
teams_store = []

@app.on_event("startup") 
def startup():
    """Initialize app on startup"""
    print("🚀 FastAPI CS2 Analytics starting...")
    
    # Create sample data
    global teams_store, matches_store
    
    teams_store = [
        {"id": "1", "name": "Passion UA", "short_name": "PUA", "created_at": datetime.now()},
        {"id": "2", "name": "ENCE", "short_name": "ENCE", "created_at": datetime.now()},
        {"id": "3", "name": "fnatic", "short_name": "FNC", "created_at": datetime.now()},
        {"id": "4", "name": "PARIVISION", "short_name": "PRV", "created_at": datetime.now()},
        {"id": "5", "name": "500", "short_name": "500", "created_at": datetime.now()},
    ]
    
    matches_store = [
        {
            "id": "match_1",
            "team1_id": "1",
            "team2_id": "5",
            "tournament": "CCT Season 3 Europe Series 5",
            "start_time": datetime.now(),
            "format": "BO3",
            "status": "live",
            "maps_score": "1:1",
            "rounds_score": "12:8",
            "current_map": "de_mirage",
            "odds_team1": "2.15",
            "odds_team2": "1.87",
            "bookmaker_name": "1xBet"
        },
        {
            "id": "match_2", 
            "team1_id": "2",
            "team2_id": "3",
            "tournament": "ESL Challenger League Season 48",
            "start_time": datetime.now(),
            "format": "BO3",
            "status": "upcoming",
            "odds_team1": "1.92",
            "odds_team2": "2.25",
            "bookmaker_name": "1xBet"
        }
    ]
    
    print("✅ FastAPI initialized with sample data")

@app.get("/")
async def root():
    return {"message": "CS2 Analytics FastAPI Backend", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy", "backend": "FastAPI Python"}

@app.get("/api/matches-fastapi")
async def get_matches():
    """Get matches from FastAPI backend"""
    
    # Add team data to matches
    matches_with_teams = []
    for match in matches_store:
        team1 = next((t for t in teams_store if t["id"] == match["team1_id"]), None)
        team2 = next((t for t in teams_store if t["id"] == match["team2_id"]), None)
        
        match_data = match.copy()
        match_data["team1"] = team1
        match_data["team2"] = team2
        matches_with_teams.append(match_data)
    
    return {
        "message": "Matches from FastAPI Python backend",
        "matches": matches_with_teams,
        "total": len(matches_with_teams),
        "backend": "FastAPI"
    }

@app.get("/api/teams-fastapi")
async def get_teams():
    """Get teams from FastAPI backend"""
    return {
        "message": "Teams from FastAPI Python backend", 
        "teams": teams_store,
        "total": len(teams_store),
        "backend": "FastAPI"
    }

@app.post("/api/analyze-match/{match_id}")
async def analyze_match(match_id: str):
    """Generate match analysis using Python AI"""
    
    match = next((m for m in matches_store if m["id"] == match_id), None)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    
    team1 = next((t for t in teams_store if t["id"] == match["team1_id"]), None)
    team2 = next((t for t in teams_store if t["id"] == match["team2_id"]), None)
    
    # Simple AI analysis
    analysis = {
        "match_id": match_id,
        "predicted_winner": team1["name"],
        "win_probability": 0.65,
        "confidence": 0.78,
        "reasoning": f"Анализ показывает, что {team1['name']} имеет преимущество в текущей форме и опыте на турнирах подобного уровня.",
        "betting_recommendations": [
            {
                "type": "Winner",
                "description": f"Победа {team1['name']}",
                "odds": 2.15,
                "recommendation": "recommended",
                "stake": "medium"
            }
        ],
        "risk_factors": ["Возможная усталость после недавних матчей"],
        "backend": "FastAPI Python AI"
    }
    
    return analysis

if __name__ == "__main__":
    print("Starting FastAPI CS2 Analytics server...")
    uvicorn.run(
        app,
        host="0.0.0.0", 
        port=5001,
        log_level="info"
    )