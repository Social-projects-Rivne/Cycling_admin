$(document).ready(function(){
    var user_id = NaN;
    var role = NaN;
    var cipId = NaN;

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
	cipId = $(this).data('cipId');
        $('#roleEditModal').modal('show');
    });
    $('#roleEditModal').on('click', '.btn-primary', function(e) {
        roleChanged = false
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
	// $('.table_select[data-cip-id="' + cipId + '"]')[0].value = roleArray[user_id];
    });
});
