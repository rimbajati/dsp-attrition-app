from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def get_dashboard():
    return render_template('dashboard_view.html')

# Handler for Vercel serverless function
def handler(request):
    with app.request_context(request):
        return app.full_dispatch_request()