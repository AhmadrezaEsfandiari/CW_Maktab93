from django.shortcuts import render

def converter(request):
    return render(request, 'converter_app/converter.html')