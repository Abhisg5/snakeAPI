from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.session_manager import SessionManager
from app.websocket_manager import WebSocketManager
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Session and WebSocket managers
session_manager = SessionManager()
websocket_manager = WebSocketManager()

# HTML templates for embedding
templates = Jinja2Templates(directory="app/templates")

# Static assets (optional for iframe rendering)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Allow iframe embedding
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Snake Game API"}

# HTML endpoint to embed the game
@app.get("/embed/{session_id}", response_class=HTMLResponse)
def embed_game(session_id: str):
    game = session_manager.get_session(session_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game session not found")
    return templates.TemplateResponse("index.html", {"request": {}, "session_id": session_id})

# Start a new game session
@app.post("/game/start")
def start_game(width: int = 20, height: int = 20):
    session_id = session_manager.create_session(width, height)
    return {"message": "Game started", "session_id": session_id}

# Handle game state updates through WebSocket
@app.websocket("/ws/{session_id}")
async def game_websocket(session_id: str, websocket: WebSocket):
    game = session_manager.get_session(session_id)
    if not game:
        await websocket.close(code=1001)
        return

    await websocket_manager.connect(session_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            direction = data.upper()
            game.setDirection(direction)
            game.update()

            state = {
                "rendered_state": game.renderGame(),
                "score": game.getScore(),
                "is_game_over": game.isGameOver(),
            }
            await websocket.send_text(json.dumps(state))
    except WebSocketDisconnect:
        await websocket_manager.disconnect(session_id)