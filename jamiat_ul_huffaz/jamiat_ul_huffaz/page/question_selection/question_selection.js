frappe.pages['question-selection'].on_page_load = function(wrapper) {
	load_screen(wrapper);

	    $("body").keydown(function(e){
	         // e.preventDefault();
	         //now we caught the key code.
	         var keyCode = e.keyCode || e.which;
	         console.log(keyCode);    
	         if(keyCode == 66){
	         	load_screen(wrapper);
	         }
	    });

}

function load_screen(wrapper){
		$(wrapper).fadeOut(500);
		frappe.call({
		    method: 'jamiat_ul_huffaz.endpoints.get_question_selection_list',
		    callback: function(r) {	 
		        $(wrapper).html(r.message);
		        var gap = ($(window).height()-$('#body').height());
		        $('#body').css("margin-top",($(window).height()-$('#body').height())/2);
		        $(wrapper).fadeIn(500);
		        $('.question-group-selection').click(function(e){
		        	e.preventDefault();
		        	$('.question-group-selection').attr('disabled',true);
		        	frappe.call({
		        		method: "jamiat_ul_huffaz.endpoints.set_question",
		        		args:{
		        			'question_group': $(this).attr('data-qg'),
		        			'participant': $('.question-selection-header').attr('data-participant')
		        		},
		        		callback: function(r){
		        			load_screen(wrapper);
		        		}
		        	})
		        });
		    }
		});
}




