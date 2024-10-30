document.getElementById('ab-test-form').onsubmit = async function (event) {
    event.preventDefault();
    const variantA = document.getElementById('variantA').value;
    const variantB = document.getElementById('variantB').value;
    const duration = document.getElementById('duration').value;

    const response = await fetch('/api/create_ab_test', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            email_id: /* Fetch or get email ID dynamically */,
            variant_a: variantA,
            variant_b: variantB,
            duration: duration
        })
    });

    const result = await response.json();
    if (response.ok) {
        alert('A/B test created successfully!');
    } else {
        alert('Error creating A/B test: ' + result.error);
    }
};