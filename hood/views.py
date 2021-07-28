from django.shortcuts import render,redirect
from .models import Neighborhood,UserProfile,Business,Post
from .forms import ProfileForm,BusinessForm,PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout 

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
           
            return redirect('login')
    else:
        form = UserCreationForm()
    # profile = UserProfile.objects.create(user=request.user)

    return render(request,'registration/register.html',{"form":form})

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def index(request):
    try:
        userprofile = request.user.userprofile
    except UserProfile.DoesNotExist:
        userprofile =  UserProfile(user=request.user)

    hood = request.user.userprofile.hood
    posts = Post.objects.filter(hood=hood).order_by("-id")
    return render(request,"index.html",{"posts":posts,"hood":hood})

@login_required(login_url="login")
def profile(request):
    try:
        userprofile = request.user.userprofile
    except UserProfile.DoesNotExist:
        userprofile =  UserProfile(user=request.user)

    posts = request.user.posts.all().order_by("-id")

    if request.method == 'POST':
        user_form = ProfileForm(request.POST,instance=request.user) 
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect(request.path_info)
    else:
        profile_form = ProfileForm(instance=request.user.userprofile)
        user_form = ProfileForm(instance=request.user)

    return render(request,'profile.html',{"profile":profile,"posts":posts,"profile_form":profile_form,"user_form":user_form})

@login_required(login_url="login")
def business(request):
    hood = request.user.userprofile.hood
    businesses = Business.objects.filter(hood=hood)
    if request.method == 'POST':
        bs_form = BusinessForm(request.POST,request.FILES)
        if bs_form.is_valid():
            form = bs_form.save(commit=False)
            form.user = request.user
            form.hood = hood
            form.save()
        return redirect('business')
    else:
        bs_form = BusinessForm()


    return render(request,"business.html",{"businesses":businesses,"bs_form":bs_form})

@login_required(login_url="login")
def add_post(request):
    hood = request.user.userprofile.hood
    user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            form = post_form.save(commit=False)
            form.user = user
            form.hood = hood
            form.save()
        return redirect('index')
    else:
        post_form = PostForm()

    return render(request,'post.html',{"post_form":post_form})
    
@login_required(login_url="login")
def search_business(request):
    if 'business' in request.GET and request.GET['business']:
        search_business = request.GET.get('business')
        searched_business = Business.find_business(search_business)
        message = f'{search_business}'

        return render(request,'results.html',{"message":message,"searched_business":searched_business})
    else:
        message = "Search Business"
        return render(request,'results.html',{"message":message})