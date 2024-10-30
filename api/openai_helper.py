import openai

openai.api_key = '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'

def get_insights_from_data(data):
    prompt = f"Analyze the following email data and provide recommendations to improve performance: Opens: {data['opens']}, Clicks: {data['clicks']}, Bounces: {data['bounces']}. Suggest strategies to increase engagement."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip()