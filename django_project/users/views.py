from django.shortcuts import render, redirect
from django.contrib import messages #Note:Called the flash message
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm

def register(request):
    print(request) # Note:<WSGIRequest: POST '/register/'> or <WSGIRequest: GET '/register/'>, We can see that any requests that comes into this route, 
    # either get or post, we will execute the following codes
    if request.method == 'POST':
        #Note: I want to create a form that has the data that was within request.post, then it 
        # has a new form with our username data and our two password fields
        form = UserRegisterForm(request.POST)
        # print('form', form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #Note: The flash message will send with form data to templates, you can use the passed message in template by saying messages
            messages.success(request, f'Account create for {username}!')
            return redirect('blog-home') #Note: This is the name we give to our url pattern of blog home page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')



