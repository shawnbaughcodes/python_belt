from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def current_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])
def index(request):
    return render(request, 'python_belt/index.html')

def register_user(request):
    is_valid = User.objects.register_validate(request.POST)
    if type(is_valid) == dict:
        for error in is_valid['errors']:
            messages.error(request, error)
            return redirect('/')
    else:
        user = User.objects.create_user(request.POST)
        return render(request, 'python_belt/dashboard.html')

def login(request):
    is_valid = User.objects.login_validate(request.POST)
    if is_valid['status'] == True:
        request.session['id'] = is_valid['user'].id
        return redirect('/dashboard')
    else:
        if is_valid['status'] == False:
            messages.error(request, is_valid['message'])
        return redirect('/')
def dashboard(request):
    context = {
    'current_user': current_user(request),
    'quote': Quotes.objects.all(),
    # 'favorite': Quotes.objects.annotate(favorites=('favorite'))
    }
    return render(request, 'python_belt/dashboard.html', context)

def process_quote(request):
    is_valid = Quotes.objects.quote_validation(request.POST)
    if type(is_valid) == dict:
        for error in is_valid['errors']:
            messages.error(request, error)
        return redirect('/dashboard')
    else:
        quote = Quotes.objects.create(author=request.POST['author'],quote=request.POST['quote'], user_id=current_user(request))
        return render(request, 'python_belt/dashboard.html', quote)
def logout(request):
    request.session.clear()
    return redirect('/')

# FUCK IT.
