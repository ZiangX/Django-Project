from django.shortcuts import render, redirect
from django.contrib import messages #Note:Called the flash message
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    # print(request) # Note:<WSGIRequest: POST '/register/'> or <WSGIRequest: GET '/register/'>, We can see that any requests that comes into this route, 
    # either get or post, we will execute the following codes according to the request type
    if request.method == 'POST':
        #Note: I want to create a form that has the data that was within request.post, then it 
        # has a new form with our username data and our two password fields
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #Note: The flash message will send with form data to templates, you can use the passed message in template by saying messages
            messages.success(request, f'Account create for {username}!')
            return redirect('login') #Note: This is the name we give to our url pattern of blog home page
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) #Note:Represent the Current login user
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #Since image is a file, we put a new field here
        if  u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You account has been updated!')
            #Note:Redirecting immediately is to avoid the warning message that form will be resubmited when users update the page
            return redirect('profile') 
    else:
        u_form = UserUpdateForm(instance=request.user) #Note:Represent the Current login user
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)



