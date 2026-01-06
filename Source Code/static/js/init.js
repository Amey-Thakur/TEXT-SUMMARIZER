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

    // Initialize Materialize Side Navigation (Mobile/Responsive)
    $('.sidenav').sidenav();

    // Initialize Parallax Effect for immersive conceptual visuals
    $('.parallax').parallax();

    // Initialize Tab Navigation Components
    $('.tabs').tabs();

    // Initialize Carousel for Feature Showcase
    $('.carousel.carousel-slider').carousel({ fullWidth: true });

    // Initialize Hero Slider with Custom Timing
    $('.slider').slider({
      indicators: false,
      // Suppress navigation dots for cleaner aesthetic
      height: 500,        // Fixed height in pixels
      transition: 500,    // Transition duration in ms
      interval: 6000      // Slide duration in ms
      // Controlled timing for optimal readability
    });


  }); // End of document ready state
})(jQuery); // End of jQuery namespace encapsulation


