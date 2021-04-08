from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    user = request.user
    return render(request, 'app/index.html', {'user': user})


class UserLogin(LoginView):
    template_name = 'app/loginpage.html'


class UserLogout(LogoutView):
    template_name = 'app/logoutpage.html'


@login_required
def loginrequired(request):
    return render(request, 'app/loginrequired.html', {
        'user': request.user
    })
