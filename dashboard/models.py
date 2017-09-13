from django.db import models
from django.contrib.auth.models import User
from lib.choices import SCHOOL_NAME_CHOICES, CLASS_STANDING_CHOICES, \
                        SHIRT_SIZE_CHOICES, STATUS_CHOICES
from django.db.models.signals import post_save
from django.dispatch import receiver


def resume_loc(instance, filename):
    return '/'.join(['profiles', str(instance.user.pk), filename])

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    dietary_restrictions = models.CharField(default="", max_length=128, blank=True)

    shirt_size = models.IntegerField(default=2, choices=SHIRT_SIZE_CHOICES)

    school = models.IntegerField(default=-1, choices=SCHOOL_NAME_CHOICES)

    major = models.CharField(default="Unknown", max_length=128)

    grade = models.IntegerField(default=0, choices=CLASS_STANDING_CHOICES)

    status = models.IntegerField(default=0, choices=STATUS_CHOICES)

    travel = models.BooleanField(default=False)

    resume = models.FileField(blank=True, null=True, upload_to=resume_loc)

    class Meta:
        db_table = "profile_tbl"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
