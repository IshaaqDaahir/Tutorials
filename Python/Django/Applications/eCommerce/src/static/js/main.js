document.addEventListener('DOMContentLoaded', function() {
    // Example: Add interactivity to product cards
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('click', () => {
            alert('Product clicked!');
        });
    });
});
