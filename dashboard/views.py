from django.shortcuts import render
from django.contrib import messages
from . import forms
from lib.helpers import notify_form_errors

def index(request):
    is_hacker = request.user.groups.filter(name='Hackers').exists()
    is_organizer = request.user.groups.filter(name='Organizers').exists()

    return render(request, "dashboard/index.html", {'is_hacker': is_hacker,
                                                    'is_organizer': is_organizer})


def edit_profile(request):
    if request.method == 'POST':

        form = forms.EditProfileForm(request.POST, request.FILES)

        if form.is_valid():

            user = request.user

            # Update the user model
            user.email = form.cleaned_data["email"]
            user.username = form.cleaned_data["email"]

            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]

            if len(form.cleaned_data["password"]) > 0:
                user.set_password(form.cleaned_data["password"])
                messages.success(request, "Successfully updated password!")

            # Update the profile
            profile = user.profile
            profile.dietary_restrictions = form.cleaned_data["dietary_restrictions"]
            profile.shirt_size = form.cleaned_data["shirt_size"]
            profile.school = form.cleaned_data["school_name"]
            profile.major = form.cleaned_data["school_major"]
            profile.grade = form.cleaned_data["class_standing"]
            profile.travel = form.cleaned_data["travel_reimbursement"]

            print(form.cleaned_data["resume"])
            if form.cleaned_data["resume"]:
                profile.resume = form.cleaned_data["resume"]

            user.save()
            profile.save()
            messages.success(request, "Successfully updated your profile!")

        else:
            notify_form_errors(request, form)

    else:
        form = forms.EditProfileForm()

    return render(request, "dashboard/edit-profile.html", {"form": form})
