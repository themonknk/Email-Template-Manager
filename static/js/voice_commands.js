document.addEventListener('DOMContentLoaded', function () {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    document.getElementById('voiceCommandBtn').addEventListener('click', () => {
        recognition.start();
    });

    recognition.onresult = (event) => {
        const command = event.results[0][0].transcript.toLowerCase();
        processVoiceCommand(command);
    };

    function processVoiceCommand(command) {
        if (command.includes('open dashboard')) {
            window.location.href = '/dashboard';
        } else if (command.includes('generate report')) {
            window.location.href = '/generate_report';
        } else {
            alert(`Command not recognized: ${command}`);
        }
    }
});