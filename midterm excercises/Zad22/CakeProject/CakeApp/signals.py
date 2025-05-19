from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
import random
from CakeApp.models import Baker, Cake


@receiver(pre_delete, sender=Baker)
def delete_baker(sender, instance, **kwargs):
    cakes = Cake.objects.filter(baker = instance).all()
    other_bakers = Baker.objects.exclude(id = instance.id).all()

    for cake in cakes:
        new_baker = random.choice(other_bakers)
        cake.baker = new_baker
        cake.save()