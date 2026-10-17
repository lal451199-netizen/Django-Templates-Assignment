from django.shortcuts import render
from datetime import date

def index(request):
    context = {
        'first_name': 'HISHAM',
        'last_name': 'ALKAHLOUT',
        'student_id': 120231599,
        'address': 'gaza palestine',
        'email': 'lal451199@gmail.com',
        'date_of_birth': date(2005,12,13),
    }

    return render(request, 'pages/index.html', context)


