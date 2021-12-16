from django.shortcuts import render


# Create your views here.

def index_view(request):
    return render(request, 'index.html')

def add(a,b):
    sum = a+b
    return sum
def subtract(a,b):
    sub = a-b
    return sub
def multiply(a,b):
    mul = a*b
    return mul
def divide(a,b):
    div = a/b
    return div

def calculations(request):

    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        num_1 = int(request.POST.get("first"))
        num_2 = int(request.POST.get("second"))
        context = {"result": None,
                   "evaluate": None,
                   "first": request.POST.get('first'),
                   "second": request.POST.get('second'),
                   "message": "Result:",
                   "equal": "="
        }

        if request.POST.get("cal") == "add":
            context['result'] = add(num_1, num_2)
            context['evaluate'] = "+"
        elif request.POST.get("cal") == "subtract":
            context['result'] = subtract(num_1, num_2)
            context['evaluate'] = "-"
        elif request.POST.get("cal") == "multiply":
            context['result'] = multiply(num_1, num_2)
            context['evaluate'] = "*"
        elif request.POST.get("cal") == "divide":
            context['result'] = divide(num_1, num_2)
            context['evaluate'] = "/"
        return render(request, 'index.html', context)
