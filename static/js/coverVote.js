$(document).ready(function(){
    $(".Options").find('tr').click(function(){
	window.location = $(this).index();
    });
    if(!($("#SuggestModal").hasClass('in'))){
	if($(".Options").find("tr")[1]){
	    window.location = "/discard";
	}
    }
    $("#addsong").click(function(){
	$("#SuggestModal").modal();
	$(".Options").hide();
	$(".submit_form").show();
    });
    if($(".Options").find("tr")[1]){
	$(".Options").show();
	$("#SuggestModal").modal();
    }
    
});    
