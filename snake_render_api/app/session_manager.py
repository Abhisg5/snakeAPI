from snake_game import SnakeGame  # Import C++ bindings

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, width=20, height=20):
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = SnakeGame(width, height)
        return session_id

    def get_session(self, session_id):
        return self.sessions.get(session_id)

    def delete_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]