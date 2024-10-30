document.addEventListener('DOMContentLoaded', function () {
    window.submitCollabFeedback = function () {
        const feedback = document.getElementById('collabFeedbackInput').value;

        fetch('/api/submit_collaborative_feedback', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ feedback })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('feedbackResponse').innerHTML = `<p>${data.message}</p>`;
        })
        .catch(() => {
            document.getElementById('feedbackResponse').innerHTML = `<p>Error submitting feedback. Please try again.</p>`;
        });
    };
});