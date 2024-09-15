function showPendingMessage() {
    document.getElementById('pendingMessage').classList.remove('hidden');
}

// Call this function when the form is submitted
document.querySelector('form').onsubmit = showPendingMessage;