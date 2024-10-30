from flask import Blueprint, request, jsonify
import openai

openai.api_key = 'your_openai_api_key_here'

insights_bp = Blueprint('insights', __name__)

@insights_bp.route('/generate_insights', methods=['POST'])
def generate_insights():
    data = request.json
    prompt = f"Analyze the following email data trends for {data['label']} and provide insights to optimize engagement: {data['data']}."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return jsonify({'insights': response.choices[0].text.strip()})

@insights_bp.route('/analyze_trends', methods=['POST'])
def analyze_trends():
    data = request.json
    prompt = f"Analyze the following trend in email data: {data['data']}. Identify any significant patterns and suggest optimizations."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.6
    )
    return jsonify({'trend_analysis': response.choices[0].text.strip()})

@insights_bp.route('/generate_custom_insights', methods=['POST'])
def generate_custom_insights():
    data = request.json
    prompt = f"Using custom analysis, provide deeper insights for the email campaign trends based on: {data['data']}."
    response = openai.Completion.create(
        model="text-curie-001",
        prompt=prompt,
        max_tokens=200,
        temperature=0.65
    )
    return jsonify({'custom_insights': response.choices[0].text.strip()})

@insights_bp.route('/share_annotations', methods=['POST'])
def share_annotations():
    data = request.json
    annotations = data['annotations']
    # Logic to send annotations via email or other sharing platforms
    # This can include sending emails to team members with the annotation details
    return jsonify({'message': 'Annotations shared successfully!'})

