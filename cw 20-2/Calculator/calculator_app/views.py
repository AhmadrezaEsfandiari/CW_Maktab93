from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'calculator_app/home.html')

def add(request, num1, num2):
    result = num1 + num2
    return render(request, 'calculator_app/result.html', {'result': result})

def subtract(request, num1, num2):
    result = num1 - num2
    return render(request, 'calculator_app/result.html', {'result': result})

def multiply(request, num1, num2):
    result = num1 * num2
    return render(request, 'calculator_app/result.html', {'result': result})

def divide(request, num1, num2):
    result = num1 / num2
    return render(request, 'calculator_app/result.html', {'result': result})