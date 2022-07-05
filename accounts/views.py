from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from .models import Profile
from .form import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password= password)
            login(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request,'registration/signup.html', context)

@login_required()
def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {'profile': profile}

    return render(request,'profile.html',context)

# AJAX *********************
def validate_username(request):
    username = request.GET.get('username')
    is_taken = User.objects.filter(username__iexact=username).exists()
    data = {'is_taken':is_taken}
    if data['is_taken']:
        data['error_message'] = "the username already taken"
    return JsonResponse(data)
# AJAX *********************

def editprofile(request):
    return render(request,'editprofile.html')


