$(document).ready(function(){
	$("#contact-form").validationEngine();

	$('#contact-form .submit-btn').click( function() {
		if ($("#contact-form").validationEngine('validate')) {
			$.ajax({
			  url: $('#contact-form').attr('action'),
			  method: "get",
			  data: $('#contact-form').serialize(),
			  success: function(data) {
				$(this).hide();
			  }
			});
		return false;
		}
	});

});