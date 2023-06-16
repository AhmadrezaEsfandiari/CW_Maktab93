from django.shortcuts import render

def home(request):
    return render(request, 'calculator_app/calculator.html')

def add(request, num1, num2):
    result = num1 + num2
    return render(request, 'calculator_app/add.html', {'num1': num1, 'num2': num2, 'result': result})

def subtract(request, num1, num2):
    result = num1 - num2
    return render(request, 'calculator_app/subtract.html', {'num1': num1, 'num2': num2, 'result': result})

def multiply(request, num1, num2):
    result = num1 * num2
    return render(request, 'calculator_app/multiply.html', {'num1': num1, 'num2': num2, 'result': result})

def divide(request, num1, num2):
    result = num1 / num2
    return render(request, 'calculator_app/divide.html', {'num1': num1, 'num2': num2, 'result': result})