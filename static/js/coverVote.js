$(document).ready(function(){
    $(".Options").find('tr').click(function(){
	window.location = $(this).index();
    });
    if(!($("#SuggestModal").hasClass('in'))){
	if($(".Options").is(":visible")){
	    if($(".Options").find('tr')[1]){
		$(".Options tbody").remove();
		window.location = "/discard";
	    }
	}
    }
    $("#addsong").click(function(){
	$("#SuggestModal").modal();
	$(".Options").hide();
	$(".submit_form").show();
    });
    if($(".Options").find("tr")[1]){
	$("#SuggestModal").modal();
	$(".Options").show();
    }
    
});    
