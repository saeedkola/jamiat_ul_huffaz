frappe.pages['participant-selection'].on_page_load = function(wrapper) {


	frappe.call({
	    method: 'jamiat_ul_huffaz.endpoints.get_participant_groups',
	    callback: function(r) {	 
	        $(wrapper).html(r.message);
	        $('#body').css("margin-top",($(window).height()-$('#body').height())/2);
	        $('.group-selection-tile').click(function(){
				var p_group = $(this).attr('data-group');
				frappe.call({
					method: 'jamiat_ul_huffaz.endpoints.get_random_participant',
					args:{
						'group': p_group
					},
					callback: function(r){
						$('#participant-profile').html(r.message);
						$('#exampleModal').modal('show');
					}
				})
			});
	        
	    }
	});




	
}