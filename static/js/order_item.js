function updateTotalAmount() {
    const quantity = document.getElementById('quantity').value;
    const unitPrice = document.getElementById('unit_price').value;

    if (quantity && unitPrice) {
        const totalAmount = (quantity * unitPrice).toFixed(2);
        document.getElementById('total_amount').value = totalAmount;
    }
}

// Event listener for quantity input
document.getElementById('quantity').addEventListener('input', function() {
    const productId = document.getElementById('product_id').value;

    // AJAX request to fetch unit price from backend
    fetch(`/get_unit_price?product_id=${productId}`)
        .then(response => response.json())
        .then(data => {
            // Set unit price in the form
            document.getElementById('unit_price').value = data.unit_price;

            // Update total amount
            updateTotalAmount();
        })
        .catch(error => console.error('Error fetching unit price:', error));
});