from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

from .models import Pilot, Flight, FlightReport, Airline, AirlinePilot, AirlineLog

@receiver(pre_save, sender=Pilot)
def update_rank_to_pilot(sender, instance, **kwargs):
    if instance.totalFlightHours > 1000:
        instance.rank = 'S'
    elif instance.totalFlightHours > 500:
        instance.rank = 'I'
    else:
        instance.rank = 'J'


@receiver(post_save, sender=Flight)
def generate_report_after_flight_creation(sender, instance, created, **kwargs):
    if created:
        description = f'Flight {instance.code}:\n' \
                      f'Take-off airport: {instance.takeOffAirport}\n' \
                      f'Landing airport: {instance.landAirport}\n' \
                      f'Balloon: {instance.baloon.name}\n' \
                      f'Pilot: {instance.pilot.name} {instance.pilot.surname}\n'\
                      f'Airline: {instance.airline.name}\n'

        FlightReport.objects.create(flight=instance, description=description)

@receiver(pre_delete, sender=Airline)
def assign_pilots_after_airline_deletion(sender, instance, **kwargs):
    airline_pilots = AirlinePilot.objects.filter(airline=instance).all()
    new_airline = Airline.objects.exclude(id=instance.id).first()

    for airline_pilot in airline_pilots:
        airline_pilot.airline = new_airline
        airline_pilot.save()

    # AirlinePilot.objects.create(
    #     airline=new_airline,
    #     pilot=airline_pilot.pilot
    # )

@receiver(post_delete, sender=Airline)
def log_airline_after_deletion(sender,instance, **kwargs):
    AirlineLog.objects.create(
        name=instance.name,
        yearFounded=instance.yearFounded,
        description=f'Airline {instance.name} is deleted from the system!'
    )