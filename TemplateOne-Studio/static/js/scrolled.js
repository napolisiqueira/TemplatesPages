const navbar = document.getElementById('nav');

if (navbar) {
    console.log("navbar encontrada")
}

window.addEventListener('scroll', () => {
    if (navbar) {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }
});