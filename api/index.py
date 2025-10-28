from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def get_dashboard():
    return render_template('dashboard_view.html')

@app.route('/api/health')
def health_check():
    return {"status": "ok", "message": "Service is healthy"}

# For local development
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)