window.generateReport = function () {
    const includeScatterPlot = document.getElementById('includeScatterPlot').checked;
    const includeHeatMap = document.getElementById('includeHeatMap').checked;
    const colorScheme = document.getElementById('colorScheme').value;
    const companyLogo = document.getElementById('companyLogo').files[0];

    const formData = new FormData();
    formData.append('includeScatterPlot', includeScatterPlot);
    formData.append('includeHeatMap', includeHeatMap);
    formData.append('colorScheme', colorScheme);
    formData.append('companyLogo', companyLogo);

    fetch('/api/generate_report', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('reportStatus').innerHTML = `<p>Report generated successfully: <a href="${data.reportUrl}" target="_blank">Download Report</a></p>`;
    })
    .catch(() => {
        document.getElementById('reportStatus').innerHTML = `<p>Error generating report. Please try again.</p>`;
    });
};