from django.db import models

class VerbalAutopsy(models.Model):
    """A single verbal autopsy record."""

    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    PLACE_CHOICES = [
        ('Hospital', 'Hospital'),
        ('Home', 'Home'),
        ('Other', 'Other'),
    ]

    deceased_name = models.CharField(max_length=200)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age_at_death = models.IntegerField()
    date_of_death = models.DateField()
    place_of_death = models.CharField(max_length=20, choices=PLACE_CHOICES)
    respondent_name = models.CharField(max_length=200)
    respondent_relationship = models.CharField(max_length=100)
    interview_date = models.DateField()
    symptoms = models.TextField()
    probable_cause_of_death = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.deceased_name
