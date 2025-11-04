/**
 * Navigation Menu Functionality
 * Handles mobile menu toggle and navigation
 */

const mobileToggle = document.querySelector('.navbar__toggle');
const mobileMenu = document.querySelector('.navbar__menu');

mobileToggle.addEventListener('click', () => {
    mobileToggle.classList.toggle('active');
    mobileMenu.classList.toggle('active');
});