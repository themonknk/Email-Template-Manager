document.addEventListener('DOMContentLoaded', function () {
    loadEmailPerformanceData();
    loadABTestSummaryData();
    loadScheduledEmailsData();
    loadRecentActivity();

    function loadEmailPerformanceData() {
        fetch('/api/get_email_performance')
            .then(response => response.json())
            .then(data => {
                const ctx = document.getElementById('emailPerformanceChart').getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: 'Open Rates',
                            data: data.openRates,
                            borderColor: '#4CAF50',
                            fill: false
                        }, {
                            label: 'Click Rates',
                            data: data.clickRates,
                            borderColor: '#FFC107',
                            fill: false
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
            });
    }

    function loadABTestSummaryData() {
        fetch('/api/get_ab_test_summary')
            .then(response => response.json())
            .then(data => {
                const ctx = document.getElementById('abTestSummaryChart').getContext('2d');
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: ['Variant A', 'Variant B'],
                        datasets: [{
                            label: 'Open Rates',
                            data: [data.variantA.openRate, data.variantB.openRate],
                            backgroundColor: ['#42A5F5', '#FFA726'],
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
            });
    }

    function loadScheduledEmailsData() {
        fetch('/api/get_scheduled_emails')
            .then(response => response.json())
            .then(emails => {
                const tableBody = document.getElementById('scheduledEmailsTable').querySelector('tbody');
                tableBody.innerHTML = emails.map(email => `
                    <tr>
                        <td>${email.subject}</td>
                        <td>${email.recipient}</td>
                        <td>${new Date(email.scheduledDate).toLocaleString()}</td>
                        <td>${email.status}</td>
                    </tr>
                `).join('');
            });
    }

    function loadRecentActivity() {
        fetch('/api/get_recent_activity')
            .then(response => response.json())
            .then(activity => {
                const recentActivityDiv = document.getElementById('recentActivity');
                recentActivityDiv.innerHTML = activity.map(item => `
                    <p>${item.description} - <small>${new Date(item.timestamp).toLocaleString()}</small></p>
                `).join('');
            });
    }


    let isEditMode = false;

    function toggleEditMode() {
        isEditMode = !isEditMode;
        const widgets = document.querySelectorAll('.widget');
        widgets.forEach(widget => {
            widget.setAttribute('draggable', isEditMode);
            widget.classList.toggle('editable', isEditMode);
        });
    }

    function saveDashboardLayout() {
        const layout = Array.from(document.querySelectorAll('.widget')).map(widget => widget.id);
        localStorage.setItem('dashboardLayout', JSON.stringify(layout));
        alert('Dashboard layout saved successfully!');
    }

    function loadDashboardLayout() {
        const layout = JSON.parse(localStorage.getItem('dashboardLayout'));
        if (layout) {
            const dashboard = document.getElementById('dashboardWidgets');
            layout.forEach(widgetId => {
                const widget = document.getElementById(widgetId);
                dashboard.appendChild(widget);
            });
        }
    }

    document.querySelectorAll('.widget').forEach(widget => {
        widget.addEventListener('dragstart', (event) => {
            event.dataTransfer.setData('text/plain', event.target.id);
        });

        widget.addEventListener('dragover', (event) => {
            event.preventDefault();
        });

        widget.addEventListener('drop', (event) => {
            event.preventDefault();
            const widgetId = event.dataTransfer.getData('text/plain');
            const draggableWidget = document.getElementById(widgetId);
            event.target.closest('.dashboard-widgets').appendChild(draggableWidget);
        });
    });

    loadDashboardLayout();
});

document.addEventListener('DOMContentLoaded', function () {
    const emailPerformanceChart = createPerformanceChart();
    const abTestSummaryChart = createABTestChart();

    function createPerformanceChart() {
        const ctx = document.getElementById('emailPerformanceChart').getContext('2d');
        return new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
                datasets: [{
                    label: 'Open Rates',
                    data: [25, 40, 55, 70],
                    borderColor: '#4CAF50',
                    fill: false
                }, {
                    label: 'Click Rates',
                    data: [10, 20, 30, 45],
                    borderColor: '#FFC107',
                    fill: false
                }]
            },
            options: {
                responsive: true,
                onClick: (event, elements) => {
                    if (elements.length > 0) {
                        const dataIndex = elements[0].index;
                        const label = emailPerformanceChart.data.labels[dataIndex];
                        loadDetailedView('performance', label);
                    }
                }
            }
        });
    }

    function createABTestChart() {
        const ctx = document.getElementById('abTestSummaryChart').getContext('2d');
        return new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Variant A', 'Variant B'],
                datasets: [{
                    label: 'Open Rates',
                    data: [45, 60],
                    backgroundColor: ['#42A5F5', '#FFA726']
                }]
            },
            options: {
                responsive: true,
                onClick: (event, elements) => {
                    if (elements.length > 0) {
                        const dataIndex = elements[0].index;
                        const label = abTestSummaryChart.data.labels[dataIndex];
                        loadDetailedView('ab_test', label);
                    }
                }
            }
        });
    }

    function loadDetailedView(type, label) {
        window.location.href = `/detailed_view?type=${type}&label=${encodeURIComponent(label)}`;
    }
});