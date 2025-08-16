import json
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .models import User  # make sure User is a proper Django auth user model
from .models import Country


def signup(request):
    return render(request, "signup.html")


@csrf_exempt
def signup_validate(request):
    body = json.loads(request.body)
    email = body.get("email", "")
    first_name = body.get("first_name", "")
    last_name = body.get("last_name", "")
    password = body.get("password", "")

    if not email:
        return JsonResponse({"success": False, "message": "email not found"})
    if not first_name:
        return JsonResponse({"success": False, "message": "first name not found"})
    if not password:
        return JsonResponse({"success": False, "message": "password not found"})

    try:
        User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
    except IntegrityError:
        return JsonResponse({"success": False, "message": "user already exists"})

    return JsonResponse({"success": True, "message": "signup succeeded"})



def c_login(request):
    return render(request, "login.html")


@csrf_exempt
def login_validate(request):
    body = json.loads(request.body)
    email = body.get("email", "")
    password = body.get("password", "")

    if not email or not password:
        return JsonResponse({"success": False, "message": "email or password missing"})

    try:
        user = User.objects.get(email=email)
        if not user.check_password(password):
            return JsonResponse({"success": False, "message": "incorrect password"})
    except User.DoesNotExist:
        return JsonResponse({"success": False, "message": "user not found"})

    login(request, user)
    return JsonResponse({"success": True, "message": "login succeeded"})


@login_required
def c_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")


@login_required
def home(request):
    return render(request, "home.html")

def search(request):
    query = request.GET.get("query", "")
    result = {}  # your search logic here
    return render(request, "search_results.html", result)

def get_country_details(request, country_name):
    try:
        country = Country.objects.get(name=country_name)
    except Country.DoesNotExist:
        country = None

    return render(request, "country.html", {"country": country})