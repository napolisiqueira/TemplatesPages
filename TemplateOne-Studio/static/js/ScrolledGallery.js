document.addEventListener('DOMContentLoaded', () => {
    // Seleciona todos os elementos que precisam ser animados.
    // Usamos .title-galery e .grid-galery.
    const elementsToAnimate = document.querySelectorAll('.title-galery, .grid-galery');

    const checkVisibility = () => {
        const windowHeight = window.innerHeight;
        
        elementsToAnimate.forEach(element => {
            // Pega a posição do elemento em relação à janela de visualização
            const elementTop = element.getBoundingClientRect().top;
            
            // Dispara a animação quando o topo do elemento estiver acima da metade da tela (50%)
            if (elementTop < windowHeight * 0.9) {
                element.classList.add('animated');
            }
        });
    };

    // Chama a função quando a página carrega e quando o usuário rola
    window.addEventListener('scroll', checkVisibility);
    checkVisibility(); // Garante que elementos já visíveis sejam animados no carregamento
});