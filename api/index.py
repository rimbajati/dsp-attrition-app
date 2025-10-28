from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/api/test')
def test():
    return {"status": "ok", "message": "Hello from Flask!"}

@app.route('/')
def home():
    return "Welcome to Attrition App"

@app.route('/api/dashboard')
def get_dashboard():
    return {"status": "ok", "message": "Dashboard data here"}

# For local development
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)