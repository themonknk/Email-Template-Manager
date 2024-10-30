from flask import Blueprint, jsonify, request
import openai

user_behavior_bp = Blueprint('user_behavior', __name__)

@user_behavior_bp.route('/analyze_user_behavior', methods=['POST'])
def analyze_user_behavior():
    data = request.json
    user_actions = data['user_actions']
    
    # AI prompt to predict user preferences based on their behavior
    prompt = f"Analyze the following user actions and predict what type of email templates they might prefer: {user_actions}."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )

    return jsonify({'predicted_preferences': response.choices[0].text.strip()})