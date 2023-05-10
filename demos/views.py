from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculator(request):
    #return HttpResponse("첫 장고: 계산기 구현")
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')
    
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    else:
        result = 0
        
    return render(request, 'calculator.html', {'result' : result})
#이렇게 만들면 html이 중괄호 안의 변수를 사용할 수 있게 된다.