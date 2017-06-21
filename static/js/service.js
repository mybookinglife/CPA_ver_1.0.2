$('document').ready(function(){
	
	$('body').on('click', '.delete_service', function(){
		var service_primary_key = $(this).attr('id').split('-')[2];
	    //console.log(service_primary_key); // sanity check
	    delete_service(service_primary_key);
	});	
	
});


$('document').ready(function(){
	//alert('test');
	
	var dialog_newservice, form,
	
    dialog_newservice = $("#dialog-form").dialog({
        autoOpen: false,
        height: 350,
        width: 350,
        modal: true,
        buttons: {
          "Create": function(){
        	  add_service();  
        	  dialog_newservice.dialog( "close" );

          },
          Cancel: function() {
        	  dialog_newservice.dialog("close");
          }
        },
       });
	
	$('.new_service').on('click', function(){
		dialog_newservice.dialog( "open" );
	});		

	
//	form = dialog.find("form").on( "submit", function( event ) {
//	      event.preventDefault();
//	      add_service(dialog.find("form"));
//	    });
//	
});

$('document').ready(function(){
	
	var dialog_editservice, form, service_primary_key
	
    dialog_editservice = $("#dialog-form").dialog({
        autoOpen: false,
        height: 450,
        width: 350,
        modal: true,
        buttons: {
          "Save": function(){
        	  edit_service(service_primary_key);  
        	  dialog_editservice.dialog( "close" );

          },
          Cancel: function() {
        	  dialog_editservice.dialog("close");
          }
        },
       });
	
	$('body').on('click','.edit_service', function(){
		service_primary_key = $(this).parent().attr('id').split('-')[1];
	    //console.log(service_primary_key); // sanity check
	    get_service(service_primary_key); 
	    dialog_editservice.dialog( "open" );
	});		
	
});


$('document').ready(function(){
	var filter_service;
	
	$('.submit_filter').on('click', function(){
		filter_service = $("#filter_service :selected").val();
		get_list_service(filter_service);
	});		
	
});

function delete_service(service_primary_key){
	
	
	if (confirm('are you sure you want to remove this service?')==true){
    	$.ajax({
            url : "delete_service/"+service_primary_key+"/", // the endpoint
            type : "POST", // http method
            data : { service_pk : service_primary_key }, // data sent with the delete request
            
            success : function(json) {
                // hide the post
            	if (json.result == 'true'){
            		$('#service-'+service_primary_key).remove(); // hide the post on success
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

function add_service(){
	
	var frm = $('#form_new_service');
	
	$.ajax({
		url : "add_service/", // the endpoint
		type : "POST", // http method
		data : frm.serialize(), // data sent with the delete request

		success : function(json) {
			// hide the post
			
			//id_service = json.id;
			if (json.result == 'true'){   
			
				$('#list_service').append('<li id="service-'+json.id+'"><a class="edit_service">'+json.name+'</a><input class="delete_service" type="button" name="submit" id="delete-service-'+json.id+'" value="Delete"></li>'); // hide the post on success
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

function get_service(service_primary_key){
	
	$.ajax({
            url : "get_info_service/"+service_primary_key+"/", // the endpoint
            type : "POST", // http method
            data : { service_pk : service_primary_key }, // data sent with the delete request
            
            success : function(json) {
            
            	 $(".fields_edit_service").empty();
            	 $('.fields_edit_service').append(json);
            	
            },

            error : function(xhr,errmsg,err) {
                // Show an error
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
	
};

function edit_service(service_primary_key){
	
	var frm = $('#form_edit_service');
	
	$.ajax({
		url : "edit_service/"+service_primary_key+"/", // the endpoint
		type : "POST", // http method
		data : frm.serialize(), // data sent with the delete request

		success : function(json) {
			// hide the post
			
			id_service = json.id;
			if (json.result == 'true'){   
				//console.log("Изменили услугу")
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

function get_list_service(filter_service){
	
	var url = "filter/"+filter_service+"/";
	if(filter_service=="all"){
		url = "/myservices/";
	}
	
	
	window.history.pushState(null, null, "/myservices/");
	
	$.ajax({
            url : url, // the endpoint
            type : "POST", // http method
            data : { filter_service : filter_service }, // data sent with the delete request
            
            success : function(json) {
            	
            	console.log(json);
            	            	
            	 $(".table_service").empty();
            	 $('.table_service').append(json);
            	 
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
