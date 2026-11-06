from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import Token
from django.urls import reverse
from .models import User
from django.contrib import messages , auth
from accounts.models import Token
# Create your views here.


# def send_login_email(request):
#     return redirect("/")

def send_login_email(request):
    email = request.POST["email"]
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(  
        reverse("login") + "?token=" + str(token.uid),
    )
    message_body = f"Use this link to log in:\n\n{url}"
    # print(type(send_mail))
    send_mail(
        "Your login link for Superlists",
        message_body,
        "noreply@superlists",
        [email],
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in.",
    )
    return redirect("/")

def login(request):
    # auth.authenticate(uid=request.GET["token"])
    if user := auth.authenticate(uid=request.GET["token"]):
        auth.login(request, user)  
    else:
        messages.error(request, "Invalid login link, please request a new one")  
    return redirect("/")

    