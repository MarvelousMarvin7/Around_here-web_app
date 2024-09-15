function goToStoreCreationPage() {
    // Redirect to store creation page with user ID
    window.location.href = '/create_store?user_id=USER_ID';
}

function openStoreModal() {
    document.getElementById('storeModal').classList.remove('hidden');
}

function closeStoreModal() {
    document.getElementById('storeModal').classList.add('hidden');
}

function goToProductCreationPage() {
    // Redirect to product creation page with the store ID
    window.location.href = '/create_product?store_id=STORE_ID';
}

function goToServiceCreationPage() {
    // Redirect to service creation page with the store ID
    window.location.href = '/create_service?store_id=STORE_ID';
}

function goToStorePage() {
    // Redirect to the store page of user
    window.location.href = '/store?store_id=STORE_ID';
}