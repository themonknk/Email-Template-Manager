from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os

file_manager_bp = Blueprint('file_manager', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@file_manager_bp.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = os.path.join(current_app.root_path, 'static/uploads')
        os.makedirs(upload_folder, exist_ok=True)
        file.save(os.path.join(upload_folder, filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 201

    return jsonify({'error': 'File type not allowed'}), 400

@file_manager_bp.route('/list_files', methods=['GET'])
def list_files():
    upload_folder = os.path.join(current_app.root_path, 'static/uploads')
    files = os.listdir(upload_folder)
    return jsonify(files)