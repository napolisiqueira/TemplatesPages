var swiper = new Swiper(".mySwiper", {
slidesPerView: 3, // Mostra 3 slides por vez
spaceBetween: 30, // Espaçamento entre os slides
loop: true, // Repete o carrossel
pagination: {
    el: ".swiper-pagination", // Conecta a paginação
    clickable: true,
},
navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
},
});