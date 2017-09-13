from django import forms
from lib.choices import CLASS_STANDING_CHOICES, SCHOOL_NAME_CHOICES, SHIRT_SIZE_CHOICES


class EditProfileForm(forms.Form):

    email = forms.EmailField(required=True)

    password = forms.CharField(required=False, widget=forms.PasswordInput, min_length=8)

    retype_password = forms.CharField(required=False, widget=forms.PasswordInput)

    first_name = forms.CharField(required=True, max_length=64)

    last_name = forms.CharField(required=True, max_length=64)

    school_major = forms.CharField(required=True, max_length=64)

    class_standing = forms.ChoiceField(required=True, choices=CLASS_STANDING_CHOICES)

    school_name = forms.ChoiceField(required=True, choices=SCHOOL_NAME_CHOICES)

    resume = forms.FileField(required=False)

    dietary_restrictions = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    shirt_size = forms.ChoiceField(required=True, choices=SHIRT_SIZE_CHOICES)

    travel_reimbursement = forms.BooleanField()

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('retype_password')

        if password1 and len(password1) > 0 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data
