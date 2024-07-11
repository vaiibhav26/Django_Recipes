from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required




# Create your views here.

@login_required(login_url= '/login/')
def recipes(request):
    if request.method =="POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(recipe_name = recipe_name,
                            recipe_description = recipe_description,
                            recipe_image = recipe_image)
        
        return redirect('/recipes')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}

        
    return render(request, 'recipes.html', context )

@login_required(login_url= '/login/')
def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image :
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes')


    context = {'recipe': queryset}
    return render(request, 'update_recipes.html', context )

@login_required(login_url= '/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes')



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect(reverse('login_page'))
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect(reverse('login_page'))
        
        else:
            login(request, user)
            return redirect(reverse('recipes'))

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if all required fields are present
        if not first_name or not last_name or not username or not password:
            return render(request, 'register.html', {'error': 'All fields are required.'})

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists.'})

        # Create the user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        # Redirect to login page after successful registration
        return redirect('/login/')

    return render(request, 'register.html')

