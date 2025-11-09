from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Librarian'

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'librarian_view.html', {'user': request.user})