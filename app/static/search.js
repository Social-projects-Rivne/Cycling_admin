$(document).ready(function(){
	$("button").click(function(){
			$.ajax({
  			type: "POST",
  			url: "/users/search",
  			data: $("form").serialize(),
  			success: function(response){
  				console.log(response);
  			},
  			dataType: "application/json"
		});
	});
});