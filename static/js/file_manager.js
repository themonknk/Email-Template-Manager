document.addEventListener('DOMContentLoaded', function () {
    const fileUploadForm = document.getElementById('file-upload-form');
    const uploadStatus = document.getElementById('uploadStatus');
    const uploadedFilesDiv = document.getElementById('uploadedFiles');

    fileUploadForm.onsubmit = async function (event) {
        event.preventDefault();
        const fileInput = document.getElementById('fileInput');
        const file = fileInput.files[0];

        if (!file) {
            uploadStatus.innerHTML = '<div class="alert alert-warning">Please select a file to upload.</div>';
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('/api/upload_file', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();
        if (response.ok) {
            uploadStatus.innerHTML = `<div class="alert alert-success">${result.message}</div>`;
            loadUploadedFiles();
        } else {
            uploadStatus.innerHTML = `<div class="alert alert-danger">${result.error}</div>`;
        }
    };

    async function loadUploadedFiles() {
        const response = await fetch('/api/list_files');
        const files = await response.json();
        uploadedFilesDiv.innerHTML = files.map(file => `<p><a href="/static/uploads/${file}">${file}</a></p>`).join('');
    }

    loadUploadedFiles();
});