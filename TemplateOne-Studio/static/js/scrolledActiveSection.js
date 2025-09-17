document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.section');

    const checkVisibility = () => {
        sections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;

            if (sectionTop < windowHeight * 0.5) {
                section.classList.add('animated');
            }
        });
    };

    window.addEventListener('scroll', checkVisibility);
    checkVisibility(); 
});