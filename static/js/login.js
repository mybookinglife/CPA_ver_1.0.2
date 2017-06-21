$('document').ready(function(){
	
	var dialog, form
	
    dialog = $("#dialog-form").dialog({
        autoOpen: false,
        width: 350,
        modal: true,
        buttons: {
          "Sing in": function(){
        	  answer = login();  
        	  if (answer == true) {  
    	      	dialog.dialog( "close" );
    	      	location.reload();
    	      	}
        	  else {
        		  alert("Your username and password didn't match. Please try again.");
        	  };

          },
          Cancel: function() {
            dialog.dialog("close");
          }
        },
       });
	
	$('#login').on('click', function(){
		dialog.dialog( "open" );
	});	
	
	
});	
    
$('document').ready(function(){
    // recovery password
	var dialog_recovery, form
	
    dialog_recovery = $("#dialog-form").dialog({
        autoOpen: false,
        width: 350,
        modal: true,
        buttons: {
          "Send e-mail": function(){
        	  recovery_password();  
    	      dialog_recovery.dialog( "close" );

          },
          Cancel: function() {
            dialog_recovery.dialog("close");
          }
        },
       });
    

	$('#recovery').on('click', function(){
		dialog_recovery.dialog( "close" );
	    dialog_recovery.dialog( "open" );
	});	
});

function recovery_password(_form){
	
	var frm = $('#recovery_form');
	
	$.ajax({
		url : "user/password_reset/", // the endpoint
		type : "POST", // http method
		data : frm.serialize(), // data sent with the delete request

		success : function() {
			document.location.href = '/';
		},

		error : function(xhr, errmsg, err) {
			// Show an error
			console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		}
	});

	
  
}

function login(_form){
	
	var frm = $('#login_form'); 
	var localanswer, stranswer;
	
	localanswer =  false;
	
	$.ajax({
		url : "user/login/", // the endpoint
		type : "POST", // http method
		async: false,
		data : frm.serialize(), // data sent with the delete request

		success : function(json) {
				localanswer = json.result;
		},

		error : function(xhr, errmsg, err) {
			// Show an error
			console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		}
	});

	return localanswer;
}
