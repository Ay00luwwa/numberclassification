import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view


def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return sum(d**len(digits) for d in digits) == num


@api_view(["GET"])
def classify_number(request):
    number = request.GET.get("number")

    
    if not number or not number.isdigit():
        return JsonResponse({"number": number, "error": True}, status=400)

    num = int(number)
    properties = []
    
    
    if is_armstrong(num):
        properties.append("armstrong")
    
    properties.append("odd" if num % 2 else "even")
    
    digit_sum = sum(int(d) for d in str(num))
    
    
    fun_fact_url = f"http://numbersapi.com/{num}/math"
    fun_fact = requests.get(fun_fact_url).text

    response_data = {
        "number": num,
        "is_prime": num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)),
        "is_perfect": sum(i for i in range(1, num) if num % i == 0) == num,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact,
    }
    
    return JsonResponse(response_data, status=200)
