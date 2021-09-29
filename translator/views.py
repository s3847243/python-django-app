from . import translate
from django.shortcuts import render

# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        # output = original_text.upper()
        output = translate.translate(original_text)
        return render(request,'translator.html',{'output_text':output,'original_text':original_text})
    else:
        return render(request,'translator.html')
