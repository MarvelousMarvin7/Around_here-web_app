function showOrderModal() {
    document.getElementById('orderModal').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('orderModal').classList.add('hidden');
}

function redirectToOrder() {
    const userId = 'USER_ID';
    const productId = 'PRODUCT_ID';
    window.location.href = `/order?user_id=${userId}&product_id=${productId}`;
}
