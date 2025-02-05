import re
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

def is_armstrong(num):
    """
    Check if a non-negative integer is an Armstrong number.
    For negative numbers, we consider the property as not applicable.
    """

    if num < 0:
        return False
    digits = [int(d) for d in str(num)]
    return sum(d ** len(digits) for d in digits) == num

@api_view(["GET"])
def classify_number(request):

    number_param = request.GET.get("number")
    
    if not number_param or not re.match(r"^-?\d+$", number_param):
        return JsonResponse({"number": "alphabet", "error": True}, status=400)
    
    num = int(number_param)
    
    digit_sum = sum(int(d) for d in str(abs(num)))
    
    properties = []
    
    if num >= 0 and is_armstrong(num):
        properties.append("armstrong")
    

    properties.append("odd" if num % 2 != 0 else "even")
    

    is_prime = False
    if num > 1:
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    
    
    is_perfect = False
    if num > 0:
        is_perfect = sum(i for i in range(1, num) if num % i == 0) == num

    .
    fun_fact_url = f"http://numbersapi.com/{abs(num)}/math"
    try:
        response = requests.get(fun_fact_url, timeout=5)
        fun_fact = response.text if response.status_code == 200 else ""
    except requests.RequestException:
        fun_fact = ""
    
    response_data = {
        "number": num,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact,
    }
    
    return JsonResponse(response_data, status=200)