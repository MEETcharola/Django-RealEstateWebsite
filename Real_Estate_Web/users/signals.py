from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.filter(user=instance)
        print(f"INSTANCE : {instance}")
        print(f"PROFILE : {profile}")
        if profile:
            print("INSIDE TRUTH 1")
            profile = instance.profile
            profile.save()
            pass
        else:
            Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    profile = Profile.objects.filter(user=instance)
    print(f"PROFILE : {profile}")
    if profile:
        print("INSIDE TRUTH 2")
        pass
    else:
        instance.profile.save()




