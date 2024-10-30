document.addEventListener('DOMContentLoaded', function () {
    window.saveReportTemplate = function () {
        const templateTitle = document.getElementById('templateTitle').value;
        const sectionOrder = Array.from(document.getElementById('sectionOrder').selectedOptions).map(option => option.value);

        fetch('/api/save_report_template', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ templateTitle, sectionOrder })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('templateStatus').innerHTML = `<p>${data.message}</p>`;
        })
        .catch(() => {
            document.getElementById('templateStatus').innerHTML = `<p>Error saving template. Please try again.</p>`;
        });
    };
});