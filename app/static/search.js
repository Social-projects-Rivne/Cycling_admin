$(document).ready(function(){
	$(".icon").on("click", function(){
		$(".navmenu").toggleClass("closed");
		$("#content").toggleClass("closed");
	});
});