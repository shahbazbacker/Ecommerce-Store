from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, get_user_model
from .forms import ContactForm
from django.contrib import messages


# def about_page(request):
#     context = {
#         'title': 'AboutPage',
#         'content': 'This is us...'
    
#     }
#     return render(request, 'about.html', context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data
        form.save()
        messages.add_message(request, messages.INFO, 'Your Feedback Added.')
        return redirect(contact_page)
    context = {
        'title': 'Contact',
        'content': 'Please provide your feedback',
        'form': form
    }
    return render(request, 'contact.html', context)

# def login_page(request):
#     form = LoginForm(request.POST or None)
#     if form.is_valid():
#        username = form.cleaned_data.get('username')
#        password = form.cleaned_data.get('password')

#        user = authenticate(username=username, password=password)
#        if user is not None:
#            login(request, user)
#            return redirect('/')

#     context = {'form' : form}
#     return render(request, 'login.html', context)


# User = get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         email = form.cleaned_data.get('email')
#         password = form.cleaned_data.get('password')
#         password2 = form.cleaned_data.get('password2')
#         # new_user = User.objects.create_user(username, email, password)
#         # print(new_user)


#     context = {'form' : form}
#     return(render, 'register.html', context)
#     