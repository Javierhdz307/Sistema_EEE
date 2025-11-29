from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_admin_group(sender, instance, created, **kwargs):
    if created:
        try:
            Grupo1 = Group.objects.get(name='Admin')
        except Group.DoesNotExist:
            Grupo1 = Group.objects.create(name='Admin')
            Grupo2 = Group.objects.create(name='Especialista')
            Grupo3 = Group.objects.create(name='Encargado')
        instance.user.groups.add(Grupo1)