from flask import Blueprint, request, jsonify
from models.template_model import EmailTemplate, db
from flask_login import current_user

template_manager_bp = Blueprint('template_manager', __name__)

@template_manager_bp.route('/create_template', methods=['POST'])
def create_template():
    data = request.json
    name = data.get('name')
    content = data.get('content')

    new_template = EmailTemplate(name=name, content=content, created_by=current_user.id)
    db.session.add(new_template)
    db.session.commit()

    return jsonify({'message': 'Template created successfully', 'template_id': new_template.id}), 201

@template_manager_bp.route('/get_templates', methods=['GET'])
def get_templates():
    templates = EmailTemplate.query.filter_by(created_by=current_user.id).all()
    template_list = [{'id': template.id, 'name': template.name, 'content': template.content} for template in templates]
    return jsonify(template_list)

@template_manager_bp.route('/delete_template/<int:template_id>', methods=['DELETE'])
def delete_template(template_id):
    template = EmailTemplate.query.get_or_404(template_id)
    if template.created_by != current_user.id:
        return jsonify({'error': 'Unauthorized action'}), 403

    db.session.delete(template)
    db.session.commit()
    return jsonify({'message': 'Template deleted successfully'})

@template_manager_bp.route('/save_template', methods=['POST'])
def save_template():
    data = request.json
    template_name = data.get('name')
    content = data.get('content')

    new_template = EmailTemplate(name=template_name, content=content)
    db.session.add(new_template)
    db.session.commit()

    return jsonify({'message': 'Template saved successfully', 'template_id': new_template.id}), 201