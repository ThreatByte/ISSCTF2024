from datetime import timedelta
from flask import Flask, session
import os
# from .ai_module import setup_openai_api

def create_app():
    app = Flask(__name__)

    # setup_openai_api()
    
    app.secret_key = os.urandom(24).hex()
    app.permanent_session_lifetime = timedelta(days=7)

    @app.before_request
    def ensure_session_id():
        if 'user_id' not in session:
            session['user_id'] = os.urandom(24).hex()

    from .views import main
    app.register_blueprint(main)

    return app