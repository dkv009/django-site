from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/homePage.html')

def contact(request):
    return render(request, 'mainapp/basic.html', {'values': ['Если у вас остались вопросы звоните по номеру:', 'Телефон: 8 747 777 77 77', 'Email: dmitry.k@gmail.com']})    