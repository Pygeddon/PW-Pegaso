from django.db import models

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    event_slug = models.SlugField(max_length=100)
    event_type = models.ForeignKey('TypeOfEvent', on_delete=models.CASCADE, related_name='event_type')
    event_description = models.TextField(verbose_name='descrizione')
    """ event_date = models.ForeignKey('AvailableDates', on_delete=models.CASCADE, related_name='event_dates') """
    event_organizer = models.ForeignKey('Organizer', on_delete=models.CASCADE, related_name='event_organizer')
    event_creation_date = models.DateTimeField(auto_now_add=True)
    event_image = models.ImageField(upload_to='static/images/', null=True, blank=True)

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ['event_date']
        verbose_name = 'evento'
        verbose_name_plural = 'eventi'

class Organizer(models.Model):
    organizer_name = models.CharField(max_length=50, verbose_name='nome organizzatore')
    organizer_description = models.TextField(verbose_name='descrizione')
    organizer_email = models.EmailField(    verbose_name='email')
    organizer_phone = models.CharField(max_length=15,   verbose_name='telefono')

    def __str__(self):
        return self.organizer_name

    class Meta:
        verbose_name = 'organizzatore'
        verbose_name_plural = 'organizzatori'

class TypeOfEvent(models.Model):
    event_types = models.CharField(max_length=50, verbose_name='tipo di evento')

    def __str__(self)->str:
        return self.event_types

    class Meta:
        verbose_name = 'tipo di evento'
        verbose_name_plural = 'tipi di evento'

class AvailableDates(models.Model):
    """ event_date_from = models.DateField()
    event_date_to = models.DateField() """
    date_from = models.DateField(verbose_name='data inizio')
    date_to = models.DateField(verbose_name='data fine')
    related_event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='event_date')

    def __str__(self):
        return str(self.date_from) + ' - ' + str(self.date_to)
    
    class Meta:
        verbose_name = 'data disponibile'
        verbose_name_plural = 'date disponibili'