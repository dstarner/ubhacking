from django.contrib import messages

def notify_form_errors(request, form):
    for field in form:
        for error in field.errors:
            messages.error(request, error.replace("This", field.label).replace("this", field.label))
    for error in form.non_field_errors():
        messages.error(request, error)
