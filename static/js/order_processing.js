function showProcessingMessage() {
    document.getElementById('processingMessage').classList.remove('hidden');
}

// Call this function when the form is submitted
document.querySelector('form').onsubmit = showProcessingMessage;