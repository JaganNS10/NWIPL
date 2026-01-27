
  (function ($) {
  
  "use strict";

    // HERO SLIDE
    // $('.hero-slide').backstretch([
    //   STATIC_URL + "images/slideshow/wooden-furniture-1.jpg", 
    //   STATIC_URL + "images/slideshow/complement-light-oak-with-mid-century-furniture.jpg",
    //   STATIC_URL + "images/slideshow/featured-compressed-46.jpg",
    //   STATIC_URL + "images/ToddlerBabyCots.jpg",
    //   STATIC_URL + "images/NewBornbabycot.jpg",
    //   STATIC_URL + "images/Babycot.jpg",
    // ],  {duration: 2000, fade: 750});
    $('.hero-slide').backstretch([
        STATIC_URL + "images/NeminathLogo.jpeg",
        STATIC_URL + "images/slideshow/wooden-furniture-1.jpg",
        STATIC_URL + "images/slideshow/complement-light-oak-with-mid-century-furniture.jpg",
        STATIC_URL + "images/slideshow/featured-compressed-46.jpg",
        STATIC_URL + "images/Image1.avif",
        STATIC_URL + "images/Image2.avif",
        STATIC_URL + "images/Babycot.jpg",
        STATIC_URL + "images/Image3.jfif"

    ], {
        duration: 2000,
        fade: 750
    });


    // REVIEWS CAROUSEL
    $('.reviews-carousel').owlCarousel({
    items:3,
    loop:true,
    dots: false,
    nav: true,
    autoplay: true,
    margin:30,
      responsive:{
        0:{
          items:1
        },
        600:{
          items:2
        },
        1000:{
          items:3
        }
      }
    })

    // CUSTOM LINK
    $('.smoothscroll').click(function(){
    var el = $(this).attr('href');
    var elWrapped = $(el);
    var header_height = $('.navbar').height();

    scrollToDiv(elWrapped,header_height);
    return false;

    function scrollToDiv(element,navheight){
      var offset = element.offset();
      var offsetTop = offset.top;
      var totalScroll = offsetTop-navheight;

      $('body,html').animate({
      scrollTop: totalScroll
      }, 300);
    }
});
    
  })(window.jQuery);


