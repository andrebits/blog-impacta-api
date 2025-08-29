
delete from django_rest_passwordreset_resetpasswordtoken;
delete from auth_user;

select id, username, email, password, date_joined  from auth_user;