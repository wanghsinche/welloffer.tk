// $(function() {
//     $('a[href*=#]:not([href=#])').click(function() {
//         if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
//             var target = $(this.hash);
//             target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
//             if (target.length) {
//                 $('html,body').animate({
//                     scrollTop: target.offset().top
//                 }, 1000);
//                 return false;
//             }
//         }
//     });
// });

// $(function() {
//     //navbar affix
//     $('#nav').affix({
//         offset: {
//             top: $('header').height()
//         }
//     });
// });

// $('#nav .navbar-nav li>a').click(function() {
//     var link = $(this).attr('href');
//     var posi = $(link).offset().top + 20;
//     $('body,html').animate({
//         scrollTop: posi
//     }, 700);
// })


$(document).ready(function() {
    // $("[rel='tooltip']").tooltip();
    //a 标签锚点点击
    $(document).on('click','a',function(e){
      var href = e.currentTarget.getAttribute('href');
      var id, position;
      if(/^#(\w+)/.test(href)){
        e.preventDefault();
        e.stopPropagation();
        id = href.match(/^#(\w+)/)[1];
        position = document.getElementById(id).offsetTop - 20;
        $('html,body').animate({
            scrollTop: position
        }, 1000);

      }
    });

    $('#nav').affix({
        offset: {
            top: $('header').height()
        }
    });

    $('.thumbnail').hover(
        function() {
            $(this).find('.caption').fadeIn(250);
        },
        function() {
            $(this).find('.caption').fadeOut(205);
        }
    );
});