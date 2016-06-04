$(document).ready(function(){
    $("#Options").find('tr').click(function(){
	console.log("row :"+($(this).index()));
    });
    $(".submit_form").hide();
    $("#addsong").click(function(){
	$(".submit_form").show();
	$("#addsong").hide();
    });
    if($("#SuggestModal").find("tr")[1]){
	$("#SuggestModal").modal();
    }
});    
