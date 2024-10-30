from flask import Blueprint, jsonify, request
import openai

ai_model_bp = Blueprint('ai_model', __name__)

@ai_model_bp.route('/improve_ai_model', methods=['POST'])
def improve_ai_model():
    data = request.json
    feedback = data['feedback']
    
    # Logic to use feedback to fine-tune AI model (e.g., storing feedback and retraining)
    improved_prompt = f"Based on user feedback: {feedback}, enhance the insights generation for email campaigns."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=improved_prompt,
        max_tokens=150,
        temperature=0.6
    )

    return jsonify({'improvement_message': 'AI model updated successfully with new feedback!'})