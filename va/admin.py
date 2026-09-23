from django.contrib import admin

from django.contrib import admin
from .models import VerbalAutopsy


@admin.register(VerbalAutopsy)
class VerbalAutopsyAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = (
        'deceased_name',
        'sex',
        'age_at_death',
        'place_of_death',
        'interview_date',
    )
