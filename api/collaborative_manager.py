from flask_socketio import SocketIO, emit
from flask import Blueprint

collaborative_bp = Blueprint('collaborative', __name__)
socketio = SocketIO()

@socketio.on('collaborative-editing')
def handle_collaborative_editing(data):
    emit('collaborative-editing', data, broadcast=True)