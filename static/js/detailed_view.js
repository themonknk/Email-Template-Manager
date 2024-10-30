document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const dataType = urlParams.get('type');
    const label = urlParams.get('label');
    const annotationList = document.getElementById('annotationList');

    // Load AI insights and chart data
    fetch(`/api/generate_insights`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ label: label, data: dataType })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('aiInsights').innerHTML = `<p>${data.insights}</p>`;
    });

    // Example data for the drill-down chart with trend lines
    const ctx = document.getElementById('drillDownChart').getContext('2d');
    const drillDownChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4'],
            datasets: [{
                label: `Details for ${label}`,
                data: [10, 25, 30, 50],
                borderColor: '#4CAF50',
                fill: false,
                trendlineLinear: {
                    style: "rgba(255,105,180, .8)",
                    lineStyle: "solid",
                    width: 2
                }
            }]
        },
        options: {
            responsive: true,
            annotation: {
                annotations: [] // Dynamic annotation array
            }
        }
    });

    // Add annotation functionality
    window.addAnnotation = function () {
        const annotationText = document.getElementById('annotationInput').value;
        if (annotationText.trim()) {
            annotationList.innerHTML += `<li>${annotationText}</li>`;
            drillDownChart.options.annotation.annotations.push({
                type: 'line',
                mode: 'vertical',
                scaleID: 'x-axis-0',
                value: drillDownChart.data.labels[drillDownChart.data.labels.length - 1],
                borderColor: 'red',
                label: { content: annotationText, enabled: true, position: 'top' }
            });
            drillDownChart.update();
            document.getElementById('annotationInput').value = '';
        }
    };
});

document.addEventListener('DOMContentLoaded', function () {
    const annotationList = document.getElementById('annotationList');

    // Create Scatter Plot Chart
    const scatterCtx = document.getElementById('scatterPlotChart').getContext('2d');
    const scatterPlotChart = new Chart(scatterCtx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Engagement Scatter Plot',
                data: [{x: 10, y: 20}, {x: 15, y: 35}, {x: 20, y: 45}],
                backgroundColor: '#FF6384',
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { type: 'linear', position: 'bottom' },
                y: { beginAtZero: true }
            }
        }
    });

    // Create Heat Map Chart
    const heatMapCtx = document.getElementById('heatMapChart').getContext('2d');
    const heatMapChart = new Chart(heatMapCtx, {
        type: 'bubble',
        data: {
            datasets: [{
                label: 'Engagement Heat Map',
                data: [{x: 10, y: 30, r: 15}, {x: 15, y: 40, r: 10}, {x: 20, y: 25, r: 20}],
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { type: 'linear', position: 'bottom' },
                y: { beginAtZero: true }
            }
        }
    });

    // Annotation Sharing Functionality
    window.shareAnnotations = function () {
        const annotations = Array.from(annotationList.children).map(item => item.textContent);
        fetch('/api/share_annotations', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ annotations: annotations })
        })
        .then(response => response.json())
        .then(data => alert('Annotations shared successfully!'));
    };
});