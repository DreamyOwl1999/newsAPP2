from django.shortcuts import redirect, render
from  register.forms import RegisterForm
from news.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def registerUser(response):
    if response.method =="POST":
        form = RegisterForm(response.POST)
        recipient = str(form['email'].value())
        form.save()
        subject = 'Welcome to WEBAPP'
        message = 'Hope you are enjoying your WEBAPP'
        print(recipient)
        print(EMAIL_HOST_USER)
        send_mail(subject,
            message, EMAIL_HOST_USER, [recipient], fail_silently = False)

        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})
