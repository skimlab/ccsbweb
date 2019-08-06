// Initialise FlexSlider for Carousels
$(window).load(function() {
    $('.flexslider').flexslider({
    	animation: "slide",
    	start: function(slider){
          $('body').removeClass('loading');
        },
        prevText: '<span class="flex-custom-nav-button--left"></i>',
        nextText: '<span class="flex-custom-nav-button---right"></i>',
    	directionNav: true,
    	slideshowSpeed: 5000,
    	animationSpeed: 600,
		smoothHeight: true,
    	touch: true
    });
});
