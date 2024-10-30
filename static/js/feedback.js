document.addEventListener('DOMContentLoaded', function () {
    window.submitFeedback = function () {
        const feedback = document.getElementById('feedbackInput').value;

        fetch('/api/submit_feedback', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ feedback })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('feedbackStatus').innerHTML = `<p>Thank you for your feedback!</p>`;
        })
        .catch(() => {
            document.getElementById('feedbackStatus').innerHTML = `<p>Error submitting feedback. Please try again.</p>`;
        });
    };
});