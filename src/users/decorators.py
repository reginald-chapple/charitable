from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

# if not (scene.user.id == request.user.id): 
#     return HttpResponse("It is not yours ! You are not permitted !", content_type="application/json", status=403)

def member_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_member,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
