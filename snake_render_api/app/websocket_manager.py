from fastapi import WebSocket
from app.session_manager import SessionManager
import json

class WebSocketManager:
    def __init__(self):
        self.active_connections = {}  # Maps session_id to WebSocket

    async def connect(self, session_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[session_id] = websocket

    async def disconnect(self, session_id: str):
        if session_id in self.active_connections:
            del self.active_connections[session_id]

    async def send_game_state(self, session_id: str, game):
        if session_id in self.active_connections:
            websocket = self.active_connections[session_id]
            state = {
                "rendered_state": game.renderGame(),
                "score": game.getScore(),
                "is_game_over": game.isGameOver(),
            }
            await websocket.send_text(json.dumps(state))