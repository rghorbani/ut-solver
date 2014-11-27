// #######################
// ### App's Common JS ###
// #######################
var App = function () {

	var manageScroll = function() {
		$(window).bind('scroll', function() {
			if ($(window).scrollTop() > 200) {
				$('nav.navbar').addClass('navbar-fixed-top');
				$('#scroll-up').show();
			} else {
				$('nav.navbar').removeClass('navbar-fixed-top');
				$('#scroll-up').hide();
			}
		});
	}

	var toTheTop = function() {
		$('body').on('click', '#scroll-up', function (e) {

			e.preventDefault();

			$("html").animate({scrollTop:$('#top').offset().top}, 800);
		});
	}
	
	return {
		// Initializing Main Functions
		init: function() {

			manageScroll();
			toTheTop();
			
		},
	};
}();

jQuery(document).ready(function() {
	App.init();
});