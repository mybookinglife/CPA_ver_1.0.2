$('document').ready(function(){
	
	var dialog, form
	
    dialog = $("#dialog-form").dialog({
        autoOpen: false,
        width: 350,
        modal: true,
        buttons: {
          "Send e-mail": function(){
        	  login_change();
        	  dialog.dialog("close");
  	      	  location.reload();
          },
          Cancel: function() {
            dialog.dialog("close");
          }
        },
       });
	
	$('#login_change').on('click', function(){
		dialog.dialog( "open" );
	});	
	
	
});	

function login_change(_form){
	
	var frm = $('#login_change_form');  
	
	$.ajax({
		url : "login_change/", // the endpoint
		type : "POST", // http method
		async: false,
		data : frm.serialize(), // data sent with the delete request
		
		success : function(json) {
			// hide the post
			
			if (json.result == 'true'){   
				//console.log("Отправлена ссылка на e-mail")
				$('#dialog-form').dialog( "close" );
				alert(json.msg);
			} else {
				alert(json.msg);
			}
		},

		error : function(xhr, errmsg, err) {
			// Show an error
			console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		}
	});

	return localanswer;
}
