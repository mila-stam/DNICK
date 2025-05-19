from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

from .models import Event, Bend, EventBend

@receiver(pre_delete, sender=Event)
def assign_bends(sender, instance, **kwargs):
    event_bends = EventBend.objects.filter(event=instance).all()

    if instance.is_open:
        assignedEvent = Event.objects.exclude(id=instance.id).filter(isOpen=True).first()
    else:
        assignedEvent = Event.objects.exclude(id=instance.id).filter(isOpen=False).first()

    # assignedEvent = Event.objects.exclude(id=instance.id).filter(date__gte=instance.date).first()

    for event_bend in event_bends:
        event_bend.event = assignedEvent
        event_bend.save()




