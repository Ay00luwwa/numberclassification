# Number Classification API

A Django REST API that classifies numbers based on their mathematical properties and provides a fun fact fetched from the Numbers API. This API evaluates whether a number is prime, perfect, Armstrong, and whether it's odd or even. It also returns the sum of its digits.

## Features

- **Number Classification**: Determines if the number is prime, perfect, Armstrong, and whether it's odd or even.
- **Digit Sum Calculation**: Computes the sum of all digits in the given number.
- **Fun Fact**: Retrieves an interesting math fact about the number from the [Numbers API](http://numbersapi.com/).
- **CORS Support**: Only allows requests from a specified list of origins.
- **JSON Response Format**: All responses are returned in JSON format.

## Technologies Used

- Python 3.13
- Django
- Django REST Framework
- django-cors-headers
- Requests

## Installation

### Prerequisites

- Python 3.10 or greater installed on your system.
- `pip` package manager.

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Ay00luwwa/numberclassification.git
   cd number-classification-api
