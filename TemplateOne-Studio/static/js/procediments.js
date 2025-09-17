const next = document.querySelector('#next');
const prev = document.querySelector('#prev');
const cards = document.querySelector('.card-content');

// Calcule a largura do primeiro grupo de cartões para saber quando voltar
const firstSectionWidth = cards.scrollWidth / 2; // se você duplicou o conteúdo uma vez

function handleScrollNext() {
  const scrollAmount = window.innerWidth / 2 > 600 ? window.innerWidth / 2 : window.innerWidth - 100;
  cards.scrollLeft += scrollAmount;
}

function handleScrollPrev() {
  const scrollAmount = window.innerWidth / 2 > 600 ? window.innerWidth / 2 : window.innerWidth - 100;
  cards.scrollLeft = Math.max(0, cards.scrollLeft - scrollAmount);
}

// Adicione um evento de rolagem para o efeito infinito
cards.addEventListener('scroll', () => {
    // Se a rolagem for maior que a largura do primeiro conjunto de cards...
    if (cards.scrollLeft >= firstSectionWidth) {
        // ...pule para o início do primeiro conjunto
        cards.scrollLeft = cards.scrollLeft - firstSectionWidth;
    }
    // Se a rolagem for menor que a largura do primeiro conjunto de cards...
    else if (cards.scrollLeft <= 0) {
        // ...pule para o final da lista (o início do conjunto duplicado)
        cards.scrollLeft = firstSectionWidth;
    }
});

if (next && prev) {
  next.addEventListener('click', handleScrollNext);
  prev.addEventListener('click', handleScrollPrev);
}