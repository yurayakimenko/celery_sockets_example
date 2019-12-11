from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from flask_socketio import send, emit
from celery_worker import generate_random
from extensions import socketio


bp = Blueprint('public', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/create_task', methods=['POST'])
def create_task():
    delay = request.form.get('delay')
    task_id = generate_random.apply_async()
    print(task_id)
    return jsonify({"status": "success"})

@bp.route('/notify')
def notify():
    socketio.emit('notify', {}, broadcast=True)
    return jsonify({"status": "success"})
