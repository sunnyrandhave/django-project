from django.shortcuts import render

def single_page(request):
    return render(request, 'demo/single_page.html')
