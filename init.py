import logging
import uvicorn
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

PLAYER_NAME = "Player1"
PLAYER_API_URL = "http://127.0.0.1:8001" 
DEALER_API_URL = "http://127.0.0.1:8000"

app = FastAPI()



class JoinGameRequest(BaseModel):
    name: str

class BetRequest(BaseModel):
    name: str
    amount: float

class FoldRequest(BaseModel):
    name: str

@app.post("/join")
def join_game(request: JoinGameRequest):
    
    try:
        
        response = requests.post(f"{DEALER_API_URL}/join", json=request.dict())
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.post("/bet")
def place_bet(request: BetRequest):
   
    try:
        response = requests.post(f"{DEALER_API_URL}/bet", json=request.dict())
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.post("/fold")
def fold(request: FoldRequest):
    
    try:
        response = requests.post(f"{DEALER_API_URL}/fold", json=request.dict())
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        raise HTTPException(status_code=response.status_code, detail=response.text)

if __name__ == "__main__":
    logging.info("Starting Player API...")
    uvicorn.run(app, host="127.0.0.1", port=8001)
