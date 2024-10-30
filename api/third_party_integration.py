from flask import Blueprint, jsonify, request
import requests

third_party_bp = Blueprint('third_party', __name__)

@third_party_bp.route('/connect_to_crm', methods=['POST'])
def connect_to_crm():
    crm_data = request.json
    response = requests.post('https://api.crmplatform.com/connect', json=crm_data)
    return jsonify({'crm_status': response.status_code, 'crm_response': response.json()})