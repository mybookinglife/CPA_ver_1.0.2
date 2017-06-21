$('document').ready(function(){
	
	$('body').on('click', '.delete_expert', function(){
		var expert_primary_key = $(this).attr('id').split('-')[2];
	    //console.log(expert_primary_key); // sanity check
	    delete_expert(expert_primary_key);
	});	
	
	$('body').on('click','.select_expert', function(){
		var expert_primary_key = $(this).parent().attr('id').split('-')[1];
		console.log(expert_primary_key); // sanity check
		get_service_experts(expert_primary_key);
	});	
	

	$('body').on('click','.edit_service_experts', function() {
		var expert_primary_key = $(this).parent().attr('id').split('-')[2];
		var service_primary_key = $(this).parent().attr('id').split('-')[1];
		var is_active = $(this).children().is(':checked')
//		console.log(expert_primary_key);
//		console.log(service_primary_key);
//		console.log(is_active);
		
		add_service_experts(is_active, expert_primary_key, service_primary_key);

		
	});	
		

	
});

$('document').ready(function(){
	//alert('test');
	
	var dialog_newexpert, form,
	
    dialog_newexpert = $("#dialog-form").dialog({
        autoOpen: false,
        height: 350,
        width: 350,
        modal: true,
        buttons: {
          "Create": function(){
        	  add_expert();  
        	  dialog_newexpert.dialog( "close" );

          },
          Cancel: function() {
        	  dialog_newexpert.dialog("close");
          }
        },
       });
	
	$('.new_expert').on('click', function(){
		dialog_newexpert.dialog( "open" );
	});		

	
//	form = dialog.find("form").on( "submit", function( event ) {
//	      event.preventDefault();
//	      add_expert(dialog.find("form"));
//	    });
//	
});

$('document').ready(function(){
	
	var dialog_editexpert, form, expert_primary_key
	
    dialog_editexpert = $("#dialog-form").dialog({
        autoOpen: false,
        height: 450,
        width: 350,
        modal: true,
        buttons: {
          "Save": function(){
        	  edit_expert(expert_primary_key);  
        	  dialog_editexpert.dialog( "close" );

          },
          Cancel: function() {
        	  dialog_editexpert.dialog("close");
          }
        },
       });
	
	$('body').on('click','.edit_expert', function(){
		expert_primary_key = $(this).parent().attr('id').split('-')[1];
	    //console.log(expert_primary_key); // sanity check
	    get_expert(expert_primary_key); 
	    dialog_editexpert.dialog( "open" );
	});		
	
});


$('document').ready(function(){
	var filter_expert;
	
	$('.submit_filter').on('click', function(){
		filter_expert = $("#filter_expert :selected").val();
		get_list_expert(filter_expert);
	});		
	
});

function delete_expert(expert_primary_key){
	
	
	if (confirm('are you sure you want to remove this expert?')==true){
    	$.ajax({
            url : "delete_expert/"+expert_primary_key+"/", // the endpoint
            type : "POST", // http method
            data : { expert_pk : expert_primary_key }, // data sent with the delete request
            
            success : function(json) {
                // hide the post
            	if (json.result == 'true'){
            		$('#expert-'+expert_primary_key).remove(); // hide the post on success
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

function add_expert(){
	
	var frm = $('#form_new_expert');
	
	$.ajax({
		url : "add_expert/", // the endpoint
		type : "POST", // http method
		data : frm.serialize(), // data sent with the delete request

		success : function(json) {
			// hide the post
			
			//id_expert = json.id;
			if (json.result == 'true'){   
			
				$('#list_expert').append('<li id="expert-'+json.id+'"><a class="edit_expert">'+json.name+'</a><input class="delete_expert" type="button" name="submit" id="delete-expert-'+json.id+'" value="Delete"></li>'); // hide the post on success
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

function get_expert(expert_primary_key){
	
	$.ajax({
            url : "get_info_expert/"+expert_primary_key+"/", // the endpoint
            type : "POST", // http method
            data : { expert_pk : expert_primary_key }, // data sent with the delete request
            
            success : function(json) {
            
            	 $(".fields_edit_expert").empty();
            	 $('.fields_edit_expert').append(json);
            	
            },

            error : function(xhr,errmsg,err) {
                // Show an error
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
	
};

function edit_expert(expert_primary_key){
	
	var frm = $('#form_edit_expert');
	
	$.ajax({
		url : "edit_expert/"+expert_primary_key+"/", // the endpoint
		type : "POST", // http method
		data : frm.serialize(), // data sent with the delete request

		success : function(json) {
			// hide the post
			
			id_expert = json.id;
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

function get_list_expert(filter_expert){
	
	var url = "filter/"+filter_expert+"/";
	if(filter_expert=="all"){
		url = "/myexperts/";
	}
	//window.history.pushState(null, null, "/expert/");
	
	$.ajax({
            url : url, // the endpoint
            type : "POST", // http method
            data : { filter_expert : filter_expert }, // data sent with the delete request
            
            success : function(json) {
            	
            	//console.log(json);
            	            	
            	 $(".table_expert").empty();
            	 $('.table_expert').append(json);
            	 
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


function get_service_experts(expert_primary_key){
	
	url = "get_service_experts/"+expert_primary_key+"/";
	
	$.ajax({
            url : url, // the endpoint
            type : "POST", // http method
            data : { pk : expert_primary_key }, // data sent with the delete request
            
            success : function(json) {
            	
            	//console.log(json);
            	            	
            	 $(".table_service_experts").empty();
            	 $('.table_service_experts').append(json);
            	 
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

function add_service_experts(is_active, expert_primary_key, service_primary_key){

	if (is_active==true){
		url = "add_service_experts/"+expert_primary_key+"/"+service_primary_key+"/";
	}else{
		url = "delete_service_experts/"+expert_primary_key+"/"+service_primary_key+"/";
	}
	
   	$.ajax({
   		url : url, // the endpoint
        type : "POST", // http method
        data : { expert_pk : expert_primary_key, service_pk : service_primary_key }, // data sent with the delete request
        
        success : function(json) {
            // hide the post
        	if (json.result == 'true'){
        		
        	} else{
        	}
        	
        },

        error : function(xhr,errmsg,err) {
            // Show an error
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
	
};
