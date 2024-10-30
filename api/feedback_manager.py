from flask import Blueprint, jsonify, request
import openai

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/submit_collaborative_feedback', methods=['POST'])
def submit_collaborative_feedback():
    data = request.json
    feedback = data['feedback']
    
    # Use collaborative feedback to refine AI-generated insights
    prompt = f"Refine the AI-generated insights based on the following feedback: {feedback}."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )

    return jsonify({'message': 'Feedback integrated successfully! AI insights updated.'})