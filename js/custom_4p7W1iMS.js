document.addEventListener('DOMContentLoaded', function() {
  // Initialize all Swiper instances
  const swiperInstances = document.querySelectorAll('.swiper-99');

  swiperInstances.forEach(function(swiperContainer) {
    // Add navigation arrows
    const prevButton = document.createElement('div');
    prevButton.className = 'swiper-button-prev';

    const nextButton = document.createElement('div');
    nextButton.className = 'swiper-button-next';

    swiperContainer.appendChild(prevButton);
    swiperContainer.appendChild(nextButton);

    // Initialize Swiper
    new Swiper(swiperContainer, {
      slidesPerView: 3,
      spaceBetween: 30,
      loop: true,
      navigation: {
        nextEl: nextButton,
        prevEl: prevButton,
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
          spaceBetween: 10
        },
        768: {
          slidesPerView: 2,
          spaceBetween: 20
        },
        1024: {
          slidesPerView: 3,
          spaceBetween: 30
        }
      }
    });
  });
});
