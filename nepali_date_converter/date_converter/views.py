from django.shortcuts import render

# Create your views here.
from nepali.datetime import NepaliDate

def convert_to_nepali_date(request):
    if request.method == 'POST':
        gregorian_date = request.POST['gregorian_date']
        year, month, day = map(int, gregorian_date.split('-'))
        nepali_date = NepaliDate.to_nepali_date(year, month, day)
        return render(request, 'date_converter/result.html', {'nepali_date': nepali_date})
    else:
        return render(request, 'date_converter/form.html')
