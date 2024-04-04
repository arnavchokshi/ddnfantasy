from django.shortcuts import render
from .models import Placings  # Import the Placings model

def real_placings(request):
    # Retrieve all real placings from the database
    real_placings = Placings.objects.all()

    # Pass the real placings data to the template for rendering
    return render(request, 'real_placings.html', {'real_placings': real_placings})
