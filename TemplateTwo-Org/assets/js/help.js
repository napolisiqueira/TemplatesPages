// Counter animation for impact metrics
document.addEventListener('DOMContentLoaded', () => {
    const animateCounter = (element, target, prefix = '') => {
        let current = 0;
        const increment = target / 50; // Divide animation into 50 steps
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = `${prefix}${Math.floor(current).toLocaleString('pt-BR')}`;
        }, 30);
    };

    const observerCallback = (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                const target = parseInt(element.dataset.count);
                const prefix = element.dataset.prefix || '';
                animateCounter(element, target, prefix);
                observer.unobserve(element); // Only animate once
            }
        });
    };

    const observer = new IntersectionObserver(observerCallback, {
        threshold: 0.5
    });

    // Observe all metric numbers
    document.querySelectorAll('.impact__number').forEach(element => {
        observer.observe(element);
    });
});