from django.shortcuts import render


def hello_test(request):
    return render(request,'hello_test.html')

# Create your views here.
