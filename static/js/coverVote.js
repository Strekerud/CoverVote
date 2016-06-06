$(document).ready(function(){
    $(".Options").find('tr').click(function(){
	window.location = $(this).index();
    });
    if(!($("#SuggestModal").hasClass('in'))){
	window.location = "/discard";
    }
    $("#addsong").click(function(){
	$(".Options").hide();
	$("#SuggestModal").modal();
	$(".submit_form").show();
    });
    if($(".Options").find("tr")[1]){
	$(".Options").show();
	$("#SuggestModal").modal();
    }
    
});    
