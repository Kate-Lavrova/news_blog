from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if auth is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользоатель не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")