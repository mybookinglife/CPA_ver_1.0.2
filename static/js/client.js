$('document').ready(function(){
	
	$('body').on('click', '.delete_client', function(){
		var client_primary_key = $(this).attr('id').split('-')[2];
	    delete_client(client_primary_key);
	});	
	
});


$('document').ready(function(){
	
	var dialog_newclient, form,
	
    dialog_newclient = $("#dialog-form").dialog({
        autoOpen: false,
        height: 350,
        width: 350,
        modal: true,
        buttons: {
          "Create": function(){
        	  add_client();  
        	  dialog_newclient.dialog( "close" );

          },
          Cancel: function() {
        	  dialog_newclient.dialog("close");
          }
        },
       });
	
	$('.new_client').on('click', function(){
		dialog_newclient.dialog( "open" );
	});		


});

$('document').ready(function(){
	
	var dialog_editclient, form, client_primary_key
	
	dialog_editclient = $("#dialog-form").dialog({
        autoOpen: false,
        height: 700,
        width: 450,
        modal: true,
        buttons: {
          "Save": function(){
        	  edit_client(client_primary_key);  
        	  dialog_editclient.dialog( "close" );

          },
          Cancel: function() {
        	  dialog_editclient.dialog("close");
          }
        },
       });
	
	$('body').on('click', '.edit_client', function(){
		client_primary_key = $(this).parent().attr('id').split('-')[1];
	    get_client(client_primary_key); 
	    dialog_editclient.dialog( "open" );
	});		
	
});


$('document').ready(function(){
	var filter_client;
	
	$('.submit_filter').on('click', function(){
		filter_client = $("#filter_client :selected").val();
		get_list_clients(filter_client);
	});		
	
});

function delete_client(client_primary_key){
	
	
	if (confirm('are you sure you want to remove this client?')==true){
    	$.ajax({
            url : "delete_client/"+client_primary_key+"/", // the endpoint
            type : "POST", // http method
            data : { client_pk : client_primary_key }, // data sent with the delete request
            
            success : function(json) {
                // hide the post
            	if (json.result == 'true'){
            		$('#client-'+client_primary_key).remove(); // hide the post on success
            	} else{
            		alert(json.msg);	
            		}
            	
            },

            error : function(xhr,errmsg,err) {
                // Show an error
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    } else {
        return false;
    }
};

function add_client(){
	
	var frm = $('#form_new_client');
	
	$.ajax({
		url : "add_client/", // the endpoint
		type : "POST", // http method
		data : frm.serialize(), // data sent with the delete request

		success : function(json) {
			// hide the post
			
			if (json.result == 'true'){   
			
				$('#list_clients').append('<li id="client-'+json.id+'"><a class="edit_client">'+json.name+'</a><input class="delete_client" type="button" name="submit" id="delete-client-'+json.id+'" value="Delete"></li>'); // hide the post on success
				//console.log("Добавили услугу");
			} else {
				alert(json.msg);
			}
		},

		error : function(xhr, errmsg, err) {
			// Show an error
			console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		}
	});

	
	
  
};

function get_client(client_primary_key){
	
	$.ajax({
            url : "get_info_client/"+client_primary_key+"/", // the endpoint
            type : "POST", // http method
            data : { client_pk : client_primary_key }, // data sent with the delete request
            
            success : function(json) {
            
            	 $(".fields_edit_client").empty();
            	 $('.fields_edit_client').append(json);
            	
            },

            error : function(xhr,errmsg,err) {
                // Show an error
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
	
};

function edit_client(client_primary_key){
	
	var frm = $('#form_edit_client');
	
	$.ajax({
		url : "edit_client/"+client_primary_key+"/", // the endpoint
		type : "POST", // http method
		data : frm.serialize(), // data sent with the delete request

		success : function(json) {
			// hide the post
			
			id_client = json.id;
			if (json.result == 'true'){   
				//console.log("Изменили клиента")
			} else {
				alert(json.msg);
			}
		},

		error : function(xhr, errmsg, err) {
			// Show an error
			console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		}
	});

	;
	
  
};

function get_list_clients(filter_clients){
	
	var url = "filter/"+filter_clients+"/";
	if(filter_clients=="all"){
		url = "/myclients/";
	}
	
	
	window.history.pushState(null, null, "/myclients/");
	
	$.ajax({
            url : url, // the endpoint
            type : "POST", // http method
            data : { filter_clients : filter_clients }, // data sent with the delete request
            
            success : function(json) {
            	
            	console.log(json);
            	            	
            	 $(".table_clients").empty();
            	 $('.table_clients').append(json);
            	 
            	 //if(url != window.location){
                 //     window.history.pushState(null, null, url);
                 //}
            	
            },

            error : function(xhr,errmsg,err) {
                // Show an error
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
	
};
