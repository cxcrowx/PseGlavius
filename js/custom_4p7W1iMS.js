/* Обзор маркетплейса (#1) */

$(function(){
  var slideKey = 134;
  if(!window.swipers){window.swipers = {};}
  if(!window.swipers[slideKey]){window.swipers[slideKey] = [];}
  $('.swiper-'+slideKey).each(function(){
    var thisKey = window.swipers[slideKey].length;
    window.swipers[slideKey][thisKey] = 
      new Swiper(this, {
      slidesPerView: 'auto',  
      spaceBetween: 40,
      centeredSlides: true,
      breakpoints: {
        435: {
          centeredSlides: false,    
          slidesPerView: 2, 
        },
        767: {
          centeredSlides: false, 
          slidesPerView: 3,   
        },
        991: {
          centeredSlides: false, 
          slidesPerView: 4,   
        },              
      }
    });
  });
});

/* Аккумуляторы (#2) */

$(function(){
  var slideKey = 99;
  if(!window.swipers){window.swipers = {};}
  if(!window.swipers[slideKey]){window.swipers[slideKey] = [];}
  $('.swiper-'+slideKey).each(function(){
    var thisKey = window.swipers[slideKey].length;
    window.swipers[slideKey][thisKey] = 
      new Swiper(this, {
      slidesPerView: 1,
      spaceBetween: 20,
      pagination: {
        el: this.querySelector('.swiper-pagination'),
        clickable: true,
      },
      autoplay: {
        delay: 3000,
        disableOnInteraction: true,
      },
      breakpoints: {
        436: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        1024: {
          slidesPerView: 4,
        },
      }
    });
  });
});