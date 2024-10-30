from flask import Blueprint, jsonify, request, render_template

template_editor_bp = Blueprint('template_editor', __name__, template_folder='../templates')

@template_editor_bp.route('/select_template')
def select_template():
    return render_template('select_template.html')

@template_editor_bp.route('/save_report_template', methods=['POST'])
def save_report_template():
    data = request.json
    template_title = data['templateTitle']
    section_order = data['sectionOrder']

    # Logic to save the template layout for future report generation
    # Save template to a database or file system for persistent use

    return jsonify({'message': 'Report template saved successfully!'})