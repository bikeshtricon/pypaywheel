$('.leaveActiont').on('click',function(){
	
	link=$(this);
	$.getJSON("/hr/leaveRequest", { id:link.attr('data-id'), action:link.text() }, function(json){
	    
		if (json['success']== true) {
			alert("Leave "+link.text()+"ed successfully");
			link.closest( "tr" ).remove()
		}
		else {
			
			alert("Error while updating leave ");
		}
	});
	
	return;
});