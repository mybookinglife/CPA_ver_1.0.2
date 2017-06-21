$('document').ready(function(){
	
	$('body').on('click', '.delete_booking', function(){
		var booking_primary_key = $(this).attr('id').split('-')[2];
	    delete_booking(booking_primary_key);
	});	
	
});


//$('document').ready(function(){
//	
//	var dialog_newbooking, form,
//	
//    dialog_newbooking = $("#dialog-form").dialog({
//        autoOpen: false,
//        height: 350,
//        width: 350,
//        modal: true,
//        buttons: {
//          "Create": function(){
//        	  add_booking();  
//        	  dialog_newbooking.dialog( "close" );
//
//          },
//          Cancel: function() {
//        	  dialog_newbooking.dialog("close");
//          }
//        },
//       });
//	
//	$('.new_booking').on('click', function(){
//		dialog_newbooking.dialog( "open" );
//	});		
//
//
//});

$('document').ready(function(){
	
	var dialog_editbooking, form, booking_primary_key
	
	dialog_editbooking = $("#dialog-form").dialog({
        autoOpen: false,
        height: 700,
        width: 450,
        modal: true,
        buttons: {
          "Save": function(){
        	  save_booking(booking_primary_key);
        	  
        	  dialog_editbooking.dialog( "close" );
          },
          Cancel: function() {
        	  dialog_editbooking.dialog("close");
          }
        },
       });
	
	$('body').on('click', '.edit_booking', function(){
		booking_primary_key = $(this).parent().attr('id').split('-')[1];
	    get_booking(booking_primary_key); 
	    dialog_editbooking.dialog( "open" );
	});	
	
//	$('body').on('click', '#new-booking', function(){
	$('#new-booking').on('click', function(){
		booking_primary_key = 0;
		get_booking(booking_primary_key); 
		dialog_editbooking.dialog( "open" );
	});		
});


$('document').ready(function(){
	var filter_booking;
	
	$('#submit_filter').on('click', function(){
		filter_booking = $("#filter_booking :selected").val();
		get_list_bookings(filter_booking);
	});		
	
});


function save_booking(booking_primary_key){
	if (booking_primary_key == 0){
		add_booking();
	}else{
		edit_booking(booking_primary_key);  	
	}
}

function delete_booking(booking_primary_key){
	
	
	if (confirm('are you sure you want to remove this booking?')==true){
    	$.ajax({
            url : "delete_booking/"+booking_primary_key+"/", // the endpoint
            type : "POST", // http method
            data : { booking_pk : booking_primary_key }, // data sent with the delete request
            
            success : function(json) {
                // hide the post
            	if (json.result == 'true'){
            		$('#booking-'+booking_primary_key).remove(); // hide the post on success
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

function add_booking(){
	
	var frm = $('#form_edit_booking');
	
	$.ajax({
		url : "add_booking/", // the endpoint
		type : "POST", // http method
		data : frm.serialize(), // data sent with the delete request

		success : function(json) {
			// hide the post
			
			if (json.result == 'true'){   
			
				$('#list_bookings').append('<li id="booking-'+json.id+'"><a class="edit_booking">'+json.name+'</a><input class="delete_booking" type="button" name="submit" id="delete-booking-'+json.id+'" value="Delete"></li>'); // hide the post on success
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

function get_booking(booking_primary_key){
	
	$.ajax({
            url : "get_info_booking/"+booking_primary_key+"/", // the endpoint
            type : "POST", // http method
            async: false,
            data : { booking_pk : booking_primary_key }, // data sent with the delete request
            
            success : function(json) {
            
            	 $(".fields_edit_booking").empty();
            	 $('.fields_edit_booking').append(json);
            	 set_select_chained();
            	
            },

            error : function(xhr,errmsg,err) {
                // Show an error
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
	
	
	
};

function edit_booking(booking_primary_key){
	
	var frm = $('#form_edit_booking');
	
	$.ajax({
		url : "edit_booking/"+booking_primary_key+"/", // the endpoint
		type : "POST", // http method
		data : frm.serialize(), // data sent with the delete request

		success : function(json) {
			// hide the post
			
			id_booking = json.id;
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

function get_list_bookings(filter_bookings){
	
	var url = "filter/"+filter_bookings+"/";
	if(filter_bookings=="all"){
		url = "/mybookings/";
	}
	
	
	window.history.pushState(null, null, "/mybookings/");
	
	$.ajax({
            url : url, // the endpoint
            type : "POST", // http method
            data : { filter_bookings : filter_bookings }, // data sent with the delete request
            
            success : function(json) {
            	
            	console.log(json);
            	            	
            	 $(".table_bookings").empty();
            	 $('.table_bookings').append(json);
            	 
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
