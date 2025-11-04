// Counter animation for program stats
document.addEventListener('DOMContentLoaded', () => {
    // Counter animation function
    const animateCounter = (element, target) => {
        let current = 0;
        const increment = target / 50; // Divide animation into 50 steps
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            element.textContent = Math.floor(current).toLocaleString('pt-BR');
        }, 30);
    };

    // Observer for counter animation
    const observerCallback = (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                const target = parseInt(element.dataset.count);
                animateCounter(element, target);
                observer.unobserve(element);
            }
        });
    };

    const observer = new IntersectionObserver(observerCallback, {
        threshold: 0.5
    });

    // Observe all program numbers
    document.querySelectorAll('.program__number').forEach(element => {
        observer.observe(element);
    });

    // Event Calendar
    const events = [
        {
            date: '12 Nov 2025',
            title: 'Feira de Adoção',
            location: 'Parque Villa-Lobos'
        },
        {
            date: '15 Nov 2025',
            title: 'Campanha de Castração',
            location: 'Vila Real'
        },
        {
            date: '20 Nov 2025',
            title: 'Visita à Escola Municipal',
            location: 'E.M. Paulo Freire'
        },
        {
            date: '25 Nov 2025',
            title: 'Terapia Assistida',
            location: 'Hospital Santa Casa'
        },
        {
            date: '30 Nov 2025',
            title: 'Treinamento de Voluntários',
            location: 'Sede do Instituto'
        },
        {
            date: '05 Dez 2025',
            title: 'Bazar Beneficente',
            location: 'Centro Comunitário'
        }
    ];

    // Populate calendar grid
    const calendarGrid = document.getElementById('eventCalendar');
    events.forEach(event => {
        const eventCard = document.createElement('div');
        eventCard.className = 'event-card';
        eventCard.innerHTML = `
            <div class="event-card__date">${event.date}</div>
            <h3 class="event-card__title">${event.title}</h3>
            <div class="event-card__location">📍 ${event.location}</div>
        `;
        calendarGrid.appendChild(eventCard);
    });
});