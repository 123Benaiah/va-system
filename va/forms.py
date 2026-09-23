from django import forms
from .models import VerbalAutopsy


class VerbalAutopsyForm(forms.ModelForm):
    """Form for adding a verbal autopsy record."""

    class Meta:
        model = VerbalAutopsy
        fields = '__all__'
        widgets = {
            # Browser-native date pickers
            'date_of_death': forms.DateInput(attrs={'type': 'date'}),
            'interview_date': forms.DateInput(attrs={'type': 'date'}),
            # Multi-line input for symptoms
            'symptoms': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Bootstrap form-control to every field
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
