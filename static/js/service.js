function showServiceRequestModal() {
    document.getElementById('serviceModal').classList.remove('hidden');
}

function closeServiceRequestModal() {
    document.getElementById('serviceModal').classList.add('hidden');
}

function redirectToServiceRequest() {
    const userId = 'USER_ID';
    const serviceId = 'SERVICE_ID';
    window.location.href = `/service_request?user_id=${userId}&service_id=${serviceId}`;
}
