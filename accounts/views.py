from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(Requests):
    if Requests.method == 'POST':
        # Register User
        first_name = Requests.POST['first_name']
        last_name = Requests.POST['last_name']
        username = Requests.POST['username']
        email = Requests.POST['email']
        password = Requests.POST['password']
        password2 = Requests.POST['password2']
        # Check passwords
        if password == password2:
            if User.objects.filter(username= username).exists():
                messages.error(Requests, 'The username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email= email).exists():
                    messages.error(Requests, 'The email is already registered')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username= username, email= email, password= password,
                                                    first_name= first_name, last_name = last_name)
                    messages.success(Requests, 'You are now registered.')
                    user.save()
                    return redirect('index')
        else:
            messages.error(Requests, 'Passwords does not match')
            return redirect('register')
    else:
        return render(Requests, 'accounts/register.html')

def login(Requests):
    # User Login
    if Requests.method == 'POST':
        username = Requests.POST['username']
        password = Requests.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(Requests, user)
            messages.success(Requests, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(Requests, 'Username or password not matched.')
            return redirect('login')
    else:
        return render(Requests, 'accounts/login.html')

def logout(Requests):
    if Requests.method == 'POST':
        auth.logout(Requests)
        messages.success(Requests, 'You are logged out.')
        return redirect('index')

def dashboard(Requests):
    user_contatcs = Contact.objects.order_by('-contact_time').filter(user_id=Requests.user.id)
    content = {
        'contacts': user_contatcs
    }
    return render(Requests, 'accounts/dashboard.html', content)
