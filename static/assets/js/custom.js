/*------------------------------------------------------------------
    Template Name:  Refix
    Version: 1.0
    Author: Layerdrops
    Author Email: layerdrops@gmail.com

    [Table of Content]

    01: Navbar Fixed
    02: PreLoader
    03: Responsive menu
    04: responsive toggle menu
    05: Book Online radio button
    06: Header Slider
    07: Home v2 Header Slider
    08: Custom Owl-carousel
    09: Clients Logo
    10: Service Slider
    11: Video Promotion



*/

(function ($) {
    "use strict";

    /*** =====================================
     * Navbar fixed
     * =====================================***/
    const menu_fixed = document.querySelector('.main_menu_area');
    const topOfNav = menu_fixed.offsetTop;

    function fixed_nav() {
        if (window.scrollY >= topOfNav || window.scrollY === topOfNav) {
            document.body.style.paddingTop = menu_fixed.offsetHeight + 'px';
            document.body.classList.add('fixed-scroll-nav');
        } else {
            document.body.style.paddingTop = 0;
            document.body.classList.remove('fixed-scroll-nav');
        }
    }
    window.addEventListener('scroll', fixed_nav);


    /*** =====================================
     * PreLoader
     * =====================================***/
    $(window).on('load', function () {
        $('.preloader').delay('500').fadeOut(2000);
    });


    $(document).on('ready', function () {

        /*** =====================================
         * Responsive menu
         * =====================================***/
        $(document).on('click','.main_menu_area .navbar-default .navbar-nav > li > span.responsive_click_menu:not(:only-child)', function(e) {
            $(this).siblings('.dropdown-menu').toggle();
            $('.dropdown-menu').not($(this).siblings()).hide();
            e.stopPropagation();
        });



        /*** =====================================
         * responsive toggle menu
         * =====================================***/
         $(document).on('click','.main_menu_area .header_nav .navbar-toggle', function() {
            $('.main_menu_area .responsive_menu').toggleClass('responsive_menu_show');
         });


        /*** =====================================
         * Fancybox
         * =====================================***/
        $(".fancybox").fancybox();


        /*** =====================================
         * CounterUP
         * =====================================***/
         $('.counter').counterUp({
             delay: 10,
             time: 4000
         });


        /*** =====================================
         * Book Online radio button
         * =====================================***/
         $(document).on('click', '.input_agree_title .check', function() {
            $('.input_agree_title .check').toggleClass('active_agree');
         });
         $(document).on('click', '.input_agree_title .check_2', function() {
            $('.input_agree_title .check_2').toggleClass('active_agree');
         });



        /*** =====================================
         * Header Slider
         * =====================================***/
        $('.header_slider_area').owlCarousel({
            items: 1,
            autoHeight: true,
            autoplay: true,
            loop: true,
            nav: false,
            dots: true,
            animateIn: 'fadeIn',
            animateOut: 'fadeOut',
        });

        /*** =====================================
         * Home v2 Header Slider
         * =====================================***/
        $('.hv2_slider_area').owlCarousel({
            items: 1,
            autoHeight: true,
            autoplay: true,
            loop: true,
            nav: true,
            navText: ["<i class='fa fa-angle-left' aria-hidden='true'></i>", "<i class='fa fa-angle-right' aria-hidden='true'></i>"],
            dots: false,
            animateIn: 'fadeIn',
            animateOut: 'fadeOut',
        });


        /*** =====================================
         * Custom Owl-carousel dots and testimonial
         * =====================================***/
        $(document).on('click','#custom_owl_carousel_dots > li', function(){
            $('#custom_owl_carousel_dots > li.active').removeClass('active');
            $(this).addClass('active');
        });


        let Owl = {
            init: function() {
              Owl.carousel();
            },
            carousel: function() {
                let owl;
                owl = $('.testimonial_slider').owlCarousel({
                    items      : 1,
                    dots       : true,
                    center     : true,
                    autoplay   : true,
                    addClassActive : true,
                    nav        : false,
                    loop       : true,
                    margin     : 10,
                    animateOut : 'slideOutDown',
                    animateIn : 'slideInDown'
                });

                $('#custom_owl_carousel_dots').on('click', 'li', function(e) {
                    owl.trigger('to.owl.carousel', [$(this).index(), 300]);
                });
            }
        };
        Owl.init();


        let testimonial_slider = $(".testimonial_slider");
        testimonial_slider.on('changed.owl.carousel', function (e) {
            if(e.relatedTarget.current()===2) {
                $('#custom_owl_carousel_dots > li.testimonial1').addClass('active');
            } else {
                $('#custom_owl_carousel_dots > li.testimonial1').removeClass('active');
            }
            if(e.relatedTarget.current()===3) {
                $('#custom_owl_carousel_dots > li.testimonial2').addClass('active');
            } else {
                $('#custom_owl_carousel_dots > li.testimonial2').removeClass('active');
            }
            if(e.relatedTarget.current()===4) {
                $('#custom_owl_carousel_dots > li.testimonial3').addClass('active');
            } else {
                $('#custom_owl_carousel_dots > li.testimonial3').removeClass('active');
            }
            if(e.relatedTarget.current()===5) {
                $('#custom_owl_carousel_dots > li.testimonial4').addClass('active');
            } else {
                $('#custom_owl_carousel_dots > li.testimonial4').removeClass('active');
            }
            if(e.relatedTarget.current()===6) {
                $('#custom_owl_carousel_dots > li.testimonial5').addClass('active');
            } else {
                $('#custom_owl_carousel_dots > li.testimonial5').removeClass('active');
            }
            if(e.relatedTarget.current()===7) {
                $('#custom_owl_carousel_dots > li.testimonial6').addClass('active');
            } else {
                $('#custom_owl_carousel_dots > li.testimonial6').removeClass('active');
            }
        });


        /*** =====================================
         * Clients Logo
         * =====================================***/
        $('.client_logo_slider').owlCarousel({
            items: 4,
            autoHeight: true,
            autoplay: true,
            loop: true,
            nav: false,
            dots: true,
            margin: 20,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                1000: {
                    items: 4
                }
            }
        });


        /*** =====================================
         * Service Slider
         * =====================================***/
        $('.service_slider').owlCarousel({
            autoHeight: true,
            autoplay: true,
            loop: true,
            nav: false,
            dots: true,
            margin: 30,
            responsive: {
                0: {
                    items: 1,
                },
                600: {
                    items: 2,
                },
                1000: {
                    items: 4,
                },
            }
        });


        /*** =====================================
         * Video Promotion
         * =====================================***/
        $("#videolink").magnificPopup({
            type: 'inline',
            midClick: true
        });
        $("#videolink2").magnificPopup({
            type: 'inline',
            midClick: true
        });


    });

})(jQuery);