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

// ----------------------------------------------------------------------------
// Security & Anti-Inspection Protocols
// ----------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', () => {
  const securityOverlay = document.getElementById('securityOverlay');
  const dismissBtn = document.getElementById('dismissSecurity');

  // Disable Right Click
  document.addEventListener('contextmenu', (e) => {
    e.preventDefault();
    showSecurityAlert();
  });

  // Disable Keyboard Shortcuts for Inspection
  document.addEventListener('keydown', (e) => {
    // F12
    if (e.key === 'F12') {
      e.preventDefault();
      showSecurityAlert();
    }
    // Ctrl+Shift+I/J/C (DevTools)
    if (e.ctrlKey && e.shiftKey && ['I', 'J', 'C'].includes(e.key.toUpperCase())) {
      e.preventDefault();
      showSecurityAlert();
    }
    // Ctrl+U (View Source)
    if (e.ctrlKey && e.key.toUpperCase() === 'U') {
      e.preventDefault();
      showSecurityAlert();
    }
  });

  // Show Security Overlay
  function showSecurityAlert() {
    if (securityOverlay) {
      securityOverlay.style.display = 'flex';
      // Add pulse animation to icon
      const icon = securityOverlay.querySelector('div');
      if (icon) icon.classList.add('security-icon');
    }
  }

  // Dismiss Security Overlay
  if (dismissBtn) {
    dismissBtn.addEventListener('click', () => {
      securityOverlay.style.display = 'none';
      // Remove animation to reset
      const icon = securityOverlay.querySelector('div');
      if (icon) icon.classList.remove('security-icon');
    });
  }

  // Console Easter Egg (Self-XSS Warning)
  console.log("%cStop!", "color: red; font-size: 50px; font-weight: bold; text-shadow: 2px 2px 0px black;");
  console.log("%cThis is a browser feature intended for developers. If someone told you to copy-paste something here to enable a feature or 'hack' someone's account, it is a scam and will give them access to your account.", "color: white; font-size: 18px; font-weight: bold;");
  console.log("%cSee https://en.wikipedia.org/wiki/Self-XSS for more information.", "color: cyan; font-size: 16px; font-weight: bold; text-decoration: underline;");
});


