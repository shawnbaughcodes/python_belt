from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

# current user method
def current_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])
# end current user method

def index(request):
    return render(request, 'python_belt/index.html')

def process(request):
    is_valid = User.objects.register_validate(request.POST)
    if type(is_valid) == dict:
        for error in is_valid['errors']:
            messages.error(request, error)
            return redirect('/')
    else:
        user = User.objects.create_user(request.POST)
        request.session['user_id'] = user.id
        return redirect('/home')

def login(request):
    is_valid = User.objects.login_validate(request.POST)
    if is_valid['status'] == True:
        request.session['user_id'] = is_valid['user'].id
        return redirect('/home')
    else:
        if is_valid['status'] == False:
            messages.error(request, is_valid['message'])
        return redirect('/')

def home(request):
    user = current_user(request)
    friends_ids = []
    for friend in user.friends.all():
        friends_ids.append(friend.id)
    context = {
        'current_user': user,
        'friends': user.friends.all(),
        'users': User.objects.exclude(id__in=friends_ids)
    }
    return render(request, 'python_belt/home.html', context)

def add_friend(request, id):
    user = current_user(request)
    friend = User.objects.get(id=id)
    user.friends.add(friend)
    return redirect('/home')

def remove_friend(request, id):
    user = current_user(request)
    friend = User.objects.get(id=id)
    user.friends.remove(friend)
    return redirect('/home')

def profile(request, id):
    context = {
    'user': User.objects.get(id=id),
    }
    return render(request, 'python_belt/profile.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')
