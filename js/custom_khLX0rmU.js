/* Выбор географической зоны (#1) */

  $(function(){
  	// Map Box - https://studio.mapbox.com//
    mapboxgl.accessToken = 'pk.eyJ1Ijoic2VyZ2V5c2htaWR0IiwiYSI6ImNqbzN5N3BhbDEyYXMzd3FjNnJlOXJnemkifQ.s0dbtY5p54XeW9_10eUlvw';
    var map = new mapboxgl.Map({
      container: 'mapboxBackground',
      style: 'mapbox://styles/sergeyshmidt/cl7p3qtjd001c14lfleyhg2ov',
      zoom: 13,
      center: [4.899, 52.372]
    });
    $('.popupTrigger[data-popup-id="mapbox"]').on('click', function(){
      map.resize();
    });
  });


/* Сравнение доходности зон (#2) */
$(document).ready(function(){
  
  // Infinite slider
  if($(".js-custom-infinite-slider").length>0){
    $(".js-custom-infinite-slider").each(function(){
      var slider = $(this),
          images = slider.attr("data-images").split(","),
          steps = "step-0",
          maxSteps = parseInt(slider.attr("data-cards-to-show"));
      $.each(images,function(key,src){
        if(key<maxSteps){
          slider.find(".slides-holder").append('<img class="absolute rounded big-shadow '+steps+'" src="'+src+'" alt=""/>');
          steps+=" step-"+(key+1);
          slider.attr("data-current",key);
        }
      });
      slider.click(function(){
        var canBeUnlocked = false,
            canBeUnlockedTimer = 0,
            slider = $(this),
            holder = slider.find(".slides-holder"),
            speed = 400,
            maxSteps = parseInt(slider.attr("data-cards-to-show")),
            currentSlide = parseInt(slider.attr("data-current")),
            images = slider.attr("data-images").split(","),
            nextSlide = currentSlide+1;
        if(images[nextSlide]==undefined){
          nextSlide = 0;
        }
        var src = images[nextSlide];
        if(holder.hasClass('locked')===false){
          holder.addClass('locked'); // lock slides change till newly added image is loaded
          holder.append('<img class="absolute rounded big-shadow ready-to-show" src="'+src+'" alt=""/>');
          // Animate the images by adding/removing classes
          holder.find("img").each(function(){
            var _this = $(this);
            for(var i=maxSteps-1; i>=0; i--){
              if(_this.hasClass("step-"+maxSteps)){ _this.addClass("will-be-removed"); }
              if(_this.hasClass("step-"+i)){ _this.addClass("step-"+(i+1)); }
              if(_this.hasClass("ready-to-show")){
                var timeout = setTimeout(function(){
                  _this.addClass("step-0");
                  holder.find(".will-be-removed").remove();
                  clearTimeout(timeout);
                },speed);
              }
            }
          });
          // if the image was loaded succsessfully
          holder.find(".ready-to-show").on("load",function(){
            $(this).removeClass("ready-to-show");
            canBeUnlocked=true;
          });
          // if the image was not loaded
          holder.find(".ready-to-show").on("error",function(){
            canBeUnlocked=true;
            holder.find(".ready-to-show").remove();
          });
          // check if image is loaded and unlock slider's change
          var interval = setInterval(function(){
            if(canBeUnlocked && canBeUnlockedTimer>speed*2){
              holder.removeClass('locked');
              slider.attr("data-current",nextSlide);
              clearInterval(interval);            
            }
            canBeUnlockedTimer+=100;
          },100);
        }
      });
    });
  }
// Switch slider
  if($(".js-custom-switch-slider").length>0){
    $(".js-custom-switch-slider").click(function(){
      var holder = $(this).find(".holder");
      if(!holder.hasClass('locked')){
        holder.addClass('locked');
        var showNext = holder.attr("data-show-next"),
            zIndex = parseInt(holder.attr("data-z-index"))+1;
        holder.find("."+showNext+".invisible").css({"opacity":0,"z-index":zIndex}).animate({"opacity":1},500,function(){
          holder.find("."+showNext).each(function(){
            if($(this).hasClass("visible")){
              $(this).removeClass("visible").addClass("invisible");
            }else{
              $(this).removeClass("invisible").addClass("visible");
            }
          });
          holder.attr("data-show-next",((showNext=="on_back")?"on_front":"on_back"));
          holder.attr("data-z-index",zIndex);
          holder.removeClass('locked');
        });
      }
    });
  }
});