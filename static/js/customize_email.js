document.getElementById('customize-email-form').onsubmit = async function (event) {
    event.preventDefault();
    const emailId = /* Get the email ID from the context */;
    const condition = document.getElementById('condition').value;
    const delay = document.getElementById('followUpDelay').value;
    const followUpContent = document.getElementById('followUpContent').value;

    const response = await fetch('/api/create_follow_up', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            email_id: emailId,
            condition: condition,
            delay: delay,
            content: followUpContent
        })
    });

    const result = await response.json();
    if (response.ok) {
        alert('Follow-up email set successfully!');
    } else {
        alert('Error setting follow-up email: ' + result.error);
    }
};