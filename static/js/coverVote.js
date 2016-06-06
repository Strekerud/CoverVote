$(document).ready(function(){
    $(".Options").find('tr').click(function(){
	window.location = $(this).index();
    });
    $("#addsong").click(function(){
	$(".Options").hide();
	$("#SuggestModal").modal();
	$(".submit_form").show();
	$("#addsong").hide();
    });
    if($(".Options").find("tr")[1]){
	$(".Options").show();
	$("#SuggestModal").modal();
    }
});    
