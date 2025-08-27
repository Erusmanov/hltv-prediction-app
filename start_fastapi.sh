#!/bin/bash
echo "Starting CS2 Analytics FastAPI Application..."
export DATABASE_URL="sqlite:///./cs2_analytics.db"
export PYTHONPATH="/home/runner/workspace:$PYTHONPATH"
cd /home/runner/workspace
python main.py