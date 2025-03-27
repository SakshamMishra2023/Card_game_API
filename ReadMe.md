# Card Game Project

## Overview
This is a simple poker game implementation using FastAPI, featuring a basic game logic with player management, betting, and folding mechanics.

## Project Structure
- `models.py`: Contains core game logic and API endpoints
- `init.py`: Player API proxy server
- `autoTest.py`: Pytest test suite for API endpoints

## Features
- Player join game
- Place bets
- Fold during gameplay
- Game status tracking

## Prerequisites
- Python 3.8+
- FastAPI
- httpx
- pytest
- uvicorn
- requests

## Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn httpx pytest requests
   ```

## Running the Application
### Dealer API (Game Server)
```bash
python models.py
```
- Runs on `http://127.0.0.1:8000`

### Player API (Proxy Server)
```bash
python init.py
```
- Runs on `http://127.0.0.1:8001`

## API Endpoints
### Dealer API
- `POST /join`: Join the game
- `POST /bet`: Place a bet
- `POST /fold`: Fold current hand
- `GET /status`: Get current game status

### Player API
- Proxies requests to Dealer API with identical endpoints

## Running Tests
```bash
pytest autoTest.py
```
