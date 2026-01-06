/**
 * @file init.js
 * @description Frontend initialization script for Materialize CSS components 
 * and interactive DOM elements.
 *
 * @author Amey Thakur <https://github.com/Amey-Thakur>
 * @author Mega Satish <https://github.com/msatmod>
 * @created 2022-08-09
 * @repository https://github.com/Amey-Thakur/TEXT-SUMMARIZER
 * @license MIT
 */

(function ($) {
  $(function () {

    $('.sidenav').sidenav();
    $('.parallax').parallax();
    // TABS INIT
    $('.tabs').tabs();
    // CAROUSEL INIT
    $('.carousel.carousel-slider').carousel({ fullWidth: true });
    // SLIDER INIT
    $('.slider').slider({
      indicators: false,
      // we don't want the little dots to show
      height: 500,
      transition: 500,
      interval: 6000
      // how long the slide stays for
    });


  }); // end of document ready
})(jQuery); // end of jQuery name space


