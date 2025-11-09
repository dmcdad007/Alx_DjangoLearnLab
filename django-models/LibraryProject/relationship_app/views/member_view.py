from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_member(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Member'

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'member_view.html', {'user': request.user})