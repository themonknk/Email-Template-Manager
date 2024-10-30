import openai

openai.api_key = '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'

def generate_new_template(template_type, audience, reason):
    prompt = f"Generate an email template for {template_type}. The audience is {audience} and the reason is {reason}."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=400
    )
    return response.choices[0].text.strip()
