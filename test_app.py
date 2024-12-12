import pytest
import json
from app import app, products  # Import products from app.py


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Reset the products dictionary before each test
        products.clear()  # Clear products before each test
        yield client


def test_create_product(client):
    """Test creating a new product."""
    response = client.post('/products', json={'name': 'Product A', 'price': 10.99})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'Product A'
    assert data['price'] == 10.99


def test_get_products(client):
    """Test retrieving all products."""
    # First, create some products
    client.post('/products', json={'name': 'Product A', 'price': 10.99})
    client.post('/products', json={'name': 'Product B', 'price': 15.49})

    response = client.get('/products')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 2  # Ensure there are two products


def test_get_product(client):
    """Test retrieving a specific product by ID."""
    response = client.post('/products', json={'name': 'Product C', 'price': 20.00})
    product_id = json.loads(response.data)['id']

    response = client.get(f'/products/{product_id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == 'Product C'


def test_update_product(client):
    """Test updating an existing product."""
    response = client.post('/products', json={'name': 'Product D', 'price': 30.00})
    product_id = json.loads(response.data)['id']

    response = client.put(f'/products/{product_id}', json={'name': 'Updated Product D'})
    assert response.status_code == 200
    updated_data = json.loads(response.data)
    assert updated_data['name'] == 'Updated Product D'


def test_delete_product(client):
    """Test deleting a specific product by ID."""
    response = client.post('/products', json={'name': 'Product E', 'price': 25.00})
    product_id = json.loads(response.data)['id']

    response = client.delete(f'/products/{product_id}')
    assert response.status_code == 200
    assert b'Product deleted successfully.' in response.data


def test_get_nonexistent_product(client):
    """Test retrieving a nonexistent product."""
    response = client.get('/products/999')  # Assuming this ID does not exist
    assert response.status_code == 404


def test_create_product_invalid(client):
    """Test creating a product with invalid data."""
    response = client.post('/products', json={'name': 'Invalid Product'})
    assert response.status_code == 400











