import re
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

def is_armstrong(num):
    """
    Check if a non-negative integer is an Armstrong number.
    For negative numbers, we consider the property as not applicable.
    """
    # Only consider Armstrong numbers for non-negative integers.
    if num < 0:
        return False
    digits = [int(d) for d in str(num)]
    return sum(d ** len(digits) for d in digits) == num

@api_view(["GET"])
def classify_number(request):
    # Retrieve the number parameter
    number_param = request.GET.get("number")
    
    # Validate: Allow optional leading '-' and digits only.
    # If invalid, return the error JSON with number set to "alphabet".
    if not number_param or not re.match(r"^-?\d+$", number_param):
        return JsonResponse({"number": "alphabet", "error": True}, status=400)
    
    # At this point, we have a valid integer string.
    num = int(number_param)
    
    # Compute digit sum using the absolute value (ignores '-' sign).
    digit_sum = sum(int(d) for d in str(abs(num)))
    
    # Determine properties.
    properties = []
    # Armstrong property: Only check if the number is non-negative.
    if num >= 0 and is_armstrong(num):
        properties.append("armstrong")
    
    # Add odd/even property (works for negative numbers as well).
    properties.append("odd" if num % 2 != 0 else "even")
    
    # Prime: Only numbers greater than 1 are considered prime.
    is_prime = False
    if num > 1:
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    
    # Perfect: Only consider positive numbers.
    is_perfect = False
    if num > 0:
        is_perfect = sum(i for i in range(1, num) if num % i == 0) == num

    # For the fun fact, use the absolute value to ensure a valid lookup.
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



# import requests
# from django.http import JsonResponse
# from rest_framework.decorators import api_view


# def is_armstrong(num):
#     digits = [int(d) for d in str(num)]
#     return sum(d**len(digits) for d in digits) == num


# @api_view(["GET"])
# def classify_number(request):
#     number = request.GET.get("number")

    
#     if not number or not number.isdigit():
#         return JsonResponse({"number": number, "error": True}, status=400)

#     num = int(number)
#     properties = []
    
    
#     if is_armstrong(num):
#         properties.append("armstrong")
    
#     properties.append("odd" if num % 2 else "even")
    
#     digit_sum = sum(int(d) for d in str(num))
    
    
#     fun_fact_url = f"http://numbersapi.com/{num}/math"
#     fun_fact = requests.get(fun_fact_url).text

#     response_data = {
#         "number": num,
#         "is_prime": num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)),
#         "is_perfect": sum(i for i in range(1, num) if num % i == 0) == num,
#         "properties": properties,
#         "digit_sum": digit_sum,
#         "fun_fact": fun_fact,
#     }
    
#     return JsonResponse(response_data, status=200)
