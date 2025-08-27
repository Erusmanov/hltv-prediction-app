# replit.md

## Overview

This is a CS2 (Counter-Strike 2) esports analytics application that scrapes match data from HLTV, analyzes it using Google Gemini AI, and provides betting recommendations through both a web interface and Telegram bot. The application focuses on providing AI-powered predictions for upcoming CS2 matches with detailed team statistics, head-to-head records, and risk assessments. Additionally, it includes a comprehensive admin panel for bot management and broadcasting posts to all users.

## User Preferences

Preferred communication style: Simple, everyday language.
Programming languages: Successfully migrated to hybrid architecture with Python backend (Flask/FastAPI) alongside existing TypeScript frontend.

## System Architecture

### Frontend Architecture
The client is built with React, TypeScript, and Vite, featuring a responsive design optimized for both desktop and mobile viewing. The UI uses shadcn/ui components with Radix UI primitives and Tailwind CSS for styling, implementing a Telegram-inspired color scheme. The application uses Wouter for client-side routing and TanStack Query for efficient API state management and caching.

### Backend Architecture
**Hybrid Python/TypeScript Architecture**: The application now runs a dual backend system:
- **Primary Backend**: Flask/Python server on port 5002 providing AI-powered match analysis, realistic team data, and Python-based predictions
- **Legacy Backend**: Express.js/TypeScript server on port 5000 maintaining existing Telegram bot functionality and frontend serving
- **FastAPI Implementation**: Complete FastAPI application structure created with SQLAlchemy models, Pydantic schemas, and async services for future migration

The Python backend includes advanced features like realistic CS2 team data (Passion UA, ENCE, fnatic, etc.), live match simulation, and AI-powered analysis with betting recommendations. The architecture follows REST API patterns with proper CORS configuration for cross-origin requests.

### Data Storage Solutions
The application uses Drizzle ORM with PostgreSQL for data persistence, with Neon Database as the hosting provider. The database schema includes tables for teams, matches, match analytics, predictions, bot users, broadcast posts, and admin sessions, with proper foreign key relationships. The system implements an in-memory storage solution for development and testing scenarios.

### Authentication and Authorization
Currently implements a minimal authentication system, designed to be extended with proper user authentication and authorization mechanisms as needed.

### External Service Integrations
- **HLTV Scraping**: Uses Puppeteer to scrape upcoming matches and team statistics from HLTV.org
- **Google Gemini Integration**: Leverages Gemini AI for match analysis, generating detailed predictions with confidence scores and betting recommendations
- **Telegram Bot**: Provides a Telegram Web App interface for mobile-optimized access to match analytics, plus admin panel functionality
- **Admin Broadcasting System**: Allows authorized administrators to create and broadcast posts to all bot users
- **Neon Database**: Cloud PostgreSQL database for production data storage with in-memory fallback

### Key Architectural Decisions

**Web Scraping Strategy**: Chose Puppeteer over simple HTTP requests to handle HLTV's dynamic content and anti-bot measures, allowing reliable data extraction from the most authoritative CS2 esports source.

**AI Analysis Pipeline**: Integrated OpenAI's GPT models to process raw match statistics and generate human-readable insights with confidence scoring, providing value beyond simple data aggregation.

**Dual Interface Approach**: Implemented both a traditional web interface and Telegram Web App to maximize accessibility, particularly for mobile users who prefer messaging platforms.

**Admin Management System**: Created a secure admin panel accessible via `/ernest` command with password authentication, enabling post creation and broadcasting to all bot users.

**Real-time Data Flow**: Designed the system to refresh match data on-demand while caching results appropriately, balancing data freshness with API rate limits and performance.

## External Dependencies

- **Database**: PostgreSQL via Neon Database (@neondatabase/serverless) with in-memory fallback
- **ORM**: Drizzle ORM with Zod schema validation
- **Web Scraping**: Puppeteer for HLTV data extraction
- **AI Service**: Google Gemini API for match analysis
- **Telegram**: Telegraf framework for bot functionality with admin panel
- **Frontend**: React, TypeScript, Vite build system
- **UI Components**: Radix UI primitives via shadcn/ui
- **Styling**: Tailwind CSS with custom Telegram-inspired theme
- **State Management**: TanStack React Query for server state
- **Date Handling**: date-fns for time calculations and formatting