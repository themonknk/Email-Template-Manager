document.addEventListener('DOMContentLoaded', function () {
    const annotationInput = document.getElementById('sharedAnnotationInput');
    const realTimeUpdates = document.getElementById('realTimeUpdates');

    // Simulate real-time updates using WebSocket (or similar technology)
    const socket = new WebSocket('ws://localhost:5000/collaborative-editing');

    socket.onmessage = function (event) {
        const data = JSON.parse(event.data);
        realTimeUpdates.innerHTML += `<p>${data.user}: ${data.message}</p>`;
    };

    window.saveAnnotation = function () {
        const annotation = annotationInput.value;
        socket.send(JSON.stringify({ user: 'User1', message: annotation }));
        annotationInput.value = '';
    };
});