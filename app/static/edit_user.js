var user_id = {{ user.id }};

// this object holds field elements
var edit_form = {
  fullname_field: document.getElementsByName('full_name')[0],
  email_field: document.getElementsByName('email')[0],
  is_active_field: document.getElementsByName('is_active')[0],
  role_field: document.getElementsByName('role_id')[0]
};

reset_data();
function reset_data(){
  edit_form.fullname_field.value = "{{ user.full_name }}";
  edit_form.email_field.value = "{{ user.email }}";
  edit_form.role_field.selectedIndex = {{ user.role_id }};
  edit_form.is_active_field.checked = {% if user.is_active == True %}0{% else %}1{% endif %};
}

// setup modal
$('#reset-modal').on('click', '.btn-ok', function(e) {

    $.ajax({
            url: '/users/' + user_id + '/reset_password',
            type: 'POST',
            error: function(xhr,status,error){
                    console.log('error');
                    $('#reset-modal').modal('hide');
                },
            success: function(result,status,xhr){
                    console.log('success');
                    $('#reset-modal').modal('hide');
                },
            }
    );
});
