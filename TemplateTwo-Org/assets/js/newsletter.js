// Newsletter form submission logic

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('newsletterForm');
    const emailInput = document.getElementById('newsletterEmail');
    const successMsg = document.getElementById('newsletterSuccess');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        // Optionally: validate email here
        form.style.display = 'none';
        successMsg.style.display = 'block';
    });
});
