$(document).ready(function(){
    if(window.location.pathname.indexOf("/submitsong") != -1){
	$("#SuggestModal").modal();
	$(".Options").show();
    }else{
	if($(".Options").find('tr')[1]){
	    $(".Options tbody").remove();
	}
    }
    if($(".Options").find("tr")[1]){
	$("#SuggestModal").modal();
	$(".Options").show();
    }
    if(!($("#SuggestModal").hasClass('in'))){
	if($(".Options").is(":visible")){
	    if($(".Options").find('tr')[1]){
		window.location = "/";
	    }
	}
    }
    $(".Options").find('tr').click(function(){
	window.location = $(this).index();
    });
    $(".submit_form").find("submit").click(function(){
	$(".Options").show();
    });
    $("#addsong").click(function(){
	$("#SuggestModal").modal();
	$(".Options").hide();
	$(".submit_form").show();
    });
});
