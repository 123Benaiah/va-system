from django.shortcuts import render, redirect
from .models import VerbalAutopsy
from .forms import VerbalAutopsyForm


def home(request):
    """Welcome page with links to the other pages."""
    return render(request, 'va/home.html')


def record_list(request):
    """List all verbal autopsy records, newest first."""
    records = VerbalAutopsy.objects.order_by('-created_at')
    return render(request, 'va/record_list.html', {'records': records})


def add_record(request):
    """Show empty form on GET, save new record on POST."""
    if request.method == 'POST':
        form = VerbalAutopsyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('va:record_list')
    else:
        form = VerbalAutopsyForm()
    return render(request, 'va/add_record.html', {'form': form})
