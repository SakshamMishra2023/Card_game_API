from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Card Model
class Card(BaseModel):
    rank: str
    suit: str
    name: str

# Player Model
class Player:
    def __init__(self, name: str, balance: float = 100.0):
        self.name = name
        self.balance = balance
        self.cards = []
        self.current_bet = 0.0
        self.is_active = True

    def place_bet(self, amount: float):
        if amount > self.balance:
            return False, "Insufficient balance."
        self.balance -= amount
        self.current_bet += amount
        return True, None

    def fold(self):
        self.is_active = False

# Game Model
class Game:
    def __init__(self):
        self.players = []
        self.is_active = False
        self.current_turn_order = []
        self.current_turn_index = 0
        self.pot = 0.0
        self.deck = []

    def add_player(self, name: str):
        if any(player.name == name for player in self.players):
            raise HTTPException(status_code=400, detail="Player already in the game.")
        player = Player(name)
        self.players.append(player)
        return player

    def find_player(self, name: str):
        for player in self.players:
            if player.name == name:
                return player
        raise HTTPException(status_code=404, detail="Player not found.")

# API Models
class JoinGameRequest(BaseModel):
    name: str

class BetRequest(BaseModel):
    name: str
    amount: float

class FoldRequest(BaseModel):
    name: str

class GameStatusResponse(BaseModel):
    is_active: bool
    pot: float
    current_turn: Optional[str]
    players: List[dict]

class EndGameResponse(BaseModel):
    message: str

# Game instance
game = Game()

@app.post("/join")
def join_game(request: JoinGameRequest):
    player = game.add_player(request.name)
    return {"message": f"{player.name} joined the game."}

@app.post("/bet")
def place_bet(request: BetRequest):
    player = game.find_player(request.name)
    success, error = player.place_bet(request.amount)
    if not success:
        raise HTTPException(status_code=400, detail=error)
    game.pot += request.amount
    return {"message": f"{player.name} placed a bet of {request.amount}."}
 
@app.post("/fold")
def fold(request: FoldRequest):
    player = game.find_player(request.name)
    player.fold()
    return {"message": f"{player.name} folded."}

@app.get("/status", response_model=GameStatusResponse)
def get_game_status():
    return GameStatusResponse(
        is_active=game.is_active,
        pot=game.pot,
        current_turn=game.current_turn_order[game.current_turn_index] if game.current_turn_order else None,
        players=[{"name": p.name, "balance": p.balance, "active": p.is_active} for p in game.players]
    )
