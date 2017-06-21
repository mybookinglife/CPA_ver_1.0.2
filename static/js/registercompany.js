$('document').ready(function(){
	
	var dialog, form,
	
	
    dialog = $("#dialog-form").dialog({
        autoOpen: false,
        width: 370,
        modal: true,
        buttons: {
          "Register": function(){
        	  register_company();  
    	      dialog.dialog( "close" );

          },
          Cancel: function() {
            dialog.dialog("close");
          }
        },
       });
    
	$('#registercompany').on('click', function(){
	    dialog.dialog( "open" );
	});		
});

function register_company(_form){
	
	var frm = $('#registercompany_form');
	
	$.ajax({
		url : "/user/add_company/", // the endpoint
		type : "POST", // http method
		data : frm.serialize(), // data sent with the delete request

		success : function(json) {
			// hide the post
			if (json.result == 'true'){ 
				console.log("Добавили компанию");  				
			} else {
				alert(json.msg);
			}
		},

		error : function(xhr, errmsg, err) {
			// Show an error
			console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		}
	});

}
