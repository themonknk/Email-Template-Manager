document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/get_advanced_email_analytics/1')  // Replace '1' with the actual email ID
        .then(response => response.json())
        .then(data => {
            createAdvancedAnalyticsCharts(data);
            displayInsights(data.insights);
        });

    function createAdvancedAnalyticsCharts(data) {
        const ctx = document.getElementById('advancedEmailAnalyticsChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Opens', 'Clicks', 'Bounces'],
                datasets: [{
                    label: 'Email Metrics',
                    data: [data.opens, data.clicks, data.bounces],
                    backgroundColor: ['#4CAF50', '#FFC107', '#F44336'],
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    function displayInsights(insights) {
        const insightsContainer = document.getElementById('insightsContainer');
        insightsContainer.innerHTML = `<p>${insights}</p>`;
    }
});