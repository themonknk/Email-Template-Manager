from flask import render_template

def generate_email_content(template_id, custom_message):
    # Dynamically load template and insert custom content
    if template_id == '1':
        return render_template('template1.html', message=custom_message)
    elif template_id == '2':
        return render_template('template2.html', message=custom_message)
    else:
        return "Invalid Template"
