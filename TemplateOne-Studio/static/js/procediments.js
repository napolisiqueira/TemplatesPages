$(document).ready(function(){
    $('#autoWidth').lightSlider({
        item: 3, 
        autoWidth: false,
        slideMove: 1,
        slideMargin: 3, 
        loop: true,
        controls: true,
        pager: false,
        onSliderLoad: function(){
        $('#autoWidth').removeClass('cS-hidden');
    },
        // Adicionando eventos de clique para navegação manual
        onAfterSlide: function (el) {
            $('.prev').click(function() {
                el.goToPrevSlide();
            });
            $('.next').click(function() {
                el.goToNextSlide();
            });
        }
    });
});