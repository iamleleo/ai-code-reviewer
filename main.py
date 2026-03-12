from flask import Flask
from routes.health import bp as health_bp

app = Flask(__name__)

@app.route('/')
def root():
    return 'Welcome to the AI Code Reviewer API!'

# Register blueprints
app.register_blueprint(health_bp)