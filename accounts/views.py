from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from .models import Profile
from orders.models import OrderItem
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
    created_by = request.user
    profile = get_object_or_404(Profile, slug=slug)
    orders = OrderItem.objects.filter(created_by=created_by)
    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request,'profile.html',context)



def editprofile(request):
    return render(request,'editprofile.html')


