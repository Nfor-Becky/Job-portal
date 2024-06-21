from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import  PostForm, ProfileForm
from .models import Post,profile
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, "index.html", {})
def about(request):
    return render(request, "about.html", {})
def contact(request):
    return render(request, "contact.html", {})

def register(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        email =request.POST.get('email')
        password =request.POST.get('password')

        # check for password length
        if len(password) < 3:
            messages.error(request, 'password must be atleast 3 characters')
            return redirect('register')
        get_all_users_by_username = User.objects.filter(username = username)
        #check if user exist
        #filters all users by username, it checks if there is any user with same username
        if get_all_users_by_username:
           messages.error(request, 'Error, username already exist, use another')
           return redirect('register')
       #creates new user
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, 'user successfully created login now')
        return redirect('login')
    return render(request, 'register.html', {})
def loginpage(request):
    if request.user.is_authenticated:
         return redirect('post')
    if request.method == 'POST':
        username =request.POST.get('uname')
        password =request.POST.get('pass')
        
        validate_user = authenticate(username = username, password= password)
        if validate_user is not None:
             login(request, validate_user)
             return redirect('post')
        else:
             messages.error(request, 'Error, wrong user details')
             return redirect('login')
    return render(request, 'login.html', {})

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required
def post(request):
    context = {
        'posts': Post.objects.all().order_by('-posted_date')
    }
    return render(request, "post.html", context)
@login_required
def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, "details.html", context)
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = PostForm(instance=post)
    return render(request, 'create_post.html', {'form': form})
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post')
    return render(request, 'delete_post.html', {'post': post})


@login_required
def create_profile(request):
    profile = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm()

    return render(request, 'create_profile.html', {'form': form})

@login_required
def profile_detail(request, pk):
    user_profile = get_object_or_404(profile, pk=pk)
    if user_profile.user == request.user:
        return render(request, 'profile_details.html', {'profile': user_profile})
    else:
        return redirect('post')
@login_required
def profile_edit(request):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_profile.html', {'form': form})


   