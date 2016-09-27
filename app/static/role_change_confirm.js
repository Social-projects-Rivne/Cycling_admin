$(document).ready(function(){
    var user_id = NaN;
    var role = NaN;
    var roleArray = {};

    var selects = $('.table_select');
    var i = 0;
    while (true) {
	if (selects.hasOwnProperty(i)) {
	    roleArray[selects[i].getAttribute('data-id')] = selects[i].value;
            i++;
	}
	else {
	    break;
	}
    }

    $('.table_select').on('change', function(){
	user_id = $(this).data('id');
	role = $(this).val();
        $('#roleEditModal').modal('show');
    });
    $('#roleEditModal').on('click', '.btn-primary', function(e) {
        $.ajax({
		url: '/users/' + user_id + '/role_edit',
		data: '{"user_role": "' + (role === 'admin' ? '1' : '0') + '"}',
		contentType: 'application/json',
		dataType: 'json',
		type: 'POST',
		error: function(xhr, status, error) {
                    console.log(error)
		},
		success: function(result, status, xhr) {
		    roleArray[user_id] = role;    
		}
	})
    });
    $('#roleEditModal').on('hidden.bs.modal', function() {
        $.ajax({
		url: '/users/' + user_id + '/get_role',
		data: '',
		contentType: 'application/json',
		dataType: 'json',
		type: 'POST',
		error: function(xhr, status, error) {
                    console.log(error)
                    $('.table_select[data-id="' + user_id + '"]')[0].value = roleArray[user_id];
		},
		success: function(result, status, xhr) {
		    roleArray[user_id] = result['message'];    
                    $('.table_select[data-id="' + user_id + '"]')[0].value = result['message'];

		}
	})
    });
});
