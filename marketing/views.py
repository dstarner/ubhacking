from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_user, authenticate, login as login_user
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from lib.decorators import anonymous_required
from lib.helpers import notify_form_errors
from . import models, forms

def index(request):
    faqs = models.FAQ.objects.all()
    return render(request, "marketing/index.html", {"faqs": faqs})

@anonymous_required
def login(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST)

        if form.is_valid():

            user = authenticate(request, username=form.cleaned_data["email"],
                                password=form.cleaned_data["password"])

            if user:
                login_user(request, user)
                return redirect('dashboard:index')
            else:
                messages.error(request, "Invalid credentials provided.")
    else:
        form = forms.UserLoginForm()
    return render(request, "marketing/login.html", {"form": form})


@anonymous_required
def register(request):
    if request.method == 'POST':
        form = forms.HackerRegistrationForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.create(email=form.cleaned_data["email"],
                                       username=form.cleaned_data["email"],
                                       password=form.cleaned_data["password"],
                                       first_name=form.cleaned_data["first_name"],
                                       last_name=form.cleaned_data["last_name"])

            user.set_password(form.cleaned_data["password"])

            # Add the user to the correct groups
            user.groups.add(Group.objects.filter(name="Hackers").first())

            # Add to the user's profile
            profile = user.profile
            profile.dietary_restrictions = form.cleaned_data["dietary_restrictions"]
            profile.shirt_size = form.cleaned_data["shirt_size"]
            profile.school = form.cleaned_data["school_name"]
            profile.major = form.cleaned_data["school_major"]
            profile.grade = form.cleaned_data["class_standing"]
            profile.travel = form.cleaned_data["travel_reimbursement"]

            profile.resume = form.cleaned_data["resume"]

            profile.save()

            return redirect("login")

        else:
            notify_form_errors(request, form)

    else:
        form = forms.HackerRegistrationForm()
    return render(request, "marketing/register.html", {"form": form})


@anonymous_required
def forgot_password(request):
    return

@login_required
def logout(request):
    logout_user(request)
    return redirect("index")
