from flask_socketio import SocketIO, emit
from flask import Blueprint

sync_bp = Blueprint('sync', __name__)
socketio = SocketIO()

@socketio.on('sync_request')
def handle_sync_request(data):
    emit('sync_response', data, broadcast=True)