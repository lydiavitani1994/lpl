from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from contacts.models import Contact


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'Login success!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Password do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            email=email,
            username=username,
            password=password
        )
        auth.login(request, user)
        user.save()
        messages.success(request, 'User created successfully!')
        return redirect('dashboard')
    else:
        return render(request, 'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    user_inquiries = Contact.objects.order_by('-timestamp').filter(user_id=request.user.id)
    data = {
        'inquiries': user_inquiries
    }
    return render(request, 'accounts/dashboard.html', data)


def logout(request):
    auth.logout(request)
    return redirect('home')
