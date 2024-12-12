# Flask RESTful API for Product Management

## Overview

This project implements a RESTful API using Flask to manage a collection of product information. The API supports operations for adding, retrieving, updating, and deleting product records. It is designed for easy integration and provides a simple interface for developers.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete products.
- **In-Memory Storage**: Uses an in-memory data structure for testing purposes.
- **Concurrency Handling**: Implements thread safety using locks to handle concurrent requests.
- **Logging**: Provides logging for important events and errors.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask
- pytest (for testing)

### Installation

#1. Clone the repository:
   ```bash
   git clone https://github.com/Joeches/flask-product-api.git
   cd flask-product-api
 
 #Create a virtual environment:  
python -m venv venv

Activate the virtual environment:
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate


# Install the required packages:
pip install -r requirements.txt


# API Endpoints
Method	Endpoint	Description
POST	/products	Create a new product
GET	/products	Retrieve all products
GET	/products/<id>	Retrieve a specific product by ID
PUT	/products/<id>	Update an existing product
DELETE	/products/<id>	Delete a specific product by ID

Request and Response Formats
Create Product (POST /products)

#Request Body:
{
    "name": "Product A",
    "price": 10.99
}

#Response:
Status: 201 Created
Body:

{
    "id": 1,
    "name": "Product A",
    "price": 10.99
}


Get All Products (GET /products)
Response:
Status: 200 OK
Body:

[
    {
        "id": 1,
        "name": "Product A",
        "price": 10.99
    },
    {
        "id": 2,
        "name": "Product B",
        "price": 15.49
    }
]

Get Product by ID (GET /products/<id>)
Response:
Status: 200 OK (if found)
Body:

{
    "id": 1,
    "name": "Product A",
    "price": 10.99
}

Status: 404 Not Found (if not found)

Update Product (PUT /products/<id>)
#Request Body:
{
    "name": "Updated Product A",
    "price": 12.99
}

Response:
Status: 200 OK
Body:

{
    "id": 1,
    "name": "Updated Product A",
    "price": 12.99
}

Delete Product (DELETE /products/<id>)
Response:
Status: 200 OK
Body:

{
    "message": "Product deleted successfully."
}

Error Handling
The API returns appropriate HTTP status codes and error messages for various scenarios:
400 Bad Request: Returned when the input data is invalid.
404 Not Found: Returned when a requested resource does not exist.

Testing the API
To run the tests, ensure you are in the project directory and execute:

pytest test_app.py

Challenges Faced:
"One challenge I encountered was ensuring thread safety when handling concurrent requests. I addressed this by implementing locks…"






   

