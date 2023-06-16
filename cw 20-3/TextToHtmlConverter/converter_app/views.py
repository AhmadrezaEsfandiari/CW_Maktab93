from django.shortcuts import render
from django.utils.html import escape

def converter(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        converted_html = escape(text).replace('\n', '<br>')
        return render(request, 'converter_app/result.html', {'converted_html': converted_html})
    else:
        return render(request, 'converter_app/converter.html')