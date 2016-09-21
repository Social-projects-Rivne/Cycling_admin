$(document).ready(function(){
	$("button").click(function(){
			$.ajax({
  			type: "POST",
  			url: "../controllers/user_controller.py",
  			data: $("#search-form").serializeArray(),
  			success: function(result){
  				console.log(result);
  			}
  			//dataType: dataType
		});
	});
});